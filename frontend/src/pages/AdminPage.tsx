import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

const adminSections = [
  { label: 'Foods', req: 'REQ-4.7.2' },
  { label: 'Recipes', req: 'REQ-4.7.3' },
  { label: 'Nutrition values', req: 'REQ-4.7.4' },
  { label: 'Categories', req: 'REQ-4.7.5' },
]

export function AdminPage() {
  return (
    <div>
      <h1 className="text-xl font-semibold text-ink-900">Admin panel</h1>
      <p className="mt-1 text-sm text-ink-500">REQ-4.7.1 – REQ-4.7.5</p>

      <div className="mt-4">
        <PlannedFeatureNotice
          milestone="Milestone 5"
          description="Admin access control (REQ-4.7.1) isn't implemented yet, so this route has no real authorization guard in Milestone 0 — do not treat it as protected."
        />
      </div>

      <div className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
        {adminSections.map((section) => (
          <Card key={section.label}>
            <p className="text-xs text-ink-500">{section.req}</p>
            <h2 className="mt-1 font-semibold text-ink-900">{section.label}</h2>
            <p className="mt-2 text-sm text-ink-500">CRUD screen not built yet</p>
          </Card>
        ))}
      </div>
    </div>
  )
}
