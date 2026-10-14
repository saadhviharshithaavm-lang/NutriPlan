import { render, screen } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'

import { apiClient } from '../../lib/apiClient'
import { HealthIndicator } from './HealthIndicator'

vi.mock('../../lib/apiClient', () => ({
  apiClient: { get: vi.fn() },
}))

describe('HealthIndicator', () => {
  it('shows "API connected" when the real health endpoint responds', async () => {
    vi.mocked(apiClient.get).mockResolvedValueOnce({
      data: { status: 'ok', environment: 'test', app_name: 'NutriPlan API' },
    })

    render(<HealthIndicator />)

    expect(await screen.findByText(/api connected/i)).toBeInTheDocument()
    expect(apiClient.get).toHaveBeenCalledWith('/health')
  })

  it('shows "API unreachable" when the health request fails', async () => {
    vi.mocked(apiClient.get).mockRejectedValueOnce(new Error('network error'))

    render(<HealthIndicator />)

    expect(await screen.findByText(/api unreachable/i)).toBeInTheDocument()
  })
})
