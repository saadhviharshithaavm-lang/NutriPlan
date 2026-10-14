import { useState } from 'react'
import { NavLink } from 'react-router'

import { HealthIndicator } from '../../features/health/HealthIndicator'

const navItems = [
  { to: '/', label: 'Home', end: true },
  { to: '/meal-plan', label: 'Meal Plan' },
  { to: '/grocery-list', label: 'Grocery List' },
  { to: '/dashboard', label: 'Dashboard' },
  { to: '/admin', label: 'Admin' },
]

const linkClasses = ({ isActive }: { isActive: boolean }) =>
  `rounded-md px-3 py-2 text-sm font-medium transition-colors ${
    isActive ? 'bg-leaf-100 text-leaf-700' : 'text-ink-700 hover:bg-warm-100'
  }`

export function NavBar() {
  const [menuOpen, setMenuOpen] = useState(false)

  return (
    <header className="border-b border-warm-200 bg-white">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-4 py-3">
        <NavLink to="/" className="flex items-center gap-2 text-lg font-semibold text-ink-900">
          <span aria-hidden="true">🥗</span>
          NutriPlan
        </NavLink>

        <nav className="hidden items-center gap-1 md:flex" aria-label="Primary">
          {navItems.map((item) => (
            <NavLink key={item.to} to={item.to} end={item.end} className={linkClasses}>
              {item.label}
            </NavLink>
          ))}
        </nav>

        <div className="hidden items-center gap-3 md:flex">
          <HealthIndicator />
          <NavLink
            to="/login"
            className="rounded-lg bg-leaf-600 px-3 py-2 text-sm font-medium text-white hover:bg-leaf-700"
          >
            Log in
          </NavLink>
        </div>

        <button
          type="button"
          className="rounded-md p-2 text-ink-700 hover:bg-warm-100 md:hidden"
          aria-label="Toggle navigation menu"
          aria-expanded={menuOpen}
          onClick={() => setMenuOpen((open) => !open)}
        >
          <span aria-hidden="true">{menuOpen ? '✕' : '☰'}</span>
        </button>
      </div>

      {menuOpen && (
        <nav className="flex flex-col gap-1 border-t border-warm-200 px-4 py-3 md:hidden" aria-label="Primary">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={linkClasses}
              onClick={() => setMenuOpen(false)}
            >
              {item.label}
            </NavLink>
          ))}
          <NavLink
            to="/login"
            className="rounded-lg bg-leaf-600 px-3 py-2 text-center text-sm font-medium text-white"
            onClick={() => setMenuOpen(false)}
          >
            Log in
          </NavLink>
          <div className="pt-2">
            <HealthIndicator />
          </div>
        </nav>
      )}
    </header>
  )
}
