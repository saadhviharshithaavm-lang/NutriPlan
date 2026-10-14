/** Mirrors backend/app/schemas/health.py. */
export interface HealthResponse {
  status: string
  environment: string
  app_name: string
}

/** Mirrors backend/app/core/errors.py's consistent error envelope. */
export interface ApiErrorBody {
  error: string
  details?: unknown
}
