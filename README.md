# Support Triage AI

AI-powered support ticket summarization and triage system.

## Quick Start

### Using pnpm (Recommended)

```bash
pnpm start
```

This will automatically:

- Create a Python virtual environment if it doesn't exist
- Install Python dependencies if needed
- Start the development server on `http://localhost:8000`

**Note:** This project uses Python, but we've set up `package.json` for convenience so you can use familiar commands like `pnpm start`. The actual dependencies are managed through Python's `pip` and `requirements.txt`.

### Option 2: Make commands

```bash
make start
# or
make dev
```

### Option 3: Direct script

**Linux/Mac:**

```bash
./start.sh
```

**Windows:**

```bash
start.bat
```

### Option 4: From backend directory

```bash
cd backend
./start.sh
```

All methods will automatically:

- Create a virtual environment if it doesn't exist
- Install dependencies if needed
- Start the development server on `http://localhost:8000`

## Backend Setup

### Manual Setup (if you prefer)

The script will automatically:

- Create a virtual environment if it doesn't exist
- Install dependencies if needed
- Start the development server

### Manual Setup

If you prefer to set up manually:

1. Navigate to the backend directory:

```bash
cd backend
```

2. Create a virtual environment:

```bash
python3 -m venv venv  # On Linux/Mac
python -m venv venv    # On Windows
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the development server:

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /triage` - Analyze a support ticket

### Example Request

```bash
curl -X POST "http://localhost:8000/triage" \
  -H "Content-Type: application/json" \
  -d '{"ticket_text": "I cannot log in to my account"}'
```

### Example Response

```json
{
  "summary": "Auto-triage (mock): extracted key issue from the ticket and prepared routing details.",
  "intent": "auth_sso_issue",
  "urgency": "P0",
  "next_step": "Collect IdP config (audience/client ID, redirect URI) and escalate to on-call.",
  "meta": {
    "model": "mock_rules_v1",
    "fallback_used": true,
    "confidence": 0.55
  }
}
```

## API Documentation

Once the server is running, visit:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
