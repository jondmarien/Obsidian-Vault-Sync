# Create Hardhat configuration
hardhat_config = '''require("@nomicfoundation/hardhat-toolbox");
require("@nomicfoundation/hardhat-verify");
require("hardhat-deploy");
require("dotenv").config();

const SEPOLIA_RPC_URL = process.env.SEPOLIA_RPC_URL || "https://eth-sepolia.g.alchemy.com/v2/YOUR-API-KEY";
const PRIVATE_KEY = process.env.PRIVATE_KEY || "0x0000000000000000000000000000000000000000000000000000000000000000";
const ETHERSCAN_API_KEY = process.env.ETHERSCAN_API_KEY || "api-key";

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  },
  
  networks: {
    hardhat: {
      chainId: 31337,
      blockConfirmations: 1,
    },
    localhost: {
      chainId: 31337,
    },
    sepolia: {
      url: SEPOLIA_RPC_URL,
      accounts: PRIVATE_KEY !== "0x0000000000000000000000000000000000000000000000000000000000000000" ? [PRIVATE_KEY] : [],
      chainId: 11155111,
      blockConfirmations: 6,
    },
  },
  
  namedAccounts: {
    deployer: {
      default: 0,
    },
    validator1: {
      default: 1,
    },
    validator2: {
      default: 2,
    },
  },
  
  etherscan: {
    apiKey: {
      sepolia: ETHERSCAN_API_KEY,
    },
  },
  
  gasReporter: {
    enabled: process.env.REPORT_GAS === "true",
    currency: "USD",
    outputFile: "gas-report.txt",
    noColors: true,
  },
  
  mocha: {
    timeout: 300000, // 300 seconds max for running tests
  },
};'''

with open('dvulndb-prototype/hardhat.config.js', 'w') as f:
    f.write(hardhat_config)

# Create .env.example
env_example = '''# Blockchain Network Configuration
SEPOLIA_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR-API-KEY
PRIVATE_KEY=0x1234567890abcdef... # Your private key (DO NOT SHARE!)
ETHERSCAN_API_KEY=YOUR-ETHERSCAN-API-KEY

# Frontend Configuration
NEXT_PUBLIC_WALLETCONNECT_PROJECT_ID=your-walletconnect-project-id
NEXT_PUBLIC_ALCHEMY_API_KEY=your-alchemy-api-key
NEXT_PUBLIC_CONTRACT_REGISTRY_ADDRESS=
NEXT_PUBLIC_CONTRACT_ESCROW_ADDRESS=
NEXT_PUBLIC_CONTRACT_REPUTATION_ADDRESS=

# IPFS Configuration  
INFURA_IPFS_PROJECT_ID=your-infura-ipfs-project-id
INFURA_IPFS_PROJECT_SECRET=your-infura-ipfs-secret

# Development
REPORT_GAS=true
NODE_ENV=development'''

with open('dvulndb-prototype/.env.example', 'w') as f:
    f.write(env_example)

print("Hardhat configuration created!")

