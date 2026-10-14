import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
const slots = ['Breakfast', 'Lunch', 'Dinner', 'Snack']

export function MealPlanPage() {
  return (
    <div>
      <h1 className="text-xl font-semibold text-ink-900">Weekly meal plan</h1>
      <p className="mt-1 text-sm text-ink-500">REQ-4.2.1 – REQ-4.2.8</p>

      <div className="mt-4">
        <PlannedFeatureNotice
          milestone="Milestone 3"
          description="The rule engine that fills this grid (diet, allergy, budget, cooking-time, and variety rules) is not implemented yet — see app/rule_engine/ in the backend."
        />
      </div>

      <div className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-7">
        {days.map((day) => (
          <Card key={day} className="flex flex-col gap-2">
            <h2 className="text-sm font-semibold text-ink-900">{day}</h2>
            {slots.map((slot) => (
              <div
                key={slot}
                className="rounded-md border border-dashed border-warm-300 p-2 text-xs text-ink-500"
              >
                <span className="font-medium text-ink-700">{slot}</span>
                <br />
                Not generated yet
              </div>
            ))}
          </Card>
        ))}
      </div>
    </div>
  )
}
