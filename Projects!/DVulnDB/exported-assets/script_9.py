# Create Web3 Provider component
web3_provider = '''\"use client\"

import React, { ReactNode } from 'react'
import { WagmiConfig } from 'wagmi'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import config from '@/config/web3'

const queryClient = new QueryClient()

interface Web3ProviderProps {
  children: ReactNode
}

export default function Web3Provider({ children }: Web3ProviderProps) {
  return (
    <WagmiConfig config={config}>
      <QueryClientProvider client={queryClient}>
        {children}
      </QueryClientProvider>
    </WagmiConfig>
  )
}'''

with open('dvulndb-prototype/frontend/src/components/providers/Web3Provider.tsx', 'w') as f:
    f.write(web3_provider)

# Create Toast Provider
toast_provider = '''\"use client\"

import { Toaster } from 'react-hot-toast'

export default function ToastProvider() {
  return (
    <Toaster
      position="top-right"
      toastOptions={{
        duration: 4000,
        style: {
          background: '#1f2937',
          color: '#f9fafb',
          border: '1px solid #374151',
        },
        success: {
          iconTheme: {
            primary: '#10b981',
            secondary: '#f9fafb',
          },
        },
        error: {
          iconTheme: {
            primary: '#ef4444',
            secondary: '#f9fafb',
          },
        },
      }}
    />
  )
}'''

with open('dvulndb-prototype/frontend/src/components/providers/ToastProvider.tsx', 'w') as f:
    f.write(toast_provider)

# Create main App layout
app_layout = '''import type { Metadata } from 'next'
import { Inter, JetBrains_Mono } from 'next/font/google'
import Web3Provider from '@/components/providers/Web3Provider'
import ToastProvider from '@/components/providers/ToastProvider'
import Header from '@/components/layout/Header'
import Footer from '@/components/layout/Footer'
import './globals.css'

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' })
const jetbrainsMono = JetBrains_Mono({ 
  subsets: ['latin'], 
  variable: '--font-jetbrains' 
})

export const metadata: Metadata = {
  title: 'Decentralized Vulnerability Database',
  description: 'Secure vulnerability disclosure platform with cryptocurrency bounties for ethical hackers and security researchers',
  keywords: ['web3', 'security', 'vulnerability', 'bug bounty', 'blockchain', 'cybersecurity'],
  authors: [{ name: 'Jon - ISSessions' }],
  openGraph: {
    title: 'Decentralized Vulnerability Database',
    description: 'Secure vulnerability disclosure platform with cryptocurrency bounties',
    type: 'website',
    siteName: 'DVulnDB',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Decentralized Vulnerability Database',
    description: 'Secure vulnerability disclosure platform with cryptocurrency bounties',
  },
  viewport: {
    width: 'device-width',
    initialScale: 1,
  },
  robots: {
    index: true,
    follow: true,
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
      <body className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-gray-100 font-sans antialiased">
        <Web3Provider>
          <div className="flex flex-col min-h-screen">
            <Header />
            <main className="flex-1 container mx-auto px-4 py-8">
              {children}
            </main>
            <Footer />
          </div>
          <ToastProvider />
        </Web3Provider>
      </body>
    </html>
  )
}'''

with open('dvulndb-prototype/frontend/src/app/layout.tsx', 'w') as f:
    f.write(app_layout)

# Create global CSS
global_css = '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --font-inter: 'Inter', sans-serif;
  --font-jetbrains: 'JetBrains Mono', monospace;
}

@layer base {
  html {
    font-family: var(--font-inter);
  }
  
  body {
    @apply bg-gray-900 text-gray-100;
  }
  
  code, pre {
    font-family: var(--font-jetbrains);
  }
}

@layer components {
  .btn-primary {
    @apply bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed;
  }
  
  .btn-secondary {
    @apply bg-gray-700 hover:bg-gray-600 text-gray-100 font-medium py-2 px-4 rounded-lg transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed;
  }
  
  .btn-ghost {
    @apply text-gray-300 hover:text-white hover:bg-gray-800 font-medium py-2 px-4 rounded-lg transition-colors duration-200;
  }
  
  .card {
    @apply bg-gray-800 border border-gray-700 rounded-xl p-6 shadow-lg;
  }
  
  .card-hover {
    @apply card hover:border-gray-600 hover:shadow-xl transition-all duration-200 cursor-pointer;
  }
  
  .input-field {
    @apply w-full px-4 py-3 bg-gray-800 border border-gray-600 rounded-lg text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-colors duration-200;
  }
  
  .textarea-field {
    @apply input-field resize-vertical min-h-[120px];
  }
  
  .badge {
    @apply inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium;
  }
  
  .severity-critical {
    @apply bg-red-600 text-red-100;
  }
  
  .severity-high {
    @apply bg-orange-600 text-orange-100;
  }
  
  .severity-medium {
    @apply bg-yellow-600 text-yellow-100;
  }
  
  .severity-low {
    @apply bg-blue-600 text-blue-100;
  }
  
  .severity-info {
    @apply bg-gray-600 text-gray-100;
  }
  
  .status-submitted {
    @apply bg-blue-600 text-blue-100;
  }
  
  .status-validating {
    @apply bg-yellow-600 text-yellow-100;
  }
  
  .status-confirmed {
    @apply bg-green-600 text-green-100;
  }
  
  .status-rejected {
    @apply bg-red-600 text-red-100;
  }
  
  .status-disclosed {
    @apply bg-purple-600 text-purple-100;
  }
  
  .glow-effect {
    @apply shadow-lg shadow-primary-500/25;
  }
  
  .cyber-border {
    @apply border border-primary-500/30 bg-gradient-to-r from-gray-900/50 to-gray-800/50 backdrop-blur-sm;
  }
}

@layer utilities {
  .text-gradient {
    @apply bg-gradient-to-r from-primary-400 to-primary-600 bg-clip-text text-transparent;
  }
  
  .animate-pulse-glow {
    animation: pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
  
  .scrollbar-thin {
    scrollbar-width: thin;
    scrollbar-color: rgb(107 114 128) rgb(31 41 55);
  }
  
  .scrollbar-thin::-webkit-scrollbar {
    width: 6px;
  }
  
  .scrollbar-thin::-webkit-scrollbar-track {
    background: rgb(31 41 55);
  }
  
  .scrollbar-thin::-webkit-scrollbar-thumb {
    background: rgb(107 114 128);
    border-radius: 3px;
  }
  
  .scrollbar-thin::-webkit-scrollbar-thumb:hover {
    background: rgb(156 163 175);
  }
}

/* Custom animations */
@keyframes pulse-glow {
  0%, 100% {
    box-shadow: 0 0 5px rgba(59, 130, 246, 0.5);
  }
  50% {
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.8);
  }
}

/* Loading spinner */
.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #374151;
  border-top: 4px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Code highlighting */
.hljs {
  background: #1f2937 !important;
  color: #f9fafb !important;
}

/* Wallet modal overrides */
w3m-modal {
  --w3m-color-mix: #1f2937;
  --w3m-accent: #3b82f6;
}'''

with open('dvulndb-prototype/frontend/src/app/globals.css', 'w') as f:
    f.write(global_css)

print("Layout components and styles created!")