import { zodResolver } from '@hookform/resolvers/zod'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { NavLink } from 'react-router'
import { z } from 'zod'

import { Button } from '../components/ui/Button'
import { Card } from '../components/ui/Card'
import { PlannedFeatureNotice } from '../components/ui/PlannedFeatureNotice'

const registerSchema = z
  .object({
    email: z.string().email('Enter a valid email address.'),
    password: z.string().min(8, 'Password must be at least 8 characters.'),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: 'Passwords do not match.',
    path: ['confirmPassword'],
  })

type RegisterFormValues = z.infer<typeof registerSchema>

export function RegisterPage() {
  const [submitted, setSubmitted] = useState(false)
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterFormValues>({ resolver: zodResolver(registerSchema) })

  const onSubmit = handleSubmit(async () => {
    setSubmitted(true)
  })

  return (
    <div className="mx-auto max-w-sm">
      <Card>
        <h1 className="text-xl font-semibold text-ink-900">Create your account</h1>
        <p className="mt-1 text-sm text-ink-500">REQ-4.1.1</p>

        <form className="mt-4 flex flex-col gap-3" onSubmit={onSubmit} noValidate>
          <label className="text-sm font-medium text-ink-700" htmlFor="email">
            Email
            <input
              id="email"
              type="email"
              className="mt-1 w-full rounded-lg border border-warm-300 px-3 py-2 text-sm"
              {...register('email')}
            />
            {errors.email && (
              <span className="mt-1 block text-xs text-red-600">{errors.email.message}</span>
            )}
          </label>

          <label className="text-sm font-medium text-ink-700" htmlFor="password">
            Password
            <input
              id="password"
              type="password"
              className="mt-1 w-full rounded-lg border border-warm-300 px-3 py-2 text-sm"
              {...register('password')}
            />
            {errors.password && (
              <span className="mt-1 block text-xs text-red-600">{errors.password.message}</span>
            )}
          </label>

          <label className="text-sm font-medium text-ink-700" htmlFor="confirmPassword">
            Confirm password
            <input
              id="confirmPassword"
              type="password"
              className="mt-1 w-full rounded-lg border border-warm-300 px-3 py-2 text-sm"
              {...register('confirmPassword')}
            />
            {errors.confirmPassword && (
              <span className="mt-1 block text-xs text-red-600">
                {errors.confirmPassword.message}
              </span>
            )}
          </label>

          <Button type="submit" disabled={isSubmitting} className="mt-2">
            Create account
          </Button>
        </form>

        {submitted && (
          <div className="mt-4">
            <PlannedFeatureNotice
              milestone="Milestone 1"
              description="Form validation works, but there is no registration backend yet — this submit intentionally does not create an account."
            />
          </div>
        )}

        <p className="mt-4 text-center text-sm text-ink-500">
          Already have an account?{' '}
          <NavLink to="/login" className="font-medium text-leaf-600">
            Log in
          </NavLink>
        </p>
      </Card>
    </div>
  )
}
