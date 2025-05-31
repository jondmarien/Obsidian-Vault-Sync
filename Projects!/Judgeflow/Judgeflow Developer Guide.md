---
title: Judgeflow Developer Guide
author:
  - Jon Marien
created: 2025-05-02
published: 2025-05-02
tags:
  - judgeflow
---

| Title                     | Author                       | Created      | Published    | Tags                       |
| ------------------------- | ---------------------------- | ------------ | ------------ | -------------------------- |
| Judgeflow Developer Guide | <ul><li>Jon Marien</li></ul> | May 02, 2025 | May 02, 2025 | [[#judgeflow\|#judgeflow]] |

# JudgeFlow Developer Guide

## Overview

This developer guide provides comprehensive information about the JudgeFlow backend architecture, code organization, and development workflows. It is designed to help new and existing developers understand the codebase structure, coding standards, and best practices for contributing to the project.

## Table of Contents

1. [Architecture](#architecture)
   - [Layered Architecture](#layered-architecture)
   - [Directory Structure](#directory-structure)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Environment Setup](#environment-setup)
   - [Building the Project](#building-the-project)
3. [Code Organization](#code-organization)
   - [Routes Layer](#routes-layer)
   - [Services Layer](#services-layer)
   - [Models Layer](#models-layer)
   - [Middleware Layer](#middleware-layer)
   - [Utils](#utils)
4. [Development Workflows](#development-workflows)
   - [Adding a New Feature](#adding-a-new-feature)
   - [Making Changes to Existing Features](#making-changes-to-existing-features)
   - [Testing Your Changes](#testing-your-changes)
5. [Coding Standards](#coding-standards)
   - [Rust Code Style](#rust-code-style)
   - [Documentation](#documentation)
   - [Error Handling](#error-handling)
6. [Key Dependencies](#key-dependencies)
7. [Common Tasks](#common-tasks)
   - [Working with Supabase](#working-with-supabase)
   - [CSV Processing](#csv-processing)
   - [Perplexity Sonar API Integration](#perplexity-sonar-api-integration)
8. [Troubleshooting](#troubleshooting)

## Architecture

### Layered Architecture

JudgeFlow backend follows a layered architecture pattern that separates concerns into distinct layers:

1. **Routes Layer**: Handles HTTP request routing and parameter validation
2. **Service Layer**: Contains business logic and orchestrates operations
3. **Model Layer**: Defines data structures and database interactions
4. **Middleware Layer**: Provides cross-cutting concerns like authentication

This layered approach provides several benefits:
- Clear separation of concerns
- Improved maintainability
- Better testability
- Enhanced scalability

### Directory Structure

The JudgeFlow backend follows a domain-driven directory structure within each layer:

```
backend/
├── certs/
├── data/
├── scripts/
├── src/
│   ├── api/
│   ├── middleware/
│   │   ├── auth.rs
│   │   └── mod.rs
│   ├── models/
│   │   ├── devpost_model.rs
│   │   ├── import_model.rs
│   │   ├── mod.rs
│   │   ├── notify_model.rs
│   │   ├── resources.rs
│   │   ├── sync_model.rs
│   │   ├── waitlist_model.rs
│   │   └── webhook_model.rs
│   ├── routes/
│   │   ├── devpost_routes.rs
│   │   ├── import_routes.rs
│   │   ├── mod.rs
│   │   ├── notify_routes.rs
│   │   ├── resource_routes.rs
│   │   ├── sync_routes.rs
│   │   ├── waitlist_routes.rs
│   │   └── webhook_routes.rs
│   ├── services/
│   │   ├── devpost_service.rs
│   │   ├── import_service.rs
│   │   ├── mod.rs
│   │   ├── notify_service.rs
│   │   ├── resource_service.rs
│   │   ├── sync_service.rs
│   │   ├── waitlist_service.rs
│   │   └── webhook_service.rs
│   ├── utils/
│   │   └── csv_processing/
│   ├── constants.rs
│   ├── lib.rs
│   ├── main.rs
│   ├── sonar_pplx.rs      # Perplexity Sonar API integration
│   └── supabase_example.rs # Supabase integration examples
├── target/
├── tests/
├── .env
├── .env.example
├── Cargo.toml
├── Cargo.lock
└── README.md
```

## Getting Started

### Prerequisites

- [Rust](https://www.rust-lang.org/tools/install)
- [Cargo](https://doc.rust-lang.org/cargo/)
- Access to Supabase project (for database functionality)
- Perplexity Sonar API key (if using AI capabilities)

### Environment Setup

1. Clone the repository
2. Create a `.env` file with the required environment variables:

```env
SONAR_PPLX_API_KEY=your-perplexity-api-key-here
SUPABASE_URL=https://your-project.supabase.co/rest/v1/
SUPABASE_API_KEY=your-supabase-api-key-here
```

### Building the Project

```bash
# Build the project
cargo build

# Run the project
cargo run

# Run tests
cargo test
```

## Code Organization

### Routes Layer

The routes layer (`src/routes/`) handles HTTP routing and request validation. Each domain area has its own routes file:

- `devpost_routes.rs`: Routes related to Devpost integration
- `import_routes.rs`: Routes for data import functionality
- `notify_routes.rs`: Notification-related routes
- `resource_routes.rs`: Routes for resource management
- `sync_routes.rs`: Synchronization-related routes
- `waitlist_routes.rs`: Waitlist management routes
- `webhook_routes.rs`: Webhook handling routes

Routes should:
- Validate incoming request data
- Call appropriate service methods
- Handle HTTP response formatting
- Not contain business logic (defer to services)

### Services Layer

The services layer (`src/services/`) contains the core business logic of the application:

- `devpost_service.rs`: Devpost integration logic
- `import_service.rs`: Data import processing logic
- `notify_service.rs`: Notification handling logic
- `resource_service.rs`: Resource management logic
- `sync_service.rs`: Synchronization logic
- `waitlist_service.rs`: Waitlist management logic 
- `webhook_service.rs`: Webhook processing logic

Services should:
- Implement domain-specific business logic
- Orchestrate model operations
- Be stateless when possible
- Handle error cases appropriately

### Models Layer

The models layer (`src/models/`) defines data structures and database interactions:

- `devpost_model.rs`: Devpost data structures and DB operations
- `import_model.rs`: Import-related data structures
- `notify_model.rs`: Notification data structures
- `resources.rs`: Resource-related data structures
- `sync_model.rs`: Synchronization data structures
- `waitlist_model.rs`: Waitlist data structures
- `webhook_model.rs`: Webhook data structures

Models should:
- Define schema/data structures
- Handle database operations
- Implement validation logic
- Provide serialization/deserialization

### Middleware Layer

The middleware layer (`src/middleware/`) provides cross-cutting functionality:

- `auth.rs`: Authentication and authorization logic

Middleware should:
- Focus on cross-cutting concerns
- Be reusable across multiple routes
- Have minimal dependencies on specific domains

### Utils

The utils directory (`src/utils/`) contains helper functions and utilities:

- `csv_processing/`: Utilities for processing CSV data

Utils should:
- Be stateless, pure functions when possible
- Provide reusable functionality
- Be well-documented with examples

## Development Workflows

### Adding a New Feature

When adding a new feature to JudgeFlow:

1. **Identify the Domain**: Determine which domain area your feature belongs to (devpost, webhook, resources, etc.)
2. **Define Models**: Create or update models to represent your feature's data
3. **Implement Services**: Add business logic in the appropriate service
4. **Create Routes**: Define HTTP endpoints in the routes layer
5. **Update Tests**: Add tests for your new functionality
6. **Document**: Update documentation to explain the new feature

### Making Changes to Existing Features

When modifying existing functionality:

1. **Understand Current Implementation**: Review the existing code across all layers
2. **Make Layer-Appropriate Changes**: Keep changes consistent with the architectural pattern
3. **Maintain Separation of Concerns**: Don't mix business logic with routing or data access
4. **Ensure Test Coverage**: Update tests to cover your changes

### Testing Your Changes

```bash
# Run all tests
cargo test

# Run tests for a specific module
cargo test <module_name>

# Run with verbose output
cargo test -- --nocapture
```

## Coding Standards

### Rust Code Style

- Follow idiomatic Rust patterns and conventions
- Use the Rust formatter (`rustfmt`) to maintain consistent style
- Prefer using Rust's Result and Option types for error handling
- Keep functions focused and small (under 100 lines when possible)

### Documentation

- Document public interfaces with doc comments (`///`)
- Include examples for complex functions
- Keep comments up-to-date with code changes
- Use inline comments to explain non-obvious logic

### Error Handling

- Use proper error types from `std::error::Error`
- Create custom error types for domain-specific errors
- Avoid panic! in production code paths
- Log errors with appropriate context

## Key Dependencies

- [`csv`](https://crates.io/crates/csv): CSV parsing and writing
- [`polars`](https://crates.io/crates/polars): DataFrame operations
- [`serde`](https://crates.io/crates/serde): Serialization/deserialization
- [`sqlx`](https://crates.io/crates/sqlx): SQL database access
- [`postgrest`](https://crates.io/crates/postgrest): Supabase RESTful access
- [`reqwest`](https://crates.io/crates/reqwest): HTTP client
- [`dotenv`](https://crates.io/crates/dotenv): Environment variable loading

## Common Tasks

### Working with Supabase

Supabase is integral to the JudgeFlow backend for database operations and API access. Follow these steps to work with Supabase within the new structure:

- **Configuration**: Set up environment variables (`SUPABASE_URL` and `SUPABASE_API_KEY`) in your `.env` file as detailed in [Environment Setup](#environment-setup).
- **Database Operations**: Use the `postgrest` crate or Supabase client for CRUD operations. Place database interaction logic in the appropriate model file under `src/models/`, such as `resources.rs` for resource-related data.
- **Edge Functions**: For background tasks like batch updates, use Supabase Edge Functions. Keep related logic in service files under `src/services/` to maintain separation of concerns.
- **Optimization**: Optimize queries with indexing and caching. Store reusable database utilities in `src/utils/` if they are not domain-specific.

Adhere to the layered architecture by ensuring Supabase interactions are handled in the model layer, while business logic remains in the service layer.

### CSV Processing

CSV processing is often required for data imports and exports in JudgeFlow. The utilities for this are located in `src/utils/csv_processing/`. Here's how to handle CSV tasks:

- **Parsing and Validation**: Use the `csv` crate for reading and writing CSV files. Implement parsing logic in utility functions under `src/utils/csv_processing/`.
- **Data Manipulation**: For complex data operations, use the `polars` crate. Keep such logic in service files under `src/services/` if tied to a specific domain.
- **Error Handling**: Ensure robust error handling in utility functions to catch malformed data or file issues. Log errors with context for traceability.

Maintain stateless utility functions and document them with examples to support reuse across domains.

### Perplexity Sonar API Integration

JudgeFlow integrates with the Perplexity Sonar API for AI-driven features, with code located in `src/sonar_pplx.rs`. Follow these guidelines to work with this integration:

- **Setup**: Configure the `SONAR_PPLX_API_KEY` in your `.env` file as described in [Environment Setup](#environment-setup).
- **API Requests**: Use the `reqwest` crate for HTTP requests to the Sonar API. Place integration logic in a dedicated service file under `src/services/` if it involves business logic, or in `src/utils/` for generic helpers.
- **Model Usage**: Select between `sonar` and `sonar-pro` models based on functionality needs. Monitor credit usage to manage costs.
- **Testing**: Limit API calls during development by mocking responses. Store mock utilities in `src/utils/` or test-specific directories under `tests/`.

Keep API interaction logic modular and follow the domain-driven structure by associating it with relevant layers.

## Troubleshooting

### Common Issues and Solutions

Encountering issues is part of development with JudgeFlow. Here are solutions to frequent problems within the new structure:

- **Supabase Connectivity**: If connections fail, verify `SUPABASE_URL` and `SUPABASE_API_KEY` in `.env`. Check Supabase project status and usage limits via the dashboard.
- **Edge Function Errors**: Background tasks in Supabase Edge Functions may terminate early during local testing. Adjust `supabase/config.toml` to use the `per_worker` policy and restart manually if needed.
- **Sonar API Credit Limits**: If credits deplete rapidly, switch to the `sonar` model and reduce calls during testing. Review usage logs for optimization.
- **CSV Processing Failures**: Malformed CSV data often causes errors. Validate input in utility functions under `src/utils/csv_processing/` and log specific issues.
- **Build Errors**: Failures in `cargo build` or `cargo test` may result from outdated dependencies or Rust versions. Run `cargo update` and ensure your environment matches prerequisites.

Locate relevant code in the appropriate layer or domain directory to address issues efficiently.

### Debugging Tips

Debugging within JudgeFlow's layered structure requires a systematic approach:

- **Trace Execution**: Add log statements in code to track flow across layers. Use domain-specific logs in `src/services/` or `src/routes/` for clarity.
- **Use Tools**: Leverage IDE debuggers with breakpoints to inspect state in specific modules like `src/models/` or `src/services/`.
- **Review Logs**: In production, check logs around the time of an issue to identify affected domains or layers.
- **Reproduce Issues**: Attempt to replicate errors in a local environment to determine if they are code or environment-specific.
- **Profile Code**: Use profiling tools to find bottlenecks, especially in database operations under `src/models/` or API calls in `src/services/`.

Focus on isolating issues to specific layers or domains using the directory structure as a guide.

### Best Practices for Troubleshooting

Adopt these practices to streamline troubleshooting in the restructured JudgeFlow backend:

- **Document Findings**: Record issues and fixes in a shared log or README to aid future debugging.
- **Validate Data**: Check inputs and outputs at each layer to catch errors early, especially in routes (`src/routes/`) and models (`src/models/`).
- **Test Across Environments**: Verify changes locally and in staging to ensure consistency across setups.
- **Monitor Performance**: Use tools to track backend health, focusing on domain-specific metrics in service logs.
- **Collaborate**: Share insights with team members to resolve complex issues, referencing specific files or directories under `src/`.

Use the clear separation of concerns in the new structure to narrow down problem areas and apply fixes effectively.
