# Web Development Commit Message Generator AI Prompt

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)
[![Audience: Web Developers](https://img.shields.io/badge/Audience-Web%20Developers-blue)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

This repository contains a **professional AI prompt** that generates **descriptive, context-aware Git commit messages** specifically for **web development projects**. The commit messages follow **Conventional Commits style** and can include **Git emojis** relevant to frontend, backend, API, and CI/CD changes.

---

## 📌 Features

- ✅ Generates commit messages for **frontend and backend changes**
- ✅ Supports Conventional Commit types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`
- ✅ Includes **Git emojis** corresponding to commit type (optional but recommended)
- ✅ Optional detailed description (≤ 72 characters per line)
- ✅ Ready to copy-paste into `git commit -m`
- ✅ Works for any web development stack (React, Vue, Angular, Node.js, Python, PHP, etc.)

---

## 🔍 Usage

1. Open `web-commit-prompt.md` (the AI prompt file).
2. Copy the prompt into your AI interface.
3. Provide the staged changes, diff, or project context.
4. The AI will generate a commit message that includes:
   - Short descriptive summary (≤ 50 characters)
   - Optional detailed description
   - Appropriate Git emojis based on change type
5. Copy the generated message into your terminal:

```bash
git commit -m "<generated commit message>"
```
