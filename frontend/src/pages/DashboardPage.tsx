import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

const summaryTiles = [
  { label: 'Weekly calories', req: 'REQ-4.6.1' },
  { label: 'Estimated spend vs. budget', req: 'REQ-4.6.2' },
  { label: 'Meal statistics', req: 'REQ-4.6.3' },
  { label: 'Favorite meals', req: 'REQ-4.6.4' },
]

export function DashboardPage() {
  return (
    <div>
      <h1 className="text-xl font-semibold text-ink-900">Dashboard</h1>
      <p className="mt-1 text-sm text-ink-500">REQ-4.6.1 – REQ-4.6.4</p>

      <div className="mt-4">
        <PlannedFeatureNotice
          milestone="Milestone 5"
          description="These tiles will show your real weekly figures once meal plans and feedback data exist to summarize. No placeholder numbers are shown below."
        />
      </div>

      <div className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
        {summaryTiles.map((tile) => (
          <Card key={tile.label}>
            <p className="text-xs text-ink-500">{tile.req}</p>
            <h2 className="mt-1 font-semibold text-ink-900">{tile.label}</h2>
            <p className="mt-2 text-sm text-ink-500">No data yet</p>
          </Card>
        ))}
      </div>
    </div>
  )
}
