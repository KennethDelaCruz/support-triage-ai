import os
import json
import re
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN", "").strip()
HF_MODEL = os.getenv("HF_MODEL", "meta-llama/Meta-Llama-3-8B-Instruct").strip()
HF_BASE_URL = os.getenv("HF_BASE_URL", "https://router.huggingface.co/v1").rstrip("/")
HF_TIMEOUT_SECONDS = float(os.getenv("HF_TIMEOUT_SECONDS", "25"))

CHAT_COMPLETIONS_URL = f"{HF_BASE_URL}/chat/completions"


def _build_messages(ticket_text: str):
    system = (
        "You are a support operations assistant. "
        "Return ONLY a single JSON object. No markdown, no prose."
    )
    user = (
        "Return ONLY valid JSON with keys: summary, intent, urgency, next_step.\n"
        "intent must be one of: billing_refund, bug_report, feature_request, auth_sso_issue, "
        "performance_outage, account_access, how_to_question, integration_issue, unknown.\n"
        "urgency must be one of: P0, P1, P2, P3.\n\n"
        f"Ticket:\n{ticket_text}"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def _extract_json(text: str):
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass

    m = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not m:
        raise ValueError("no_json_found")
    return json.loads(m.group(0))


def hf_generate_triage(ticket_text: str):
    """
    Returns dict or None. Prints debug info for failures.
    """
    if not HF_TOKEN:
        print("[hf] HF_TOKEN missing (env not loaded?)")
        return None

    payload = {
        "model": HF_MODEL,
        "messages": _build_messages(ticket_text),
        "temperature": 0.2,
        "max_tokens": 350,
    }

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    timeout = httpx.Timeout(HF_TIMEOUT_SECONDS, connect=5.0)

    try:
        with httpx.Client(timeout=timeout) as client:
            resp = client.post(CHAT_COMPLETIONS_URL, headers=headers, json=payload)
    except Exception as e:
        print(f"[hf] request exception: {repr(e)}")
        return None

    if resp.status_code != 200:
        print(f"[hf] HTTP {resp.status_code}")
        print(f"[hf] body: {resp.text[:500]}")
        return None

    try:
        data = resp.json()
    except Exception as e:
        print(f"[hf] response not json: {repr(e)} body={resp.text[:300]}")
        return None

    try:
        content = data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[hf] unexpected response shape: {repr(e)} data_keys={list(data.keys())}")
        print(f"[hf] data: {str(data)[:500]}")
        return None

    try:
        parsed = _extract_json(content)
        if isinstance(parsed, dict):
            return parsed
        print("[hf] parsed json is not an object")
        return None
    except Exception as e:
        print(f"[hf] json extract/parse failed: {repr(e)}")
        print(f"[hf] raw content: {content[:500]}")
        return None
