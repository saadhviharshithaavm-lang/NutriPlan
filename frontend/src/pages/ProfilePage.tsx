import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

const profileFields = [
  'Age',
  'Gender',
  'Height (cm)',
  'Weight (kg)',
  'Activity level',
  'Dietary preference',
  'Allergies',
  'Health goal (Weight Loss / Muscle Gain / Maintenance)',
  'Weekly grocery budget (₹)',
  'Available cooking time (minutes)',
]

export function ProfilePage() {
  return (
    <div className="mx-auto max-w-2xl">
      <h1 className="text-xl font-semibold text-ink-900">Profile setup</h1>
      <p className="mt-1 text-sm text-ink-500">REQ-4.1.3, REQ-4.1.4, REQ-4.1.5</p>

      <Card className="mt-4">
        <p className="text-sm text-ink-700">
          This is where you'll enter the attributes the recommendation engine uses to build
          your weekly plan:
        </p>
        <ul className="mt-3 grid grid-cols-1 gap-x-6 gap-y-1 text-sm text-ink-700 sm:grid-cols-2">
          {profileFields.map((field) => (
            <li key={field} className="flex items-center gap-2">
              <span aria-hidden="true" className="text-leaf-600">
                •
              </span>
              {field}
            </li>
          ))}
        </ul>
      </Card>

      <div className="mt-4">
        <PlannedFeatureNotice
          milestone="Milestone 1"
          description="Profile creation and editing requires the authentication system that lands in Milestone 1, so this form is not interactive yet."
        />
      </div>
    </div>
  )
}
