# 🐳 Docker Architect Agent

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../../LICENSE.md)

A high-performance AI agentic prompt designed to automate the creation of secure, optimized, and multi-stage Docker configurations.

## 🚀 Overview

The **Docker Architect Agent** acts as a virtual DevOps specialist. Instead of generic templates, it analyzes your specific project structure to implement industry best practices—such as layer caching, multi-stage builds, and non-root security—ensuring your images are production-ready from the start.

## ✨ Key Features

- **Smart Stack Detection:** Automatically configures environments for Node.js, Python, Go, Rust, Java, and more.
- **Multi-Stage Optimization:** Drastically reduces final image footprint by stripping away build-time dependencies.
- **Security-First Approach:** Implements non-privileged users and secure defaults to minimize attack surfaces.
- **Layer-Cache Efficiency:** Orders instructions to ensure faster rebuilds during development.
- **Compose Ready:** Handles multi-service orchestration logic when dependencies are detected.

## 🛠 Usage

1. **Context Acquisition:** Provide the agent with your file list and core configuration files (e.g., `cat package.json`).
2. **Generation:** The agent provides copy-pasteable `Dockerfile`, `.dockerignore`, and `docker-compose.yml` files.
3. **Execution:** Use the generated "How to Run" section to build and deploy your container instantly.

## 📊 Container Standards

| Feature        | Implementation                                            |
| :------------- | :-------------------------------------------------------- |
| **Base Image** | Minimal footprints (Alpine, Distroless, or Slim).         |
| **User**       | Non-root execution for runtime security.                  |
| **Caching**    | Dependency installation isolated from source code copies. |
| **Cleanup**    | Removal of temporary build artifacts and package caches.  |

## ⚠️ Requirements

- Valid dependency manifest in the root directory.
- Docker Engine 20.10+ for multi-stage support.
