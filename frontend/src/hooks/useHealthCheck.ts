import { useEffect, useState } from 'react'

import { apiClient } from '../lib/apiClient'
import type { HealthResponse } from '../types/api'

export type HealthCheckStatus = 'loading' | 'online' | 'offline'

export interface HealthCheckResult {
  status: HealthCheckStatus
  data: HealthResponse | null
}

/**
 * Calls the real `GET /api/v1/health` endpoint so the UI reflects whether the
 * FastAPI backend is actually reachable, rather than assuming it is.
 */
export function useHealthCheck(): HealthCheckResult {
  const [status, setStatus] = useState<HealthCheckStatus>('loading')
  const [data, setData] = useState<HealthResponse | null>(null)

  useEffect(() => {
    let cancelled = false

    apiClient
      .get<HealthResponse>('/health')
      .then((response) => {
        if (cancelled) return
        setData(response.data)
        setStatus('online')
      })
      .catch(() => {
        if (cancelled) return
        setStatus('offline')
      })

    return () => {
      cancelled = true
    }
  }, [])

  return { status, data }
}
