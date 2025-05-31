---
title: New Backend README
author:
  - Jon Marien
created: 2025-05-02
published: 2025-05-02
tags:
  - judgeflow
---

| Title              | Author                       | Created      | Published    | Tags                       |
| ------------------ | ---------------------------- | ------------ | ------------ | -------------------------- |
| New Backend README | <ul><li>Jon Marien</li></ul> | May 02, 2025 | May 02, 2025 | [[#judgeflow\|#judgeflow]] |

# Judgeflow Backend (Rust) – Judging Platform

This judgeflow_backend is written in Rust and is designed to:

- Process CSV data (with `csv` and `polars`)
- Interface with Supabase (via PostgREST and SQLx)
- Integrate with the Perplexity Sonar API for advanced AI Q&A
- Use environment variables for configuration (dotenv support)

## Features
- **CSV/Data Processing:** Use `csv` for simple CSV, or `polars` for advanced DataFrame operations.

- **Supabase Integration:**
  - Use `sqlx` for direct Postgres queries (recommended for transactional logic).
  - Use `postgrest` for RESTful access to Supabase tables (leverages Supabase RLS/policies).

- **Perplexity Sonar API:**
  - Call the Sonar API for real-time, web-wide research and Q&A.
  - See [`src/sonar_pplx.rs`](./src/sonar_pplx.rs) for a minimal async integration example.

- **Environment Variables:**
  - Use a `.env` file for local development (see below for required keys).

## Getting Started

### 1. Prerequisites

- [Rust](https://www.rust-lang.org/tools/install)
- [Cargo](https://doc.rust-lang.org/cargo/)

### 2. Browser Automation (Geckodriver) Setup
Some features (such as Devpost profile scraping or browser automation) require [geckodriver](https://github.com/mozilla/geckodriver) and [Firefox](https://www.mozilla.org/en-US/firefox/new/) to be installed and available on your system PATH.

#### Windows Setup Instructions
1. **Download Geckodriver:**
   - Go to the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases) and download the latest `geckodriver-vX.Y.Z-win64.zip` for Windows 64-bit.
2. **Extract the ZIP:**
   - Extract `geckodriver.exe` to a folder of your choice, e.g., `C:\tools\geckodriver`.
3. **Add to System PATH:**
   - Open Start Menu, search for "Environment Variables", and open "Edit the system environment variables".
   - Click "Environment Variables...".
   - Under "System variables", find and select `Path`, then click "Edit...".
   - Click "New" and add the path to your `geckodriver.exe` folder (e.g., `C:\tools\geckodriver`).
   - Click OK to save and close all dialogs.
4. **Verify Installation:**
   - Open a new Command Prompt or PowerShell window and run:
     ```sh

     geckodriver --port 4444

     ```

   - You should see output indicating that geckodriver is listening on port 4444. Press Ctrl+C to stop it.

> **Note:** You must also have Firefox installed. The backend expects `geckodriver` to be callable from any directory.

If you encounter issues, ensure you extracted the correct version (64-bit), and that you opened a new terminal after updating your PATH.

#### Linux Setup Instructions

1. **Install via Package Manager (Recommended):**
   - For Ubuntu/Debian:
     ```sh

     sudo apt update

     sudo apt install firefox-geckodriver

     ```

   - For Fedora:
     ```sh

     sudo dnf install geckodriver

     ```

   - For Arch:
     ```sh

     sudo pacman -S geckodriver

     ```

2. **Manual Download:**
   - Download the latest release from the [geckodriver releases page](https://github.com/mozilla/geckodriver/releases) (`geckodriver-vX.Y.Z-linux64.tar.gz`).
   - Extract the tarball and move `geckodriver` to a directory in your PATH (e.g., `/usr/local/bin`).
     
     ```sh

     tar -xzf geckodriver-*-linux64.tar.gz

     sudo mv geckodriver /usr/local/bin/

     ```

3. **Verify Installation:**
   - Run:
     ```sh

     geckodriver --port 4444

     ```

   - You should see output indicating that geckodriver is listening on port 4444. Press Ctrl+C to stop it.

> **Note:** You must also have Firefox installed. The backend expects `geckodriver` to be callable from any directory.

---

### 2. Setup
Clone the repo and enter the judgeflow_backend directory:
```sh

cd backend

```

Install dependencies (if needed):
```sh

cargo build

```

### 3. Environment Variables
Create a `.env` file in the `backend/` directory:
```env

SONAR_PPLX_API_KEY=your-perplexity-api-key-here

SUPABASE_URL=https://your-project.supabase.co/rest/v1/

SUPABASE_API_KEY=your-supabase-api-key-here

```

### 4. Running the Backend
Run the main entry point (Sonar API example):
```sh

cargo run

```

To run a different example (e.g., Supabase), change the entry point in `src/main.rs` or create a separate binary.

## Project Structure

```sh

backend/

├── src/

│   ├── main.rs              # Main entry point
│   ├── hello_world.rs       # Simple hello world example
│   ├── constants.rs         # Environment variable keys
│   ├── lib.rs               # Library root
│   ├── models/              # Data models (devpost, discord, import, resources, sync, webhook, waitlist)
│   ├── routes/              # API route handlers (devpost, discord, import, resource, sync, waitlist, webhook)
│   ├── services/            # Service logic (devpost, discord, import, resource, sync, waitlist, webhook)
│   ├── utils/               # Utilities (apify_sherlock, csv_processing, sonar_pplx, supabase_example)
│   └── middleware/          # Middleware (auth)
├── data/                    # CSV and output data files
│   ├── registrants-data.csv
│   ├── projects-info.csv
│   ├── projects-info-fixed.csv
│   ├── projects-info-cleaned.csv
│   ├── country-breakdown.csv
│   └── output/              # Output subdirectory
├── certs/                   # Certificates
├── scripts/                 # Utility scripts (backfill_clerk_to_supabase.rs, fix_csv.rs)
├── tests/                   # Test suite (test_apify_sherlock.rs)
├── Cargo.toml               # Rust dependencies
├── Cargo.lock               # Cargo lockfile
├── .env                     # Environment variables (not committed)
├── .env.example             # Example environment file
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── devpost_debug.html
├── uuid_line.txt
└── README.md                # This current file

```

## Key Dependencies

- [`axum`](https://crates.io/crates/axum) – Web framework
- [`tokio`](https://crates.io/crates/tokio) – Async runtime
- [`dotenv`](https://crates.io/crates/dotenv) – Environment variable loading
- [`serde`](https://crates.io/crates/serde), [`serde_json`](https://crates.io/crates/serde_json) – Serialization
- [`csv`](https://crates.io/crates/csv), [`polars`](https://crates.io/crates/polars), [`prettytable-rs`](https://crates.io/crates/prettytable-rs) – Data processing
- [`sqlx`](https://crates.io/crates/sqlx), [`postgrest`](https://crates.io/crates/postgrest) – Database/PostgREST
- [`reqwest`](https://crates.io/crates/reqwest) – HTTP client
- [`fantoccini`](https://crates.io/crates/fantoccini) – Headless browser automation (WebDriver)
- [`validator`](https://crates.io/crates/validator), [`validator_derive`](https://crates.io/crates/validator_derive) – Data validation
- [`clerk`](https://crates.io/crates/clerk), [`jsonwebtoken`](https://crates.io/crates/jsonwebtoken), [`jwks-client`](https://crates.io/crates/jwks-client) – Auth
- [tower, tower-http](https://crates.io/crates/tower-http) – Middleware
- [`tracing`](https://crates.io/crates/tracing) – Logging
- [`uuid`](https://crates.io/crates/uuid) – UUIDs
- [`scraper`](https://crates.io/crates/scraper) – HTML parsing
- [`futures-util`](https://crates.io/crates/futures-util), [`tokio-stream`](https://crates.io/crates/tokio-stream) – Async utilities
- [`chrono`](https://crates.io/crates/chrono) – Date/time

## Security

- **Never commit your `.env` file or secrets to version control!**
- The `.env` file is already included in `.gitignore`.

## License

Figure out license we want to use // TODO: MIT ?

## Contact

For questions or contributions, please open an issue or pull request.