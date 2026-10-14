import { NavLink } from 'react-router'

import { Button } from '../components/ui/Button'
import { Card } from '../components/ui/Card'

const features = [
  {
    title: 'Weekly meal plans',
    description: 'A full 7-day plan of breakfast, lunch, dinner, and snacks, built around your diet, allergies, and budget.',
  },
  {
    title: 'Grocery lists, automatically',
    description: 'Ingredients across the week combined into one deduplicated shopping list.',
  },
  {
    title: 'Budget and time aware',
    description: 'Every meal respects your weekly budget in ₹ and the cooking time you actually have.',
  },
  {
    title: 'Learns from feedback',
    description: 'Like, dislike, skip, or favourite a meal, and future plans adjust accordingly.',
  },
]

export function LandingPage() {
  return (
    <div className="flex flex-col gap-10">
      <section className="text-center">
        <h1 className="text-3xl font-semibold text-ink-900 sm:text-4xl">
          Adaptive meal planning, built around your lifestyle
        </h1>
        <p className="mx-auto mt-3 max-w-xl text-ink-500">
          NutriPlan generates a personalized weekly meal plan and grocery list from your
          dietary preferences, health goal, budget, and available cooking time.
        </p>
        <div className="mt-6 flex justify-center gap-3">
          <NavLink to="/register">
            <Button variant="primary">Get started</Button>
          </NavLink>
          <NavLink to="/login">
            <Button variant="secondary">Log in</Button>
          </NavLink>
        </div>
      </section>

      <section className="grid grid-cols-1 gap-4 sm:grid-cols-2">
        {features.map((feature) => (
          <Card key={feature.title}>
            <h2 className="font-semibold text-ink-900">{feature.title}</h2>
            <p className="mt-1 text-sm text-ink-500">{feature.description}</p>
          </Card>
        ))}
      </section>

      <p className="text-center text-xs text-ink-500">
        Nutrition values and meal costs shown anywhere in NutriPlan are estimates for planning
        purposes, not medical or financial advice.
      </p>
    </div>
  )
}
