import { render, screen } from '@testing-library/react'
import { describe, expect, it, vi } from 'vitest'

import { App } from './App'

vi.mock('../lib/apiClient', () => ({
  apiClient: {
    get: vi.fn().mockRejectedValue(new Error('network unavailable in tests')),
  },
}))

describe('App', () => {
  it('renders the landing page at the root route', async () => {
    render(<App />)
    expect(
      await screen.findByRole('heading', {
        name: /adaptive meal planning, built around your lifestyle/i,
      }),
    ).toBeInTheDocument()
  })

  it('renders the shared navigation layout', () => {
    render(<App />)
    expect(screen.getByRole('banner')).toBeInTheDocument()
    expect(screen.getByRole('navigation', { name: /primary/i })).toBeInTheDocument()
  })
})
