import { Badge } from './Badge'

interface PlannedFeatureNoticeProps {
  milestone: string
  description: string
}

/**
 * Every screen whose backend isn't implemented yet renders this instead of
 * fabricated data or a working-looking form, per the master prompt's
 * instruction not to make unfinished features appear functional.
 */
export function PlannedFeatureNotice({ milestone, description }: PlannedFeatureNoticeProps) {
  return (
    <div className="rounded-lg border border-dashed border-warm-300 bg-warm-100 p-4 text-sm text-ink-700">
      <div className="mb-1 flex items-center gap-2">
        <Badge tone="warning">Planned — {milestone}</Badge>
      </div>
      <p>{description}</p>
    </div>
  )
}
