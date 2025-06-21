# Create UI components directory and StatsCard component
os.makedirs('dvulndb-prototype/frontend/src/components/ui', exist_ok=True)

stats_card = '''import { LucideIcon } from 'lucide-react'
import { TrendingUp, TrendingDown } from 'lucide-react'

interface StatsCardProps {
  title: string
  value: string
  icon: LucideIcon
  trend?: string
  trendDirection?: 'up' | 'down'
  description?: string
}

export default function StatsCard({
  title,
  value,
  icon: Icon,
  trend,
  trendDirection,
  description
}: StatsCardProps) {
  return (
    <div className="card">
      <div className="flex items-center justify-between">
        <div className="space-y-2">
          <p className="text-sm font-medium text-gray-400">{title}</p>
          <p className="text-2xl font-bold text-white">{value}</p>
          {description && (
            <p className="text-xs text-gray-500">{description}</p>
          )}
        </div>
        <div className="p-3 bg-primary-600/20 rounded-lg">
          <Icon className="h-6 w-6 text-primary-400" />
        </div>
      </div>
      
      {trend && (
        <div className="flex items-center mt-4 pt-4 border-t border-gray-700">
          <div className={`flex items-center space-x-1 text-sm ${
            trendDirection === 'up' 
              ? 'text-green-400' 
              : 'text-red-400'
          }`}>
            {trendDirection === 'up' ? (
              <TrendingUp className="h-4 w-4" />
            ) : (
              <TrendingDown className="h-4 w-4" />
            )}
            <span>{trend}</span>
          </div>
          <span className="text-gray-500 text-sm ml-2">from last month</span>
        </div>
      )}
    </div>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/ui/StatsCard.tsx', 'w') as f:
    f.write(stats_card)

# Create VulnerabilityCard component
os.makedirs('dvulndb-prototype/frontend/src/components/vulnerability', exist_ok=True)

vulnerability_card = '''import Link from 'next/link'
import { Clock, User, DollarSign } from 'lucide-react'
import SeverityBadge from '@/components/ui/SeverityBadge'
import StatusBadge from '@/components/ui/StatusBadge'

interface VulnerabilityCardProps {
  vulnerability: {
    id: number
    title: string
    severity: number
    status: string
    researcher: string
    bounty: string
    submittedAt: string
  }
  showDetails?: boolean
}

