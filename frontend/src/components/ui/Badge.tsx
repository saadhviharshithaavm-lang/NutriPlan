import type { HTMLAttributes } from 'react'

type Tone = 'neutral' | 'success' | 'warning' | 'danger'

interface BadgeProps extends HTMLAttributes<HTMLSpanElement> {
  tone?: Tone
}

const toneClasses: Record<Tone, string> = {
  neutral: 'bg-warm-200 text-ink-700',
  success: 'bg-leaf-100 text-leaf-700',
  warning: 'bg-amber-100 text-amber-800',
  danger: 'bg-red-100 text-red-800',
}

export function Badge({ tone = 'neutral', className = '', ...props }: BadgeProps) {
  return (
    <span
      className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${toneClasses[tone]} ${className}`}
      {...props}
    />
  )
}