# Create deployment script
deploy_script = '''const { network } = require("hardhat");
const { verify } = require("../utils/verify");

module.exports = async ({ getNamedAccounts, deployments }) => {
  const { deploy, log, get } = deployments;
  const { deployer, validator1, validator2 } = await getNamedAccounts();
  
  const chainId = network.config.chainId;
  const isDevelopment = chainId === 31337;
  
  log("===============================================");
  log("Deploying Decentralized Vulnerability Database");
  log("===============================================");
  log(`Network: ${network.name} (${chainId})`);
  log(`Deployer: ${deployer}`);
  
  // Deploy BountyEscrow first
  log("\\n1. Deploying BountyEscrow...");
  const bountyEscrow = await deploy("BountyEscrow", {
    from: deployer,
    args: [],
    log: true,
    waitConfirmations: isDevelopment ? 1 : 6,
  });
  
  // Deploy ReputationNFT
  log("\\n2. Deploying ReputationNFT...");
  const reputationNFT = await deploy("ReputationNFT", {
    from: deployer,
    args: [],
    log: true,
    waitConfirmations: isDevelopment ? 1 : 6,
  });
  
  // Deploy VulnerabilityRegistry
  log("\\n3. Deploying VulnerabilityRegistry...");
  const vulnerabilityRegistry = await deploy("VulnerabilityRegistry", {
    from: deployer,
    args: [],
    log: true,
    waitConfirmations: isDevelopment ? 1 : 6,
  });
  
  // Setup contract connections
  log("\\n4. Setting up contract connections...");
  const escrowContract = await ethers.getContractAt("BountyEscrow", bountyEscrow.address);
  const registryContract = await ethers.getContractAt("VulnerabilityRegistry", vulnerabilityRegistry.address);
  const nftContract = await ethers.getContractAt("ReputationNFT", reputationNFT.address);
  
  // Set registry address in escrow
  await escrowContract.setVulnerabilityRegistry(vulnerabilityRegistry.address);
  log(`✓ Escrow registry set to: ${vulnerabilityRegistry.address}`);
  
  // Set escrow address in registry
  await registryContract.setBountyEscrow(bountyEscrow.address);
  log(`✓ Registry escrow set to: ${bountyEscrow.address}`);
  
  // Set registry address in NFT contract
  await nftContract.setVulnerabilityRegistry(vulnerabilityRegistry.address);
  log(`✓ NFT registry set to: ${vulnerabilityRegistry.address}`);
  
  // Add validators
  if (!isDevelopment && validator1 && validator2) {
    await registryContract.addValidator(validator1);
    await registryContract.addValidator(validator2);
    log(`✓ Added validators: ${validator1}, ${validator2}`);
    
    await escrowContract.addApprover(validator1);
    await escrowContract.addApprover(validator2);
    log(`✓ Added escrow approvers: ${validator1}, ${validator2}`);
  }
  
  // Verify contracts on Etherscan
  if (!isDevelopment) {
    log("\\n5. Verifying contracts...");
    await verify(bountyEscrow.address, []);
    await verify(reputationNFT.address, []);
    await verify(vulnerabilityRegistry.address, []);
  }
  
  log("\\n===============================================");
  log("✅ Deployment completed successfully!");
  log("===============================================");
  log(`VulnerabilityRegistry: ${vulnerabilityRegistry.address}`);
  log(`BountyEscrow: ${bountyEscrow.address}`);
  log(`ReputationNFT: ${reputationNFT.address}`);
  log("===============================================");
  
  // Save deployment info
  const deploymentInfo = {
    network: network.name,
    chainId: chainId,
    timestamp: new Date().toISOString(),
    contracts: {
      VulnerabilityRegistry: vulnerabilityRegistry.address,
      BountyEscrow: bountyEscrow.address,
      ReputationNFT: reputationNFT.address
    },
    deployer: deployer,
    blockNumbers: {
      VulnerabilityRegistry: vulnerabilityRegistry.receipt?.blockNumber,
      BountyEscrow: bountyEscrow.receipt?.blockNumber,
      ReputationNFT: reputationNFT.receipt?.blockNumber
    }
  };
  
  const fs = require("fs");
  const path = require("path");
  const deploymentPath = path.join(__dirname, "../frontend/src/config/deployments.json");
  
  try {
    fs.writeFileSync(deploymentPath, JSON.stringify(deploymentInfo, null, 2));
    log(`\\n📄 Deployment info saved to: ${deploymentPath}`);
  } catch (error) {
    log(`⚠️  Could not save deployment info: ${error.message}`);
  }
};

module.exports.tags = ["all", "vulnerability-db"];'''

with open('dvulndb-prototype/deploy/01-deploy-vulnerability-db.js', 'w') as f:
    f.write(deploy_script)

# Create verification utility
verify_util = '''const { run } = require("hardhat");

const verify = async (contractAddress, args) => {
  console.log("Verifying contract...");
  try {
    await run("verify:verify", {
      address: contractAddress,
      constructorArguments: args,
    });
  } catch (e) {
    if (e.message.toLowerCase().includes("already verified")) {
      console.log("Already verified!");
    } else {
      console.log(e);
    }
  }
};

module.exports = { verify };'''

with open('dvulndb-prototype/utils/verify.js', 'w') as f:
    f.write(verify_util)

print("Deployment scripts created!")