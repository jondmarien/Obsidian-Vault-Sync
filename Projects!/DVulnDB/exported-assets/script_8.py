# Create Web3 configuration
web3_config = '''import { createWeb3Modal } from '@web3modal/wagmi/react'
import { defaultWagmiConfig } from '@web3modal/wagmi/react/config'
import { WagmiConfig } from 'wagmi'
import { arbitrum, mainnet, polygon, sepolia, hardhat } from 'wagmi/chains'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

// 1. Get projectId from https://cloud.walletconnect.com
const projectId = process.env.NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID || ''

// 2. Create wagmiConfig
const metadata = {
  name: 'Decentralized Vulnerability Database',
  description: 'Secure vulnerability disclosure platform with cryptocurrency bounties',
  url: 'https://dvulndb.com', // origin must match your domain & subdomain
  icons: ['https://avatars.githubusercontent.com/u/37784886']
}

const chains = [sepolia, hardhat, mainnet, arbitrum, polygon] as const

export const config = defaultWagmiConfig({
  chains,
  projectId,
  metadata,
  enableWalletConnect: true,
  enableInjected: true,
  enableEIP6963: true,
  enableCoinbase: true,
})

// 3. Create modal
createWeb3Modal({
  wagmiConfig: config,
  projectId,
  enableAnalytics: true,
  themeMode: 'dark',
  themeVariables: {
    '--w3m-color-mix': '#1f2937',
    '--w3m-color-mix-strength': 20,
    '--w3m-accent': '#3b82f6',
    '--w3m-border-radius-master': '8px',
  }
})

export default config'''

with open('dvulndb-prototype/frontend/src/config/web3.ts', 'w') as f:
    f.write(web3_config)

# Create contract configurations
contract_config = '''// Contract ABIs and addresses
export const CONTRACTS = {
  VulnerabilityRegistry: {
    address: process.env.NEXT_PUBLIC_CONTRACT_REGISTRY_ADDRESS as `0x${string}`,
    abi: [
      'function submitVulnerability(bytes32 _targetHash, uint8 _severity, string _ipfsHash, string[] _toolOutputs) external payable',
      'function validateVulnerability(uint256 _vulnId, bool _approved) external',
      'function getVulnerabilityDetails(uint256 _vulnId) external view returns (address researcher, uint8 severity, uint8 status, uint256 submissionTime, uint256 disclosureTime, string ipfsHash, bool isDisclosed)',
      'function getResearcherProfile(address _researcher) external view returns (tuple(uint256 totalSubmissions, uint256 confirmedVulnerabilities, uint256 totalEarnings, uint256 reputationScore, bool isActive, uint256 lastSubmission))',
      'function getTotalVulnerabilities() external view returns (uint256)',
      'function isValidator(address _address) external view returns (bool)',
      'event VulnerabilitySubmitted(uint256 indexed vulnId, address indexed researcher, bytes32 targetHash, uint8 severity, uint256 bountyAmount)',
      'event VulnerabilityValidated(uint256 indexed vulnId, address indexed validator, bool approved)',
      'event VulnerabilityConfirmed(uint256 indexed vulnId, uint256 bountyAmount)',
      'event BountyPaid(uint256 indexed vulnId, address indexed researcher, uint256 amount)'
    ]
  },
  BountyEscrow: {
    address: process.env.NEXT_PUBLIC_CONTRACT_ESCROW_ADDRESS as `0x${string}`,
    abi: [
      'function getEscrowDetails(uint256 _vulnId) external view returns (address researcher, uint256 amount, uint256 depositTime, uint8 status, uint256 approvalCount, bool isDisputed)',
      'function approveBountyRelease(uint256 _vulnId) external',
      'function getTotalEscrowed() external view returns (uint256)',
      'function isApprover(address _address) external view returns (bool)'
    ]
  },
  ReputationNFT: {
    address: process.env.NEXT_PUBLIC_CONTRACT_REPUTATION_ADDRESS as `0x${string}`,
    abi: [
      'function getResearcherData(uint256 _tokenId) external view returns (tuple(uint256 reputationScore, uint256 vulnerabilitiesFound, uint256 totalEarnings, uint256 lastUpdate, uint8 level, string[] specializations, uint256[] criticalFinds))',
      'function getTokenIdByAddress(address _researcher) external view returns (uint256)',
      'function tokenURI(uint256 tokenId) external view returns (string)',
      'function balanceOf(address owner) external view returns (uint256)',
      'function ownerOf(uint256 tokenId) external view returns (address)'
    ]
  }
} as const

// Vulnerability status enum
export const VULNERABILITY_STATUS = {
  SUBMITTED: 0,
  VALIDATING: 1,
  CONFIRMED: 2,
  REJECTED: 3,
  DISCLOSED: 4
} as const

// Severity levels with colors
export const SEVERITY_LEVELS = {
  1: { label: 'Informational', color: 'bg-gray-500', textColor: 'text-gray-100' },
  2: { label: 'Low', color: 'bg-blue-500', textColor: 'text-blue-100' },
  3: { label: 'Low', color: 'bg-blue-600', textColor: 'text-blue-100' },
  4: { label: 'Medium', color: 'bg-yellow-500', textColor: 'text-yellow-100' },
  5: { label: 'Medium', color: 'bg-yellow-600', textColor: 'text-yellow-100' },
  6: { label: 'Medium', color: 'bg-orange-500', textColor: 'text-orange-100' },
  7: { label: 'High', color: 'bg-orange-600', textColor: 'text-orange-100' },
  8: { label: 'High', color: 'bg-red-500', textColor: 'text-red-100' },
  9: { label: 'Critical', color: 'bg-red-600', textColor: 'text-red-100' },
  10: { label: 'Critical', color: 'bg-red-700', textColor: 'text-red-100' }
} as const

// Reputation levels
export const REPUTATION_LEVELS = {
  0: { name: 'Novice', color: '#8B9DC3', minScore: 0 },
  1: { name: 'Researcher', color: '#16A085', minScore: 101 },
  2: { name: 'Expert', color: '#F39C12', minScore: 501 },
  3: { name: 'Elite', color: '#8E44AD', minScore: 1501 },
  4: { name: 'Legendary', color: '#E74C3C', minScore: 5000 }
} as const

// Network configurations
export const SUPPORTED_NETWORKS = {
  11155111: {
    name: 'Sepolia',
    rpcUrl: 'https://eth-sepolia.g.alchemy.com/v2/',
    blockExplorer: 'https://sepolia.etherscan.io',
    nativeCurrency: { name: 'ETH', symbol: 'ETH', decimals: 18 }
  },
  31337: {
    name: 'Hardhat',
    rpcUrl: 'http://127.0.0.1:8545',
    blockExplorer: 'http://localhost:8545',
    nativeCurrency: { name: 'ETH', symbol: 'ETH', decimals: 18 }
  }
} as const

export type SeverityLevel = keyof typeof SEVERITY_LEVELS
export type VulnerabilityStatus = keyof typeof VULNERABILITY_STATUS
export type ReputationLevel = keyof typeof REPUTATION_LEVELS'''

