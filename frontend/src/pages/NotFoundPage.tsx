import { NavLink } from 'react-router'

import { Button } from '../components/ui/Button'

export function NotFoundPage() {
  return (
    <div className="flex flex-col items-center gap-3 py-20 text-center">
      <h1 className="text-3xl font-semibold text-ink-900">404</h1>
      <p className="text-ink-500">This page doesn't exist.</p>
      <NavLink to="/">
        <Button variant="primary">Back to home</Button>
      </NavLink>
    </div>
  )
}
