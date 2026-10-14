import { render, screen } from '@testing-library/react'
import { afterEach, describe, expect, it, vi } from 'vitest'

import { App } from './App'

vi.mock('../lib/apiClient', () => ({
  apiClient: {
    get: vi.fn().mockRejectedValue(new Error('network unavailable in tests')),
  },
}))

function navigateTo(path: string) {
  window.history.pushState({}, '', path)
}

describe('routing', () => {
  afterEach(() => {
    navigateTo('/')
  })

  it('renders the admin page at /admin', async () => {
    navigateTo('/admin')
    render(<App />)
    expect(await screen.findByRole('heading', { name: /admin panel/i })).toBeInTheDocument()
  })

  it('renders the not found page for an unknown route', async () => {
    navigateTo('/this-route-does-not-exist')
    render(<App />)
    expect(await screen.findByRole('heading', { name: /404/i })).toBeInTheDocument()
  })
})