export default function VulnerabilityCard({ 
  vulnerability, 
  showDetails = true 
}: VulnerabilityCardProps) {
  return (
    <Link href={`/vulnerabilities/${vulnerability.id}`}>
      <div className="card-hover">
        <div className="space-y-4">
          {/* Header */}
          <div className="flex items-start justify-between">
            <div className="space-y-2 flex-1">
              <h3 className="text-lg font-semibold text-white hover:text-primary-400 transition-colors">
                {vulnerability.title}
              </h3>
              <div className="flex items-center space-x-3">
                <SeverityBadge severity={vulnerability.severity} />
                <StatusBadge status={vulnerability.status} />
              </div>
            </div>
            <div className="text-right space-y-1">
              <div className="flex items-center text-green-400 text-sm font-medium">
                <DollarSign className="h-4 w-4 mr-1" />
                {vulnerability.bounty}
              </div>
            </div>
          </div>

          {/* Details */}
          {showDetails && (
            <div className="flex items-center justify-between text-sm text-gray-400 pt-4 border-t border-gray-700">
              <div className="flex items-center space-x-4">
                <div className="flex items-center space-x-1">
                  <User className="h-4 w-4" />
                  <span>{vulnerability.researcher}</span>
                </div>
                <div className="flex items-center space-x-1">
                  <Clock className="h-4 w-4" />
                  <span>{vulnerability.submittedAt}</span>
                </div>
              </div>
              <span className="text-primary-400 text-xs font-medium">
                #{vulnerability.id}
              </span>
            </div>
          )}
        </div>
      </div>
    </Link>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/vulnerability/VulnerabilityCard.tsx', 'w') as f:
    f.write(vulnerability_card)

# Create SeverityBadge component
severity_badge = '''interface SeverityBadgeProps {
  severity: number
  size?: 'sm' | 'md' | 'lg'
}

export default function SeverityBadge({ severity, size = 'md' }: SeverityBadgeProps) {
  const getSeverityConfig = (level: number) => {
    if (level >= 9) return { label: 'Critical', className: 'severity-critical' }
    if (level >= 7) return { label: 'High', className: 'severity-high' }
    if (level >= 4) return { label: 'Medium', className: 'severity-medium' }
    if (level >= 2) return { label: 'Low', className: 'severity-low' }
    return { label: 'Info', className: 'severity-info' }
  }

  const config = getSeverityConfig(severity)
  
  const sizeClasses = {
    sm: 'px-2 py-0.5 text-xs',
    md: 'px-2.5 py-0.5 text-xs',
    lg: 'px-3 py-1 text-sm'
  }

  return (
    <span className={`badge ${config.className} ${sizeClasses[size]}`}>
      {config.label} ({severity}/10)
    </span>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/ui/SeverityBadge.tsx', 'w') as f:
    f.write(severity_badge)

# Create StatusBadge component
status_badge = '''interface StatusBadgeProps {
  status: string
  size?: 'sm' | 'md' | 'lg'
}

export default function StatusBadge({ status, size = 'md' }: StatusBadgeProps) {
  const getStatusConfig = (status: string) => {
    switch (status.toLowerCase()) {
      case 'submitted':
        return { label: 'Submitted', className: 'status-submitted' }
      case 'validating':
        return { label: 'Validating', className: 'status-validating' }
      case 'confirmed':
        return { label: 'Confirmed', className: 'status-confirmed' }
      case 'rejected':
        return { label: 'Rejected', className: 'status-rejected' }
      case 'disclosed':
        return { label: 'Disclosed', className: 'status-disclosed' }
      default:
        return { label: 'Unknown', className: 'bg-gray-600 text-gray-100' }
    }
  }

  const config = getStatusConfig(status)
  
  const sizeClasses = {
    sm: 'px-2 py-0.5 text-xs',
    md: 'px-2.5 py-0.5 text-xs',
    lg: 'px-3 py-1 text-sm'
  }

  return (
    <span className={`badge ${config.className} ${sizeClasses[size]}`}>
      {config.label}
    </span>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/ui/StatusBadge.tsx', 'w') as f:
    f.write(status_badge)

# Create RecentActivity component
recent_activity = '''import { Activity, Shield, Award, TrendingUp } from 'lucide-react'

export default function RecentActivity() {
  const activities = [
    {
      id: 1,
      type: 'vulnerability',
      description: 'New critical vulnerability submitted',
      time: '2 min ago',
      icon: Shield,
      color: 'text-red-400'
    },
    {
      id: 2,
      type: 'bounty',
      description: 'Bounty of 2.5 ETH paid out',
      time: '15 min ago',
      icon: Award,
      color: 'text-green-400'
    },
    {
      id: 3,
      type: 'validation',
      description: 'Vulnerability validated by 3 experts',
      time: '1 hour ago',
      icon: TrendingUp,
      color: 'text-blue-400'
    }
  ]

  return (
    <div className="card">
      <div className="flex items-center space-x-2 mb-6">
        <Activity className="h-5 w-5 text-primary-400" />
        <h3 className="text-lg font-semibold text-white">Recent Activity</h3>
      </div>
      
      <div className="space-y-4">
        {activities.map((activity) => {
          const Icon = activity.icon
          return (
            <div key={activity.id} className="flex items-start space-x-3">
              <div className={`p-2 rounded-lg bg-gray-800 ${activity.color}`}>
                <Icon className="h-4 w-4" />
              </div>
              <div className="flex-1 space-y-1">
                <p className="text-sm text-gray-300">{activity.description}</p>
                <p className="text-xs text-gray-500">{activity.time}</p>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/dashboard/RecentActivity.tsx', 'w') as f:
    f.write(recent_activity)

# Create TopResearchers component
top_researchers = '''import { Users, Award, TrendingUp } from 'lucide-react'

export default function TopResearchers() {
  const researchers = [
    {
      rank: 1,
      address: '0x1234...5678',
      vulnerabilities: 42,
      earnings: '28.5 ETH',
      reputation: 2450
    },
    {
      rank: 2,
      address: '0xabcd...efgh',
      vulnerabilities: 38,
      earnings: '24.2 ETH',
      reputation: 2180
    },
    {
      rank: 3,
      address: '0x9876...5432',
      vulnerabilities: 35,
      earnings: '21.8 ETH',
      reputation: 1950
    }
  ]

  const getRankColor = (rank: number) => {
    switch (rank) {
      case 1: return 'text-yellow-400'
      case 2: return 'text-gray-300'
      case 3: return 'text-orange-400'
      default: return 'text-gray-500'
    }
  }

  return (
    <div className="card">
      <div className="flex items-center space-x-2 mb-6">
        <Users className="h-5 w-5 text-primary-400" />
        <h3 className="text-lg font-semibold text-white">Top Researchers</h3>
      </div>
      
      <div className="space-y-4">
        {researchers.map((researcher) => (
          <div key={researcher.rank} className="flex items-center space-x-4 p-3 bg-gray-800/50 rounded-lg">
            <div className={`text-xl font-bold ${getRankColor(researcher.rank)}`}>
              #{researcher.rank}
            </div>
            <div className="flex-1 space-y-1">
              <div className="font-medium text-white">{researcher.address}</div>
              <div className="flex items-center space-x-4 text-xs text-gray-400">
                <span className="flex items-center space-x-1">
                  <Award className="h-3 w-3" />
                  <span>{researcher.vulnerabilities} vulns</span>
                </span>
                <span className="flex items-center space-x-1">
                  <TrendingUp className="h-3 w-3" />
                  <span>{researcher.reputation}</span>
                </span>
              </div>
            </div>
            <div className="text-right">
              <div className="text-sm font-medium text-green-400">{researcher.earnings}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/dashboard/TopResearchers.tsx', 'w') as f:
    f.write(top_researchers)

print("UI components created!")