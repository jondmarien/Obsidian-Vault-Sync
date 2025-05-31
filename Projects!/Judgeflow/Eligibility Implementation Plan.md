---
title: Eligibility Implementation Plan
author:
  - Jon Marien
created: 2025-05-13
published: 2025-05-13
tags:
  - projects
  - judgeflow
---

| Title                           | Author                       | Created      | Published    | Tags                                                 |
| ------------------------------- | ---------------------------- | ------------ | ------------ | ---------------------------------------------------- |
| Eligibility Implementation Plan | <ul><li>Jon Marien</li></ul> | May 13, 2025 | May 13, 2025 | [[#projects\|#projects]], [[#judgeflow\|#judgeflow]] |

# Automated Eligibility Checks Integration

## 1. Scope and Goals

- **Goal:** Automate eligibility screening for hackathon submissions using Perplexity AI’s API, with structured outputs and modular code.
- **Focus:** Only eligibility checks (geography, age, employment, previous wins, affiliations).
- **Data Sources:**  
  - **Production:** Pull from Supabase.  
  - **Local Testing:** Use CSV files in `backend/data`, leveraging custom CSV processing/normalization utilities in `backend/src/utils/csv_processing`.

---

## 2. Project Structure & File Responsibilities

**Following the Developer Guide and your conventions:**

- `backend/src/models/eligibility.rs`  
  - Data models for eligibility input & output (structs, enums).
- `backend/src/services/eligibility_service.rs`  
  - Core logic for eligibility checking, orchestrates calls to utils and Perplexity API.
- `backend/src/routes/eligibility_routes.rs`  
  - API endpoints for eligibility checking (accepts requests, returns results).
- `backend/src/utils/sonar_pplx.rs`  
  - Utility functions for interacting with Perplexity API (prompt construction, sending requests, parsing responses).
- `backend/src/utils/csv_processing/`  
  - Utilities for reading, normalizing, and validating CSV data for local testing.
- `backend/data/`  
  - Sample/test CSV files for local runs.
- **Output:**  
  - Write results as both a JSON object (for API return) and a JSON file (for auditing/future-proofing).

---

## 3. Data Flow

### A. Local Testing

1. **CSV Input:**  
   - Read participant/project data from CSV in `backend/data` using custom utilities.
   - Normalize and validate data.
2. **Eligibility Check:**  
   - Pass normalized data to the eligibility service.
   - Service calls Perplexity API via `sonar_pplx.rs` for each criterion.
   - Aggregate responses into a result object.
3. **Output:**  
   - Return JSON object and write to a JSON file in a designated output directory.

### B. Production

1. **Supabase Input:**  
   - Fetch submission data from Supabase.
   - Normalize/validate as needed.
2. **Eligibility Check:**  
   - Same as above.
3. **Output:**  
   - Return JSON object via API.

---

## 4. Eligibility Criteria (Configurable)

- **Geography:** Allowed/disallowed countries/regions.
- **Age:** Minimum/maximum age.
- **Employment/Affiliation:** Disallowed companies/organizations.
- **Previous Wins:** Flag if participant is a previous winner.
- **Affiliations:** Check for connections to sponsors, organizers, etc.

---

## 5. Core Components & Responsibilities

### A. Models (`models/eligibility.rs`)

- `EligibilityCheckInput`: Struct for normalized input data.
- `EligibilityCriterionResult`: Per-criterion result struct (status, explanation, evidence).
- `EligibilityCheckResult`: Aggregated result struct (overall status, per-criterion results, confidence scores).

### B. Utils (`utils/sonar_pplx.rs`)

- Functions for:
  - Building eligibility prompts.
  - Sending requests to Perplexity API.
  - Parsing and interpreting responses.

### C. Services (`services/eligibility_service.rs`)

- Orchestrates the eligibility check:
  - Receives input (from API or CSV).
  - Calls Perplexity API for each criterion.
  - Aggregates and formats results.

### D. Routes (`routes/eligibility_routes.rs`)

- API endpoints:
  - `/eligibility/check` (POST): Accepts input, returns eligibility result as JSON.
  - `/eligibility/check-local` (POST/GET): For local CSV-based testing.

### E. CSV Processing (`utils/csv_processing/`)

- Functions for:
  - Reading CSV files.
  - Normalizing/validating data into `EligibilityCheckInput`.

### F. Output

- Write results to:
  - JSON file (e.g., `backend/data/eligibility_results/eligibility_<timestamp>.json`)
  - Return as JSON object from the API.

---

## 6. Extensibility & Testing

- **Extensible:**  
  - Easy to add new eligibility criteria or swap out Perplexity for another backend.
- **Testing:**  
  - Unit tests for prompt construction, response parsing, and the service layer.
  - End-to-end test using sample CSV data.

---

