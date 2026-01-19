# AI Support Ticket Triage System - Next Steps Plan

## Current Status ✅

**Completed:**

- Backend scaffolding with FastAPI
- Mock API with keyword-based triage logic
- Pydantic schemas (TriageRequest, TriageResponse, TriageMeta)
- CORS middleware configured for frontend
- Health check endpoint
- Basic project structure

**Current Structure:**

```
support-triage-ai/
├── backend/
│   ├── app/
│   │   ├── main.py          ✅ (mock triage endpoint)
│   │   ├── schemas.py        ✅ (Pydantic models)
│   │   └── __init__.py
│   └── requirements.txt      ✅
└── README.md
```

## Next Steps Roadmap

### Phase 1: Frontend Foundation (Next)

**Goal:** Create a basic React + TypeScript frontend to test the mock API

**Tasks:**

1. Initialize React + TypeScript project with Vite
2. Set up project structure (components, types, lib)
3. Create Zod schemas matching backend Pydantic models
4. Build API client to call `/triage` endpoint
5. Create basic UI:
   - Text input component for ticket content
   - Submit button
   - Results display component
   - Loading and error states

**Files to Create:**

- `frontend/package.json`
- `frontend/tsconfig.json`
- `frontend/vite.config.ts`
- `frontend/src/App.tsx`
- `frontend/src/types/ticket.ts` (TypeScript interfaces)
- `frontend/src/lib/schemas.ts` (Zod validation)
- `frontend/src/lib/api.ts` (API client)
- `frontend/src/components/TicketInput.tsx`
- `frontend/src/components/TicketResults.tsx`

**Dependencies:**

- react, react-dom
- typescript
- vite
- zod
- axios (or fetch)
- tailwindcss (optional, for styling)

---

### Phase 2: Database Integration

**Goal:** Store processed tickets for history and analytics

**Tasks:**

1. Add SQLAlchemy and database dependencies
2. Create database models (Ticket table)
3. Set up SQLite database connection
4. Create database session management
5. Add endpoints:
   - `POST /api/tickets` - Save analyzed ticket
   - `GET /api/tickets` - List tickets (paginated)
   - `GET /api/tickets/{id}` - Get specific ticket

**Files to Create:**

- `backend/app/database.py` (SQLAlchemy setup)
- `backend/app/models/ticket.py` (Database model)
- Update `backend/app/main.py` (add new endpoints)

**Dependencies to Add:**

- sqlalchemy
- alembic (for migrations, optional)

---

### Phase 3: AI Integration (Hugging Face)

**Goal:** Replace mock logic with real AI-powered triage

**Tasks:**

1. Add Hugging Face API client dependency (httpx)
2. Create AI service module
3. Design prompt for structured output
4. Implement API call with retry logic
5. Parse AI response and validate structure
6. Integrate with existing triage endpoint
7. Keep mock logic as fallback

**Files to Create:**

- `backend/app/services/ai_service.py`
- `backend/app/services/validation_service.py`
- `.env.example` (for API key)
- Update `backend/app/main.py` (use AI service)

**Dependencies to Add:**

- httpx
- python-dotenv

**Environment Variables:**

- `HUGGING_FACE_API_KEY`

---

### Phase 4: Enhanced Validation & Fallback

**Goal:** Robust error handling and graceful degradation

**Tasks:**

1. Enhance validation service with multiple fallback strategies
2. Add regex-based extraction as secondary fallback
3. Implement confidence scoring
4. Add logging for debugging
5. Handle edge cases (empty text, API failures, etc.)

**Files to Update:**

- `backend/app/services/validation_service.py`
- `backend/app/services/ai_service.py`

---

### Phase 5: Frontend Enhancement

**Goal:** Complete UI with history and better UX

**Tasks:**

1. Add ticket history component
2. Implement search/filter functionality
3. Add urgency/intent badges with colors
4. Improve styling and responsive design
5. Add error boundaries
6. Implement proper TypeScript types throughout

**Files to Create:**

- `frontend/src/components/TicketHistory.tsx`
- Update existing components with better styling

---

### Phase 6: Production Polish

**Goal:** Make it production-ready

**Tasks:**

1. Add rate limiting
2. Add request/response logging
3. Add comprehensive error handling
4. Update README with full setup instructions
5. Add environment variable validation
6. Add tests (optional but recommended)
7. Add Docker setup (optional)

## Architecture Flow

```
User Input (Frontend)
    ↓
POST /triage
    ↓
AI Service (Hugging Face API)
    ↓
Validation Service (with fallbacks)
    ↓
Save to Database (optional)
    ↓
Return Structured Response
    ↓
Display Results (Frontend)
```

## Key Design Decisions

1. **Structured Output:** Use JSON schema in prompt + post-processing validation
2. **Fallback Strategy:** AI → Regex/Pattern Matching → Default values
3. **Database:** SQLite for simplicity (easy migration to PostgreSQL later)
4. **Validation:** Pydantic (backend) + Zod (frontend) for type safety
5. **Error Handling:** Graceful degradation at each step

## Next Immediate Step

**Start with Phase 1: Frontend Foundation**

This will allow you to:

- Test the existing mock API visually
- Establish the frontend structure
- Set up TypeScript types and Zod validation
- Create a foundation for future enhancements

Would you like to proceed with Phase 1, or would you prefer to tackle a different phase first?
