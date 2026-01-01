# Dockerfile Generator AI Prompt

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

This repository contains a **professional AI prompt** that generates **production-ready Docker setups** for any software project. It can produce a Dockerfile, optional docker-compose.yml, and instructions for building and running the project in containers.

---

## 📌 Features

- ✅ Generates a **Dockerfile** optimized for project language and dependencies
- ✅ Optionally generates **docker-compose.yml** for multi-service projects
- ✅ Includes best practices: minimal base images, caching, environment variables, ports, volumes
- ✅ Strict, professional Markdown formatting for all outputs
- ✅ Clear, concise instructions for building and running Docker containers

---

## 🔍 Usage

1. Open `docker-prompt.md` (or the main prompt file).
2. Copy the prompt into your AI system interface.
3. Provide the project structure or repository path as input.
4. The AI will generate:
   - `Dockerfile`
   - Optional `docker-compose.yml` (if multi-service)
   - Markdown instructions for usage
5. Review and copy the generated files to your project directory.
6. Build and run the Docker container(s) as instructed.

---

## 🧭 Recommendations

- Keep project dependencies pinned for reproducibility.
- Verify generated Dockerfiles using `docker build` before production deployment.
- Use minimal images to reduce container size and attack surface.
- Lint Markdown outputs if included in documentation.

---

## 📄 License

This prompt and repository content are released under the [MIT License](LICENSE).
