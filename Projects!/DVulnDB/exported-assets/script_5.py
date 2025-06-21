# Create missing directories first
import os

missing_dirs = [
    'dvulndb-prototype/deploy',
    'dvulndb-prototype/utils'
]

for directory in missing_dirs:
    os.makedirs(directory, exist_ok=True)

print("Missing directories created!")

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