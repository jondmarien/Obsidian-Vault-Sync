# Create frontend package.json
frontend_package_json = {
    "name": "dvulndb-frontend",
    "version": "0.1.0",
    "private": True,
    "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "next lint",
        "type-check": "tsc --noEmit"
    },
    "dependencies": {
        "next": "^14.0.4",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "@web3modal/wagmi": "^3.5.0",
        "@web3modal/siwe": "^3.5.0", 
        "wagmi": "^1.4.10",
        "viem": "^1.19.0",
        "@tanstack/react-query": "^4.36.1",
        "ethers": "^6.8.1",
        "ipfs-http-client": "^60.0.1",
        "react-hook-form": "^7.47.0",
        "react-hot-toast": "^2.4.1",
        "react-markdown": "^9.0.1",
        "react-syntax-highlighter": "^15.5.0",
        "lucide-react": "^0.294.0",
        "clsx": "^2.0.0",
        "tailwind-merge": "^2.0.0",
        "class-variance-authority": "^0.7.0",
        "@radix-ui/react-dialog": "^1.0.5",
        "@radix-ui/react-tabs": "^1.0.4",
        "@radix-ui/react-toast": "^1.1.5",
        "@radix-ui/react-select": "^2.0.0",
        "@radix-ui/react-progress": "^1.0.3",
        "framer-motion": "^10.16.5"
    },
    "devDependencies": {
        "typescript": "^5.2.2",
        "@types/node": "^20.8.10",
        "@types/react": "^18.2.37",
        "@types/react-dom": "^18.2.15",
        "@types/react-syntax-highlighter": "^15.5.9",
        "eslint": "^8.53.0",
        "eslint-config-next": "^14.0.4",
        "tailwindcss": "^3.3.5",
        "autoprefixer": "^10.4.16",
        "postcss": "^8.4.31"
    }
}

import json
with open('dvulndb-prototype/frontend/package.json', 'w') as f:
    json.dump(frontend_package_json, f, indent=2)

# Create Next.js config
nextjs_config = '''/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['ipfs.io', 'gateway.pinata.cloud'],
  },
  webpack: (config) => {
    config.resolve.fallback = {
      fs: false,
      net: false,
      tls: false,
    };
    return config;
  },
  experimental: {
    appDir: true,
  },
};

module.exports = nextConfig;'''

with open('dvulndb-prototype/frontend/next.config.js', 'w') as f:
    f.write(nextjs_config)

# Create Tailwind config
tailwind_config = '''/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
        secondary: {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
        },
        success: '#10b981',
        warning: '#f59e0b',
        error: '#ef4444',
        critical: '#dc2626',
        high: '#ea580c',
        medium: '#d97706',
        low: '#65a30d',
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'Consolas', 'Monaco', 'monospace'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'pulse-glow': 'pulseGlow 2s infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        pulseGlow: {
          '0%, 100%': { boxShadow: '0 0 5px rgba(59, 130, 246, 0.5)' },
          '50%': { boxShadow: '0 0 20px rgba(59, 130, 246, 0.8)' },
        },
      },
    },
  },
  plugins: [],
}'''

with open('dvulndb-prototype/frontend/tailwind.config.js', 'w') as f:
    f.write(tailwind_config)

# Create PostCSS config
postcss_config = '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}'''

with open('dvulndb-prototype/frontend/postcss.config.js', 'w') as f:
    f.write(postcss_config)

print("Frontend configuration files created!")