with open('dvulndb-prototype/frontend/src/config/contracts.ts', 'w') as f:
    f.write(contract_config)

# Create TypeScript types
types_file = '''// Core types for the application
export interface Vulnerability {
  id: number
  researcher: string
  severity: number
  status: VulnerabilityStatus
  submissionTime: number
  disclosureTime: number
  ipfsHash: string
  isDisclosed: boolean
  bountyAmount: bigint
  targetHash: string
  toolOutputs: string[]
}

export interface ResearcherProfile {
  totalSubmissions: number
  confirmedVulnerabilities: number
  totalEarnings: bigint
  reputationScore: number
  isActive: boolean
  lastSubmission: number
}

export interface EscrowDetails {
  researcher: string
  amount: bigint
  depositTime: number
  status: EscrowStatus
  approvalCount: number
  isDisputed: boolean
}

export interface ReputationNFTData {
  reputationScore: number
  vulnerabilitiesFound: number
  totalEarnings: bigint
  lastUpdate: number
  level: ReputationLevel
  specializations: string[]
  criticalFinds: number[]
}

export enum VulnerabilityStatus {
  SUBMITTED = 0,
  VALIDATING = 1,
  CONFIRMED = 2,
  REJECTED = 3,
  DISCLOSED = 4
}

export enum EscrowStatus {
  DEPOSITED = 0,
  RELEASED = 1,
  REFUNDED = 2,
  DISPUTED = 3
}

export enum ReputationLevel {
  NOVICE = 0,
  RESEARCHER = 1,
  EXPERT = 2,
  ELITE = 3,
  LEGENDARY = 4
}

export interface VulnerabilitySubmission {
  targetUrl: string
  targetDescription: string
  severity: number
  title: string
  description: string
  reproductionSteps: string[]
  proofOfConcept: string
  toolOutputs: File[]
  bountyAmount: string
}

export interface ToolOutput {
  name: string
  type: 'nmap' | 'nikto' | 'burp' | 'custom'
  content: string
  size: number
  uploadedAt: Date
}

export interface IPFSUploadResult {
  hash: string
  size: number
  url: string
}

// UI Component Props
export interface VulnerabilityCardProps {
  vulnerability: Vulnerability
  onClick?: () => void
  showDetails?: boolean
}

export interface ResearcherBadgeProps {
  profile: ResearcherProfile
  address: string
  size?: 'sm' | 'md' | 'lg'
}

export interface SeverityBadgeProps {
  severity: number
  size?: 'sm' | 'md' | 'lg'
}

export interface StatusBadgeProps {
  status: VulnerabilityStatus
  size?: 'sm' | 'md' | 'lg'
}

// Form types
export interface FormFieldProps {
  label: string
  name: string
  required?: boolean
  error?: string
  children: React.ReactNode
}

export interface FileUploadProps {
  accept: string
  multiple?: boolean
  onUpload: (files: File[]) => void
  maxSize?: number
  maxFiles?: number
}

// Web3 hook return types
export interface UseVulnerabilityContract {
  submitVulnerability: (data: VulnerabilitySubmission) => Promise<void>
  validateVulnerability: (id: number, approved: boolean) => Promise<void>
  getVulnerability: (id: number) => Promise<Vulnerability | null>
  getTotalVulnerabilities: () => Promise<number>
  isValidator: (address: string) => Promise<boolean>
  isLoading: boolean
  error: string | null
}

export interface UseResearcherProfile {
  profile: ResearcherProfile | null
  nftData: ReputationNFTData | null
  tokenId: number | null
  isLoading: boolean
  error: string | null
  refresh: () => Promise<void>
}

// API response types
export interface APIResponse<T> {
  success: boolean
  data?: T
  error?: string
  message?: string
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  limit: number
  hasNext: boolean
  hasPrevious: boolean
}

// Analytics types
export interface DashboardStats {
  totalVulnerabilities: number
  totalBountyPaid: bigint
  activeResearchers: number
  avgSeverity: number
  recentSubmissions: Vulnerability[]
  topResearchers: Array<{
    address: string
    profile: ResearcherProfile
    rank: number
  }>
}'''

with open('dvulndb-prototype/frontend/src/types/index.ts', 'w') as f:
    f.write(types_file)

print("Web3 configuration and types created!")