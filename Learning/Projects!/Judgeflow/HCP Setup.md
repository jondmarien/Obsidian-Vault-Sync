---
title: HCP Setup
author:
  - Jon Marien
created: 2025-05-08
published: 2025-05-08
tags:
  - projects
  - judgeflow
---

| Title     | Author                       | Created      | Published    | Tags                                                 |
| --------- | ---------------------------- | ------------ | ------------ | ---------------------------------------------------- |
| HCP Setup | <ul><li>Jon Marien</li></ul> | May 08, 2025 | May 08, 2025 | [[#projects\|#projects]], [[#judgeflow\|#judgeflow]] |
# Judgeflow Backend – HCP Vault Secrets Setup & Usage

## Prerequisites
- [Rust](https://www.rust-lang.org/tools/install) and Cargo
- [Make](https://www.gnu.org/software/make/) (Windows users: install via Chocolatey or use GNUWin32)
- HashiCorp Cloud Platform (HCP) account and access to your project
- HCP Vault Secrets app(s) and credentials (client ID/secret)

---

## 1. Windows Setup

### 1.1 Install HCP CLI
- Download the latest Windows release from the [HCP CLI Releases](https://releases.hashicorp.com/hcp/)
- Extract the `hcp.exe` to a folder (e.g., `C:\tools\hcp`)

### 1.2 Add HCP CLI to PATH
- Open Start Menu, search for "Environment Variables", and open "Edit the system environment variables"
- Click "Environment Variables..."
- Under "System variables", find and select `Path`, then click "Edit..."
- Click "New" and add the path to your `hcp.exe` folder (e.g., `C:\tools\hcp`)
- Click OK to save and close all dialogs
- Open a new Command Prompt or PowerShell and verify:

```sh
  hcp --version
```

### 1.3 Authenticate with HCP
- Run:

```sh
  hcp auth login
```

- Follow the prompt to authenticate via browser or paste your credentials

### 1.4 Initialize HCP Profile, Choose Project, and Configure Secrets
- Run the following command to interactively select your organization, project, and Vault Secrets app:

```sh
  hcp profile init
```

- Follow the prompts to:
  - Select your organization
  - Select your project
  - Choose **yes** to configure Vault Secrets
  - Select the Vault Secrets app (e.g., `judgeflow-dev` or `judgeflow-prod`)
- This will set up your CLI context for all future commands.
### 1.5 Choose the Vault Secrets App (optional, if needed; if not, skip to 1.6)
- List available apps:

```sh
  hcp vault-secrets app list # OR hcp vs app list
```

- Set the app for your session:

```sh
  hcp profile set vault-secrets/app <your-app-name>
```

(e.g., `judgeflow-dev` or `judgeflow-prod`)

### 1.6 Run the Project Using Makefile
- Build:

```sh
  make build
  # or specify app/binary
  make build HCP_APP_DEV=your-app APP=your-binary
```

- Run:

```sh
  make run
  # or specify app/binary
  make run HCP_APP_DEV=your-app APP=your-binary
```

- Release (production):

```sh
  make release
  # or specify prod app
  make release HCP_APP_PROD=your-prod-app
```

---

## 2. Linux Setup

### 2.1 Install HCP CLI
Install the required packages:

```sh
sudo apt-get update && \
  sudo apt-get install wget gpg coreutils
```

Add the HashiCorp GPG key:

```sh
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
```

Add the official HashiCorp Linux repository:

```sh
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
```

Update and install HCP CLI:

```sh
sudo apt-get update && sudo apt-get install hcp
```

Verify installation:

```sh
hcp --version
```

### 2.2 Authenticate, Initialize Profile, and Use Makefile
- Use the same steps as in the Windows section for:
  - Authenticating with HCP (`hcp login`)
  - Initializing your profile and selecting your organization/project/app (`hcp profile init`)
  - Optionally setting the app (`hcp profile set vault-secrets/app <your-app-name>`)
  - Running the Makefile build scripts

---

## 3. MacOSX Setup

### 3.1 Install HCP CLI
- Install the HashiCorp tap, a repository of all of the HashiCorp Homebrew packages:

```sh
brew tap hashicorp/tap
```

- Install hcp with hashicorp/tap/hcp:

```sh
brew install hashicorp/tap/hcp
```

- Upgrade to the latest version (optional):

```sh
brew upgrade hashicorp/tap/hcp
```

- Verify installation:

```sh
hcp --version
```

### 3.2 Authenticate, Initialize Profile, and Use Makefile
- Use the same steps as in the Linux section for:
  - Authenticating with HCP (`hcp auth login`)
  - Initializing your profile and selecting your organization/project/app (`hcp profile init`)
  - Optionally setting the app (`hcp profile set vault-secrets/app <your-app-name>`)
  - Running the Makefile build scripts

---

## Troubleshooting

- **`hcp` not found:** Ensure it is in your PATH and you opened a new terminal after editing environment variables.
- **Authentication issues:** Run `hcp auth login` again and ensure your credentials are correct.
- **Secrets not injected:** Make sure you selected the correct app with `hcp profile set vault-secrets/app <app-name>`.
- **Makefile errors:** Ensure you have GNU Make installed and are running commands from the `backend/` directory.
- **Permission denied (Linux):** Try `sudo` or check file permissions on the `hcp` binary.
- **For more help:** See the [HCP CLI docs](https://developer.hashicorp.com/hcp/docs/hcp-vault-secrets/cli) or open an issue in this repo.
