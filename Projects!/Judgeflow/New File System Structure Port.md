---
title: New File System Structure Port
author:
  - Jon Marien
created: 2025-05-02
published: 2025-05-02
tags:
  - judgeflow
---

| Title                          | Author                       | Created      | Published    | Tags                       |
| ------------------------------ | ---------------------------- | ------------ | ------------ | -------------------------- |
| New File System Structure Port | <ul><li>Jon Marien</li></ul> | May 02, 2025 | May 02, 2025 | [[#judgeflow\|#judgeflow]] |

# JudgeFlow Project Restructure Comparison

## Overview
This document provides a comprehensive comparison of the file structure and organization changes between the `main` branch and the `project-restructure` branch in the JudgeFlow backend repository. It explains what was changed, why these changes were made, and the architectural implications of the restructuring.

## High-Level Architectural Goals
The primary goals behind the project restructuring were:

1. **Improved Code Organization**: Establish a clearer separation of concerns by organizing code into well-defined layers and modules.
2. **Enhanced Maintainability**: Make the codebase easier to navigate, understand, and modify by applying consistent organizational patterns.
3. **Better Scalability**: Ensure the structure can accommodate project growth with minimal friction.
4. **Clearer Dependencies**: Make dependencies between components more explicit and manageable.

## Directory Structure Changes

### Top-Level Directory Structure

The top-level directory structure remains largely the same between the two branches:

```
certs/
data/
scripts/
src/
target/
tests/
```

The most significant changes are within the `src` directory, which has been substantially reorganized.

### Source Directory Structure

#### Main Branch (`main`) src/ Structure:
```
src/
├── api/
│   ├── devpost_scrape.rs
│   ├── mod.rs
│   ├── notify.rs
│   ├── resource.rs
│   ├── resources.rs
│   ├── sync.rs
│   ├── waitlist.rs
│   ├── webhook_notifier.rs
│   └── webhooks.rs
└── utils/
```

#### Restructured Branch (`project-restructure`) src/ Structure:
```
src/
├── api/
├── middleware/
│   ├── auth.rs
│   └── mod.rs
├── models/
│   ├── devpost_model.rs
│   ├── import_model.rs
│   ├── mod.rs
│   ├── notify_model.rs
│   ├── resources.rs
│   ├── sync_model.rs
│   ├── waitlist_model.rs
│   └── webhook_model.rs
├── routes/
│   ├── devpost_routes.rs
│   ├── import_routes.rs
│   ├── mod.rs
│   ├── notify_routes.rs
│   ├── resource_routes.rs
│   ├── sync_routes.rs
│   ├── waitlist_routes.rs
│   └── webhook_routes.rs
├── services/
│   ├── devpost_service.rs
│   ├── import_service.rs
│   ├── mod.rs
│   ├── notify_service.rs
│   ├── resource_service.rs
│   ├── sync_service.rs
│   ├── waitlist_service.rs
│   └── webhook_service.rs
├── utils/
│   └── csv_processing/
├── constants.rs
└── mod.rs
```

## Key Architectural Changes

### 1. Layered Architecture
The restructured project adopts a more clearly defined layered architecture:

- **Routes Layer**: Handles HTTP request routing and parameter validation
- **Service Layer**: Contains business logic and orchestrates operations
- **Model Layer**: Defines data structures and database interactions
- **Middleware Layer**: Provides cross-cutting concerns like authentication

This layered approach provides a clearer separation of concerns compared to the previous structure where these responsibilities were mixed within the `api` directory.

### 2. Domain-Driven Organization
The project structure now organizes code by domain concerns (devpost, webhook, waitlist, etc.) within each layer, instead of having everything consolidated in the `api` directory. This makes it easier to locate related code across different layers.

### 3. Middleware Extraction
Authentication and other cross-cutting concerns have been moved to a dedicated `middleware` directory, making these components more reusable and maintainable.

## Comprehensive File Changes

### New Files in project-restructure
The following files were added in the restructuring:

```rust
backend/src/constants.rs
backend/src/main.rs.bak
backend/src/middleware/mod.rs
backend/src/mod.rs
backend/src/models/devpost_model.rs
backend/src/models/import_model.rs
backend/src/models/mod.rs
backend/src/models/notify_model.rs
backend/src/models/resources.rs
backend/src/models/sync_model.rs
backend/src/models/waitlist_model.rs
backend/src/models/webhook_model.rs
backend/src/routes/import_routes.rs
backend/src/routes/mod.rs
backend/src/routes/notify_routes.rs
backend/src/routes/resource_routes.rs
backend/src/routes/sync_routes.rs
backend/src/routes/waitlist_routes.rs
backend/src/routes/webhook_routes.rs
backend/src/services/mod.rs
backend/src/services/notify_service.rs
backend/src/services/resource_service.rs
backend/src/services/sync_service.rs
backend/src/services/waitlist_service.rs
backend/src/services/webhook_service.rs
backend/uuid_line.txt
```

Key additions include:
- New `mod.rs` files to organize modules
- Domain-specific model files
- Domain-specific route handlers
- Domain-specific service implementations
- `constants.rs` for centralized constants management

### Removed Files
The following files were removed or replaced:

```rust
backend/src/api/devpost_scrape.rs
backend/src/api/mod.rs
backend/src/api/notify.rs
backend/src/api/resource.rs
backend/src/api/resources.rs
backend/src/api/sync.rs
backend/src/api/waitlist.rs
backend/src/api/webhook_notifier.rs
backend/src/api/webhooks.rs
backend/src/config.rs
backend/tests/api_integration.rs
```

The functionality in these files was redistributed to the appropriate layers in the new structure.

### Modified Files
Several files were modified to align with the new structure:

```rust
backend/Cargo.lock
backend/Cargo.toml
backend/scripts/backfill_clerk_to_supabase.rs
backend/src/lib.rs
backend/src/main.rs
backend/src/middleware/auth.rs
```

These modifications were necessary to:
- Update import paths
- Adjust for the new module organization
- Update dependencies in Cargo.toml

## Architectural Implications

### 1. Improved Maintainability
The restructured codebase is more maintainable because:
- Related code is grouped together by both layer and domain
- Cross-cutting concerns are properly isolated
- Module boundaries are clearly defined with `mod.rs` files

### 2. Better Testability
The layered architecture improves testability by:
- Making dependencies more explicit
- Enabling better mocking of dependencies
- Allowing for more focused unit tests

### 3. Easier Onboarding
Developers (us) will find it easier to understand the codebase because:
- The directory structure clearly communicates the application's architecture
- File naming conventions make it obvious where to find specific functionality
- The separation of concerns reduces cognitive load when working on a feature

### 4. Enhanced Scalability
The new structure is better equipped to handle growth because:
- New domains can be added by following the established patterns
- Domain-specific code is isolated, reducing merge conflicts
- Each layer can evolve independently

## Build and Deployment Impact
The restructuring has minimal impact on build and deployment processes:
- The overall project structure (with certs, data, scripts, etc.) remains unchanged
- The entry points (main.rs and lib.rs) still exist, though their contents have been modified
- Cargo dependencies remain largely the same

## Conclusion
The restructuring of the JudgeFlow backend represents a significant improvement in code organization and architecture. By transitioning from a flat structure to a layered, domain-driven approach, the project is now better positioned for maintainability, testability, and future growth.

