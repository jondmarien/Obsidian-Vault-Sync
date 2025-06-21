# Create the main page component
main_page = '''import { Metadata } from 'next'
import DashboardPage from '@/components/dashboard/DashboardPage'

export const metadata: Metadata = {
  title: 'Dashboard | DVulnDB',
  description: 'Security researcher dashboard for the Decentralized Vulnerability Database',
}

export default function HomePage() {
  return <DashboardPage />
}'''

with open('dvulndb-prototype/frontend/src/app/page.tsx', 'w') as f:
    f.write(main_page)

# Create Dashboard component
dashboard_component = '''"use client"

import { useState, useEffect } from 'react'
import { useAccount } from 'wagmi'
import { Shield, TrendingUp, Users, DollarSign, Plus, Award, Activity } from 'lucide-react'
import Link from 'next/link'
import { motion } from 'framer-motion'
import StatsCard from '@/components/ui/StatsCard'
import VulnerabilityCard from '@/components/vulnerability/VulnerabilityCard'
import RecentActivity from '@/components/dashboard/RecentActivity'
import TopResearchers from '@/components/dashboard/TopResearchers'

export default function DashboardPage() {
  const { isConnected } = useAccount()
  
  // Mock data - in real app, this would come from Web3 hooks
  const [stats, setStats] = useState({
    totalVulnerabilities: 1337,
    totalBountyPaid: '89.42',
    activeResearchers: 234,
    avgSeverity: 6.8
  })

  const [recentVulnerabilities] = useState([
    {
      id: 1,
      title: 'SQL Injection in User Authentication',
      severity: 9,
      status: 'confirmed',
      researcher: '0x1234...5678',
      bounty: '2.5 ETH',
      submittedAt: '2 hours ago'
    },
    {
      id: 2,
      title: 'XSS in Comment System',
      severity: 6,
      status: 'validating',
      researcher: '0xabcd...efgh',
      bounty: '0.8 ETH',
      submittedAt: '5 hours ago'
    },
    {
      id: 3,
      title: 'CSRF in Admin Panel',
      severity: 7,
      status: 'submitted',
      researcher: '0x9876...5432',
      bounty: '1.2 ETH',
      submittedAt: '1 day ago'
    }
  ])

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  }

  const itemVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: {
      y: 0,
      opacity: 1,
      transition: {
        duration: 0.5
      }
    }
  }

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="text-center space-y-4"
      >
        <h1 className="text-4xl md:text-6xl font-bold text-gradient">
          Decentralized Vulnerability Database
        </h1>
        <p className="text-xl text-gray-400 max-w-3xl mx-auto">
          Secure the Web3 ecosystem through blockchain-based vulnerability disclosure 
          with cryptocurrency bounty rewards for ethical hackers.
        </p>
        
        {!isConnected && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
            className="mt-8"
          >
            <div className="bg-yellow-600/20 border border-yellow-600/30 rounded-lg p-4 max-w-md mx-auto">
              <p className="text-yellow-400 text-sm">
                💡 Connect your wallet to submit vulnerabilities and earn bounties
              </p>
            </div>
          </motion.div>
        )}
      </motion.div>

      {/* Stats Grid */}
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
      >
        <motion.div variants={itemVariants}>
          <StatsCard
            title="Total Vulnerabilities"
            value={stats.totalVulnerabilities.toLocaleString()}
            icon={Shield}
            trend="+12%"
            trendDirection="up"
          />
        </motion.div>
        
        <motion.div variants={itemVariants}>
          <StatsCard
            title="Bounties Paid"
            value={`${stats.totalBountyPaid} ETH`}
            icon={DollarSign}
            trend="+24%"
            trendDirection="up"
          />
        </motion.div>
        
        <motion.div variants={itemVariants}>
          <StatsCard
            title="Active Researchers"
            value={stats.activeResearchers.toLocaleString()}
            icon={Users}
            trend="+8%"
            trendDirection="up"
          />
        </motion.div>
        
        <motion.div variants={itemVariants}>
          <StatsCard
            title="Avg. Severity"
            value={stats.avgSeverity.toFixed(1)}
            icon={TrendingUp}
            trend="-0.2"
            trendDirection="down"
          />
        </motion.div>
      </motion.div>

      {/* Quick Actions */}
      {isConnected && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="grid grid-cols-1 md:grid-cols-3 gap-6"
        >
          <Link href="/submit" className="group">
            <div className="card-hover group-hover:glow-effect">
              <div className="flex items-center space-x-4">
                <div className="p-3 bg-primary-600/20 rounded-lg group-hover:bg-primary-600/30 transition-colors">
                  <Plus className="h-6 w-6 text-primary-400" />
                </div>
                <div>
                  <h3 className="font-semibold text-white">Submit Vulnerability</h3>
                  <p className="text-sm text-gray-400">Report a new security finding</p>
                </div>
              </div>
            </div>
          </Link>

          <Link href="/profile" className="group">
            <div className="card-hover group-hover:glow-effect">
              <div className="flex items-center space-x-4">
                <div className="p-3 bg-green-600/20 rounded-lg group-hover:bg-green-600/30 transition-colors">
                  <Award className="h-6 w-6 text-green-400" />
                </div>
                <div>
                  <h3 className="font-semibold text-white">View Profile</h3>
                  <p className="text-sm text-gray-400">Check your reputation & earnings</p>
                </div>
              </div>
            </div>
          </Link>

          <Link href="/vulnerabilities" className="group">
            <div className="card-hover group-hover:glow-effect">
              <div className="flex items-center space-x-4">
                <div className="p-3 bg-orange-600/20 rounded-lg group-hover:bg-orange-600/30 transition-colors">
                  <Activity className="h-6 w-6 text-orange-400" />
                </div>
                <div>
                  <h3 className="font-semibold text-white">Browse Database</h3>
                  <p className="text-sm text-gray-400">Explore public disclosures</p>
                </div>
              </div>
            </div>
          </Link>
        </motion.div>
      )}

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Recent Vulnerabilities */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.3 }}
          className="lg:col-span-2 space-y-6"
        >
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-bold text-white">Recent Vulnerabilities</h2>
            <Link href="/vulnerabilities" className="btn-ghost text-sm">
              View All
            </Link>
          </div>
          
          <div className="space-y-4">
            {recentVulnerabilities.map((vuln, index) => (
              <motion.div
                key={vuln.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 * index }}
              >
                <VulnerabilityCard vulnerability={vuln} />
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Sidebar */}
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.4 }}
          className="space-y-8"
        >
          <RecentActivity />
          <TopResearchers />
        </motion.div>
      </div>
    </div>
  )
}'''

# Create dashboard directory and component
os.makedirs('dvulndb-prototype/frontend/src/components/dashboard', exist_ok=True)
with open('dvulndb-prototype/frontend/src/components/dashboard/DashboardPage.tsx', 'w') as f:
    f.write(dashboard_component)

print("Main page and dashboard component created!")