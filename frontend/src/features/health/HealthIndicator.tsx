import { Badge } from '../../components/ui/Badge'
import { useHealthCheck } from '../../hooks/useHealthCheck'

export function HealthIndicator() {
  const { status } = useHealthCheck()

  if (status === 'loading') {
    return <Badge tone="neutral">Checking API…</Badge>
  }

  if (status === 'online') {
    return <Badge tone="success">API connected</Badge>
  }

  return <Badge tone="danger">API unreachable</Badge>
}
