import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

export function GroceryListPage() {
  return (
    <div className="mx-auto max-w-xl">
      <h1 className="text-xl font-semibold text-ink-900">Grocery list</h1>
      <p className="mt-1 text-sm text-ink-500">REQ-4.3.1 – REQ-4.3.4</p>

      <Card className="mt-4 flex flex-col items-center gap-2 py-10 text-center">
        <span aria-hidden="true" className="text-3xl">
          🧺
        </span>
        <p className="text-sm text-ink-500">
          Your consolidated, quantity-aggregated grocery list will appear here once a weekly
          meal plan has been generated.
        </p>
      </Card>

      <div className="mt-4">
        <PlannedFeatureNotice
          milestone="Milestone 3"
          description="Grocery list aggregation depends on weekly meal plan generation, which is not implemented yet."
        />
      </div>
    </div>
  )
}
