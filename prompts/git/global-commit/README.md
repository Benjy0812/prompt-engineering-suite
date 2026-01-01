# Global Commit Message Generator AI Prompt

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)  
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

This repository contains a **professional AI prompt** that generates **descriptive, context-aware Git commit messages** for any project or programming language. The commit messages follow **Conventional Commits style** and can include **Git emojis** when appropriate. It also outputs **ready-to-run Git commands** to stage and commit your changes.

---

## 📌 Features

- ✅ Generates professional, readable commit messages
- ✅ Supports Conventional Commit types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`
- ✅ Includes **Git emojis** corresponding to commit type (optional but recommended)
- ✅ Provides a concise summary and optional detailed description
- ✅ Outputs **Git commands** (`git add`, `git commit -m`) ready to run
- ✅ Works for **any project, framework, or language**

---

## 🔍 Usage

1. Open `commit-prompt.md` (the AI prompt file).
2. Copy the prompt into your AI interface.
3. Provide the staged changes, diff, or project context.
4. The AI will generate:
   - A short, descriptive summary
   - Optional detailed description (≤ 72 characters per line)
   - Appropriate Git emojis based on commit type
   - Git commands to stage and commit the changes
5. Copy the generated commands into your terminal, for example:

```bash
git add <file1> <file2> ...
git commit -m "<generated commit message>"
```
