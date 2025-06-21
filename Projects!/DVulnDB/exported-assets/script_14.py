# Create Web3 hooks
web3_hooks = '''import { useState, useEffect } from 'react'
import { useAccount, useReadContract, useWriteContract, useWaitForTransaction } from 'wagmi'
import { CONTRACTS } from '@/config/contracts'
import { parseEther, formatEther } from 'viem'
import toast from 'react-hot-toast'

export function useVulnerabilityRegistry() {
  const { address } = useAccount()
  const { writeContract, isPending } = useWriteContract()
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const submitVulnerability = async (data: {
    targetUrl: string
    severity: number
    ipfsHash: string
    toolOutputs: string[]
    bountyAmount: string
  }) => {
    try {
      setIsLoading(true)
      setError(null)

      // Hash the target URL for privacy
      const targetHash = '0x' + Array.from(new TextEncoder().encode(data.targetUrl))
        .map(b => b.toString(16).padStart(2, '0'))
        .join('')

      const result = await writeContract({
        address: CONTRACTS.VulnerabilityRegistry.address,
        abi: CONTRACTS.VulnerabilityRegistry.abi,
        functionName: 'submitVulnerability',
        args: [targetHash, data.severity, data.ipfsHash, data.toolOutputs],
        value: parseEther(data.bountyAmount)
      })

      toast.success('Vulnerability submitted successfully!')
      return result
    } catch (err: any) {
      const errorMessage = err.message || 'Failed to submit vulnerability'
      setError(errorMessage)
      toast.error(errorMessage)
      throw err
    } finally {
      setIsLoading(false)
    }
  }

  const validateVulnerability = async (vulnId: number, approved: boolean) => {
    try {
      setIsLoading(true)
      setError(null)

      const result = await writeContract({
        address: CONTRACTS.VulnerabilityRegistry.address,
        abi: CONTRACTS.VulnerabilityRegistry.abi,
        functionName: 'validateVulnerability',
        args: [vulnId, approved]
      })

      toast.success(`Vulnerability ${approved ? 'approved' : 'rejected'}!`)
      return result
    } catch (err: any) {
      const errorMessage = err.message || 'Failed to validate vulnerability'
      setError(errorMessage)
      toast.error(errorMessage)
      throw err
    } finally {
      setIsLoading(false)
    }
  }

  return {
    submitVulnerability,
    validateVulnerability,
    isLoading: isLoading || isPending,
    error
  }
}

export function useVulnerabilityData(vulnId?: number) {
  const { data: totalVulns } = useReadContract({
    address: CONTRACTS.VulnerabilityRegistry.address,
    abi: CONTRACTS.VulnerabilityRegistry.abi,
    functionName: 'getTotalVulnerabilities'
  })

  const { data: vulnDetails } = useReadContract({
    address: CONTRACTS.VulnerabilityRegistry.address,
    abi: CONTRACTS.VulnerabilityRegistry.abi,
    functionName: 'getVulnerabilityDetails',
    args: vulnId ? [vulnId] : undefined,
    enabled: !!vulnId
  })

  return {
    totalVulnerabilities: totalVulns as number || 0,
    vulnerabilityDetails: vulnDetails as any || null
  }
}

export function useResearcherProfile(address?: string) {
  const { address: connectedAddress } = useAccount()
  const targetAddress = address || connectedAddress

  const { data: profile, refetch } = useReadContract({
    address: CONTRACTS.VulnerabilityRegistry.address,
    abi: CONTRACTS.VulnerabilityRegistry.abi,
    functionName: 'getResearcherProfile',
    args: targetAddress ? [targetAddress] : undefined,
    enabled: !!targetAddress
  })

  const { data: tokenId } = useReadContract({
    address: CONTRACTS.ReputationNFT.address,
    abi: CONTRACTS.ReputationNFT.abi,
    functionName: 'getTokenIdByAddress',
    args: targetAddress ? [targetAddress] : undefined,
    enabled: !!targetAddress
  })

  const { data: nftData } = useReadContract({
    address: CONTRACTS.ReputationNFT.address,
    abi: CONTRACTS.ReputationNFT.abi,
    functionName: 'getResearcherData',
    args: tokenId ? [tokenId] : undefined,
    enabled: !!tokenId && tokenId !== 0n
  })

  return {
    profile: profile as any || null,
    nftData: nftData as any || null,
    tokenId: tokenId as number || 0,
    refresh: refetch
  }
}

export function useValidatorStatus() {
  const { address } = useAccount()

  const { data: isValidator } = useReadContract({
    address: CONTRACTS.VulnerabilityRegistry.address,
    abi: CONTRACTS.VulnerabilityRegistry.abi,
    functionName: 'isValidator',
    args: address ? [address] : undefined,
    enabled: !!address
  })

  const { data: isApprover } = useReadContract({
    address: CONTRACTS.BountyEscrow.address,
    abi: CONTRACTS.BountyEscrow.abi,
    functionName: 'isApprover',
    args: address ? [address] : undefined,
    enabled: !!address
  })

  return {
    isValidator: !!isValidator,
    isApprover: !!isApprover
  }
}

export function useEscrowData(vulnId?: number) {
  const { data: totalEscrowed } = useReadContract({
    address: CONTRACTS.BountyEscrow.address,
    abi: CONTRACTS.BountyEscrow.abi,
    functionName: 'getTotalEscrowed'
  })

  const { data: escrowDetails } = useReadContract({
    address: CONTRACTS.BountyEscrow.address,
    abi: CONTRACTS.BountyEscrow.abi,
    functionName: 'getEscrowDetails',
    args: vulnId ? [vulnId] : undefined,
    enabled: !!vulnId
  })

  return {
    totalEscrowed: totalEscrowed ? formatEther(totalEscrowed as bigint) : '0',
    escrowDetails: escrowDetails as any || null
  }
}'''

