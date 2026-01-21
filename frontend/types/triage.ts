// TypeScript types matching the backend Pydantic schemas
// These use camelCase to match the backend's alias_generator

export interface TriageRequest {
  ticketText: string;
}

export interface TriageMeta {
  model: string;
  fallbackUsed: boolean;
  confidence: number;
}

export interface TriageResponse {
  summary: string;
  intent: string;
  urgency: string;
  nextStep: string;
  meta: TriageMeta;
}
