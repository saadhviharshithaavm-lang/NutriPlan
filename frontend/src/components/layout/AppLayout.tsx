import { Outlet } from 'react-router'

import { Footer } from './Footer'
import { NavBar } from './NavBar'

export function AppLayout() {
  return (
    <div className="flex min-h-screen flex-col bg-warm-50">
      <NavBar />
      <main className="mx-auto w-full max-w-5xl flex-1 px-4 py-8">
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}