with open('dvulndb-prototype/frontend/src/hooks/useWeb3.ts', 'w') as f:
    f.write(web3_hooks)

# Create IPFS utilities
ipfs_utils = '''import { create, IPFSHTTPClient } from 'ipfs-http-client'

// Initialize IPFS client
const projectId = process.env.NEXT_PUBLIC_INFURA_IPFS_PROJECT_ID
const projectSecret = process.env.NEXT_PUBLIC_INFURA_IPFS_PROJECT_SECRET

let ipfsClient: IPFSHTTPClient

if (projectId && projectSecret) {
  const auth = 'Basic ' + Buffer.from(projectId + ':' + projectSecret).toString('base64')
  
  ipfsClient = create({
    host: 'ipfs.infura.io',
    port: 5001,
    protocol: 'https',
    headers: {
      authorization: auth,
    },
  })
} else {
  // Fallback to local IPFS node
  ipfsClient = create({
    host: 'localhost',
    port: 5001,
    protocol: 'http',
  })
}

export interface IPFSUploadResult {
  hash: string
  size: number
  url: string
}

export interface VulnerabilityReport {
  title: string
  description: string
  targetUrl: string
  targetDescription: string
  severity: number
  reproductionSteps: string[]
  proofOfConcept: string
  toolOutputs: Array<{
    name: string
    type: string
    content: string
  }>
  submittedAt: string
  researcher: string
}

/**
 * Upload vulnerability report to IPFS
 */
export async function uploadVulnerabilityReport(
  report: VulnerabilityReport
): Promise<IPFSUploadResult> {
  try {
    // Encrypt sensitive data before upload
    const encryptedReport = await encryptReport(report)
    
    const result = await ipfsClient.add(JSON.stringify(encryptedReport), {
      progress: (prog) => console.log(`Upload progress: ${prog}`)
    })

    return {
      hash: result.cid.toString(),
      size: result.size,
      url: `https://ipfs.io/ipfs/${result.cid.toString()}`
    }
  } catch (error) {
    console.error('IPFS upload failed:', error)
    throw new Error('Failed to upload to IPFS')
  }
}

/**
 * Upload tool output files to IPFS
 */
export async function uploadToolOutputs(files: File[]): Promise<string[]> {
  try {
    const uploadPromises = files.map(async (file) => {
      const buffer = await file.arrayBuffer()
      const result = await ipfsClient.add(buffer, {
        pin: true
      })
      return result.cid.toString()
    })

    return await Promise.all(uploadPromises)
  } catch (error) {
    console.error('Tool output upload failed:', error)
    throw new Error('Failed to upload tool outputs')
  }
}

/**
 * Retrieve and decrypt vulnerability report from IPFS
 */
export async function getVulnerabilityReport(
  hash: string,
  isDisclosed: boolean = false
): Promise<VulnerabilityReport | null> {
  try {
    const stream = ipfsClient.cat(hash)
    const chunks = []
    
    for await (const chunk of stream) {
      chunks.push(chunk)
    }
    
    const data = Buffer.concat(chunks).toString()
    const encryptedReport = JSON.parse(data)
    
    // Only decrypt if the vulnerability is disclosed or user has permission
    if (isDisclosed) {
      return await decryptReport(encryptedReport)
    } else {
      // Return limited info for non-disclosed vulnerabilities
      return {
        ...encryptedReport,
        description: 'This vulnerability has not been disclosed yet.',
        reproductionSteps: [],
        proofOfConcept: 'Available after disclosure period.',
        toolOutputs: []
      }
    }
  } catch (error) {
    console.error('Failed to retrieve report:', error)
    return null
  }
}

/**
 * Simple encryption for demonstration (use proper encryption in production)
 */
async function encryptReport(report: VulnerabilityReport): Promise<any> {
  // In production, use proper encryption libraries like Web Crypto API
  // For now, just base64 encode sensitive fields
  return {
    ...report,
    description: btoa(report.description),
    reproductionSteps: report.reproductionSteps.map(step => btoa(step)),
    proofOfConcept: btoa(report.proofOfConcept),
    toolOutputs: report.toolOutputs.map(output => ({
      ...output,
      content: btoa(output.content)
    }))
  }
}

/**
 * Decrypt report data
 */
async function decryptReport(encryptedReport: any): Promise<VulnerabilityReport> {
  return {
    ...encryptedReport,
    description: atob(encryptedReport.description),
    reproductionSteps: encryptedReport.reproductionSteps.map((step: string) => atob(step)),
    proofOfConcept: atob(encryptedReport.proofOfConcept),
    toolOutputs: encryptedReport.toolOutputs.map((output: any) => ({
      ...output,
      content: atob(output.content)
    }))
  }
}

/**
 * Format file size for display
 */
export function formatFileSize(bytes: number): string {
  if (bytes === 0) return '0 Bytes'
  
  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
}

/**
 * Validate file type for tool outputs
 */
export function isValidToolOutput(file: File): boolean {
  const validTypes = [
    'text/xml',
    'text/plain',
    'application/json',
    'text/html',
    'application/xml'
  ]
  
  const validExtensions = ['.xml', '.txt', '.json', '.html', '.log', '.nmap', '.nikto']
  
  return validTypes.includes(file.type) || 
         validExtensions.some(ext => file.name.toLowerCase().endsWith(ext))
}

export default ipfsClient'''

