---
title: Launchscripts README
author:
  - Jon Marien
created: 2025-05-02
published: 2025-05-02
tags:
  - judgeflow
---

| Title                | Author                       | Created      | Published    | Tags                       |
| -------------------- | ---------------------------- | ------------ | ------------ | -------------------------- |
| Launchscripts README | <ul><li>Jon Marien</li></ul> | May 02, 2025 | May 02, 2025 | [[#judgeflow\|#judgeflow]] |

# JudgeFlow Cross-Platform Launch Scripts

This project provides platform-specific Warp terminal configurations and cross-platform launch scripts for the JudgeFlow development environment. It resolves issues with environment variable substitution in Warp terminal configurations, particularly focusing on the `${HOME}` variable which doesn't function correctly on Windows systems.

## Problem Solved

When using Warp terminal's launch configurations with paths that include environment variables like `${HOME}`, Windows users often encounter errors. This happens because:

1. The `${HOME}` environment variable is primarily used in Unix-like systems and may not be properly set in Windows environments
2. Windows uses different path separator characters (`\` vs `/`)
3. Windows typically uses `%USERPROFILE%` or `$env:USERPROFILE` for the user's home directory path instead of `${HOME}`

This project offers a solution by:

- Creating separate platform-specific YAML configuration files
- Using the appropriate environment variables for each platform (`${USERPROFILE}` for Windows, `${HOME}` for Linux)
- Providing cross-platform launch scripts that detect the OS and use the correct configuration

## Files

### YAML Configuration Files

| File                                | Description                                           |
| ----------------------------------- | ----------------------------------------------------- |
| `judgeflow_local_dev_template.yaml` | The original template file (kept for reference)       |
| `judgeflow_local_dev_windows.yaml`  | Windows-specific configuration using `${USERPROFILE}` |
| `judgeflow_local_dev_linux.yaml`    | Linux-specific configuration using `${HOME}`          |

### Launch Scripts

| File                                  | Description                                                            |
| ------------------------------------- | ---------------------------------------------------------------------- |
| `launch-judgeflow-cross-platform.ps1` | PowerShell script that detects OS and launches with appropriate config |
| `launch-judgeflow-cross-platform.sh`  | Bash script that detects OS and launches with appropriate config       |
| `launch-judgeflow.bat`                | Windows batch file wrapper for easy execution on Windows               |
| `launch-judgeflow`                    | Universal script that works on both Windows and Unix-like systems      |

## Installation

### Prerequisites

- [Warp Terminal](https://www.warp.dev/) installed on your system
- For Windows: PowerShell 5.1+ or PowerShell Core 7.0+
- For Linux: Bash shell

### Setup

1. Clone or download these scripts to your JudgeFlow project's launch scripts directory
2. Ensure the shell scripts have executable permissions on Linux/macOS:

   ```bash

   chmod +x launch-judgeflow-cross-platform.sh launch-judgeflow

   ```

## Usage

### Quick Start

The simplest way to launch JudgeFlow is to use the universal script:

```

# On Windows (Command Prompt or PowerShell)

launch-judgeflow

  

# On Linux/macOS

./launch-judgeflow

```

This script will detect your operating system and use the appropriate configuration.

### Platform-Specific Launch

#### Windows Users

You have several options:
1. Using the batch file:
   ```

   launch-judgeflow.bat

   ```

2. Using PowerShell directly:
   ```powershell

   .\launch-judgeflow-cross-platform.ps1

   ```

3. Specifying a configuration type:
   ```powershell

   .\launch-judgeflow-cross-platform.ps1 -ConfigType windows

   ```

![[image-267.png]]
#### Linux/macOS Users

1. Using the shell script:
   ```bash

   ./launch-judgeflow-cross-platform.sh

   ```

2. Specifying a configuration type:
   ```bash

   ./launch-judgeflow-cross-platform.sh --config linux

   ```

### Command-Line Arguments

All scripts support these arguments:

#### PowerShell Script Arguments

| Argument      | Description                                                    |
| ------------- | -------------------------------------------------------------- |
| `-ConfigType` | Specify which config to use: 'windows', 'linux', or 'template' |
| `-WarpPath`   | Override the default path to the Warp executable               |
| `-ConfigPath` | Override the default path to the configuration files           |

#### Shell Script Arguments

| Argument | Description |
|----------|-------------|

| `-c, --config TYPE` | Specify config type: windows, linux, or template |
| `-w, --warp-path PATH` | Specify path to Warp executable |
| `-p, --config-path PATH` | Specify path to configuration file |
| `-h, --help` | Show help message |

## Customization

### Adding New Tabs

To add a new tab to your development environment:
1. Edit the appropriate YAML file(s) for your platform(s)
2. Add a new tab entry under the `tabs` section, following this structure:
```yaml

- title: new-tab-name

  layout:

    cwd: "${USERPROFILE}\Path\To\Directory"  # for Windows

    # or

    cwd: "${HOME}/Path/To/Directory"  # for Linux

    is_focused: true

    commands:

      - exec: "your-command-here"

  color: purple  # Choose: red, green, blue, yellow, purple, cyan, etc.

```

### Changing Project Paths

If your JudgeFlow project is located in a different directory, you'll need to modify:

1. The path values in both YAML configuration files:
   - `judgeflow_local_dev_windows.yaml`: Update paths that start with `${USERPROFILE}\Projects\judgeflow\`
   - `judgeflow_local_dev_linux.yaml`: Update paths that start with `${HOME}/Projects/judgeflow/`

1. Example for different project locations:
   - Windows: `${USERPROFILE}\Development\MyApps\judgeflow\`
   - Linux: `${HOME}/dev/judgeflow/`

### Using Environment Variables for Project Path

For even more flexibility, you can set a custom environment variable:

1. Define a `JUDGEFLOW_DIR` environment variable on your system pointing to your project root
2. Then modify the YAML files to use this variable:
   ```yaml

   cwd: "${JUDGEFLOW_DIR}/backend"  # Works on both Windows and Linux

   ```

## Troubleshooting

### Common Issues

| Issue                                  | Solution                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| "Warp executable not found"            | Ensure Warp is installed and in a standard location, or specify path with `-WarpPath`      |
| "Configuration file not found"         | Check that you're running the script from the correct directory                            |
| Windows path errors                    | Ensure paths in the Windows YAML use backslashes (`\`) or properly escaped forward slashes |
| Linux path errors                      | Ensure paths in the Linux YAML use forward slashes (`/`)                                   |
| Script permission denied (Linux)       | Run `chmod +x launch-judgeflow launch-judgeflow-cross-platform.sh`                         |
| "Could not determine operating system" | Manually specify the config with `-ConfigType` or `--config`                               |

### Platform-Specific Issues

#### Windows

- If PowerShell script execution is disabled, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

- If the WSL path is not found, check that WSL is installed with: `wsl --status`

#### Linux

- If the script doesn't execute properly with `./launch-judgeflow`, try running it with an explicit interpreter: `bash ./launch-judgeflow`

- If GeckoDriver is not found, ensure it's installed and in the PATH

## Notes for Developers

- The YAML files are processed by Warp Terminal directly and should be placed in the appropriate Warp configuration directory for permanent installation.

- Windows: `%APPDATA%\warp\launch_configurations\`

- Linux/macOS: `~/.warp/launch_configurations/`

## License

This project is for internal use within the JudgeFlow development team and is not subject to external licensing.