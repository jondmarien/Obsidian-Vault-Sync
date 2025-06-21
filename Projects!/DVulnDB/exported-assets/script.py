# Create the main project structure
import os
import json

# Create directory structure
directories = [
    'dvulndb-prototype',
    'dvulndb-prototype/contracts',
    'dvulndb-prototype/contracts/interfaces',
    'dvulndb-prototype/frontend',
    'dvulndb-prototype/frontend/src',
    'dvulndb-prototype/frontend/src/components',
    'dvulndb-prototype/frontend/src/components/layout',
    'dvulndb-prototype/frontend/src/components/vulnerability',
    'dvulndb-prototype/frontend/src/hooks',
    'dvulndb-prototype/frontend/src/utils',
    'dvulndb-prototype/frontend/src/config',
    'dvulndb-prototype/frontend/src/types',
    'dvulndb-prototype/scripts',
    'dvulndb-prototype/test',
    'dvulndb-prototype/docs'
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

print("Project structure created successfully!")

# Create package.json for the main project
package_json = {
    "name": "decentralized-vulnerability-database",
    "version": "1.0.0",
    "description": "A decentralized vulnerability disclosure platform with bounty rewards",
    "main": "index.js",
    "scripts": {
        "compile": "hardhat compile",
        "test": "hardhat test",
        "deploy:localhost": "hardhat run scripts/deploy.js --network localhost",
        "deploy:sepolia": "hardhat run scripts/deploy.js --network sepolia",
        "verify": "hardhat verify --network sepolia",
        "frontend:dev": "cd frontend && npm run dev",
        "frontend:build": "cd frontend && npm run build",
        "node": "hardhat node"
    },
    "keywords": ["web3", "vulnerability", "security", "blockchain", "bug-bounty"],
    "author": "Jon - ISSessions",
    "license": "MIT",
    "devDependencies": {
        "@nomicfoundation/hardhat-toolbox": "^4.0.0",
        "@nomicfoundation/hardhat-verify": "^2.0.0",
        "@openzeppelin/contracts": "^5.0.0",
        "hardhat": "^2.19.0",
        "hardhat-deploy": "^0.11.45",
        "dotenv": "^16.3.1",
        "chai": "^4.3.10",
        "mocha": "^10.2.0"
    },
    "dependencies": {
        "ethers": "^6.8.1",
        "ipfs-http-client": "^60.0.1"
    }
}

with open('dvulndb-prototype/package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("Root package.json created!")