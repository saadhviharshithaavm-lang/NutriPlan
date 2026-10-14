import { useParams } from 'react-router'

import { Button } from '../components/ui/Button'
import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

export function MealDetailsPage() {
  const { recipeId } = useParams()

  return (
    <div className="mx-auto max-w-xl">
      <h1 className="text-xl font-semibold text-ink-900">Meal details</h1>
      <p className="mt-1 text-sm text-ink-500">REQ-4.4.1 – REQ-4.4.4, REQ-4.5.1 – REQ-4.5.5</p>

      <Card className="mt-4">
        <p className="text-sm text-ink-700">
          Recipe <span className="font-mono">#{recipeId ?? '—'}</span> details, ingredients, and
          nutrition will appear here once meal generation (Milestone 3) is implemented.
        </p>
        <div className="mt-4 flex flex-wrap gap-2">
          <Button variant="secondary" disabled>
            👍 Like
          </Button>
          <Button variant="secondary" disabled>
            👎 Dislike
          </Button>
          <Button variant="secondary" disabled>
            ⏭ Skip
          </Button>
          <Button variant="secondary" disabled>
            ⭐ Favorite
          </Button>
          <Button variant="primary" disabled>
            Replace meal
          </Button>
        </div>
      </Card>

      <div className="mt-4">
        <PlannedFeatureNotice
          milestone="Milestone 4"
          description="Feedback capture and meal replacement are disabled until the feedback and rule-engine ranking modules are implemented."
        />
      </div>
    </div>
  )
}