with open('dvulndb-prototype/frontend/src/utils/ipfs.ts', 'w') as f:
    f.write(ipfs_utils)

# Create general utility functions
utils_file = '''import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

/**
 * Utility function for combining Tailwind CSS classes
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

/**
 * Format Ethereum address for display
 */
export function formatAddress(address: string, chars: number = 4): string {
  if (!address) return ''
  return `${address.slice(0, chars + 2)}...${address.slice(-chars)}`
}

/**
 * Format ETH amount for display
 */
export function formatEth(amount: string | number, decimals: number = 4): string {
  const num = typeof amount === 'string' ? parseFloat(amount) : amount
  return num.toFixed(decimals)
}

/**
 * Format large numbers with commas
 */
export function formatNumber(num: number): string {
  return num.toLocaleString()
}

/**
 * Calculate time ago from timestamp
 */
export function timeAgo(timestamp: number): string {
  const now = Date.now()
  const diff = now - timestamp * 1000 // Convert to milliseconds
  
  const seconds = Math.floor(diff / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  const days = Math.floor(hours / 24)
  const weeks = Math.floor(days / 7)
  const months = Math.floor(days / 30)
  const years = Math.floor(days / 365)
  
  if (years > 0) return `${years} year${years > 1 ? 's' : ''} ago`
  if (months > 0) return `${months} month${months > 1 ? 's' : ''} ago`
  if (weeks > 0) return `${weeks} week${weeks > 1 ? 's' : ''} ago`
  if (days > 0) return `${days} day${days > 1 ? 's' : ''} ago`
  if (hours > 0) return `${hours} hour${hours > 1 ? 's' : ''} ago`
  if (minutes > 0) return `${minutes} minute${minutes > 1 ? 's' : ''} ago`
  return 'Just now'
}

/**
 * Validate URL format
 */
export function isValidUrl(url: string): boolean {
  try {
    new URL(url)
    return true
  } catch {
    return false
  }
}

/**
 * Validate Ethereum address
 */
export function isValidAddress(address: string): boolean {
  return /^0x[a-fA-F0-9]{40}$/.test(address)
}

/**
 * Generate CVSS score color
 */
export function getCvssColor(score: number): string {
  if (score >= 9) return 'text-red-500'
  if (score >= 7) return 'text-orange-500'
  if (score >= 4) return 'text-yellow-500'
  if (score >= 1) return 'text-blue-500'
  return 'text-gray-500'
}

/**
 * Copy text to clipboard
 */
export async function copyToClipboard(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text)
    return true
  } catch {
    // Fallback for older browsers
    const textArea = document.createElement('textarea')
    textArea.value = text
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
    return true
  }
}

/**
 * Generate random ID
 */
export function generateId(): string {
  return Math.random().toString(36).substr(2, 9)
}

/**
 * Debounce function
 */
export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout
  return (...args: Parameters<T>) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => func(...args), wait)
  }
}

/**
 * Sleep utility
 */
export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms))
}

/**
 * Format timestamp to readable date
 */
export function formatDate(timestamp: number): string {
  return new Date(timestamp * 1000).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

/**
 * Truncate text with ellipsis
 */
export function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text
  return text.slice(0, maxLength) + '...'
}

/**
 * Parse tool output file type
 */
export function getToolType(filename: string): string {
  const ext = filename.split('.').pop()?.toLowerCase()
  
  switch (ext) {
    case 'nmap':
    case 'xml':
      return 'nmap'
    case 'nikto':
      return 'nikto'
    case 'burp':
      return 'burp'
    case 'json':
      return 'json'
    default:
      return 'custom'
  }
}

/**
 * Calculate reputation level from score
 */
export function getReputationLevel(score: number): {
  level: number
  name: string
  color: string
  minScore: number
} {
  if (score >= 5000) return { level: 4, name: 'Legendary', color: '#E74C3C', minScore: 5000 }
  if (score >= 1501) return { level: 3, name: 'Elite', color: '#8E44AD', minScore: 1501 }
  if (score >= 501) return { level: 2, name: 'Expert', color: '#F39C12', minScore: 501 }
  if (score >= 101) return { level: 1, name: 'Researcher', color: '#16A085', minScore: 101 }
  return { level: 0, name: 'Novice', color: '#8B9DC3', minScore: 0 }
}'''

with open('dvulndb-prototype/frontend/src/utils/index.ts', 'w') as f:
    f.write(utils_file)

print("Web3 hooks and utility functions created!")