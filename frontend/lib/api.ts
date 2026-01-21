import { TriageRequest, TriageResponse } from "@/types/triage";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function triageTicket(
  request: TriageRequest
): Promise<TriageResponse> {
  const response = await fetch(`${API_BASE_URL}/triage`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Triage request failed: ${error}`);
  }

  return response.json();
}

export async function checkHealth(): Promise<{ ok: boolean }> {
  const response = await fetch(`${API_BASE_URL}/health`);
  if (!response.ok) {
    throw new Error("Health check failed");
  }
  return response.json();
}
