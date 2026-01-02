# 🌐 Web Dev Commit Agent

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)  
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)  
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../../LICENSE.md)

A specialized AI agent for web developers that automates the generation of stack-aware, professional commit messages.

## 🚀 Overview

The **Web Dev Commit Agent** interprets changes across the full web stack—from CSS adjustments to API logic. It maps these changes to the [Conventional Commits](https://www.conventionalcommits.org/) standard, ensuring your project history is clean, semantic, and easy to navigate.

## ✨ Key Features

- **Stack Sensitivity:** Recognizes the difference between a UI `style` change and a backend `refactor`.
- **Auto-Scoping:** Detects affected modules (e.g., `auth`, `store`, `views`) based on file paths.
- **Gitmoji Integration:** Enhances scannability with visual cues for different change types.
- **Professional Standards:** Enforces the 50/72 character rule and imperative mood.

## 🛠 Usage

1. **Input:** Provide the output of `git diff` or a list of modified files.
2. **Generation:** The agent produces a single, executable `git commit` command.
3. **Execution:** Copy and paste directly into your terminal to maintain a perfect commit history.

## 📊 Mapping Table

| Stack Area       | Type    | Gitmoji |
| :--------------- | :------ | :------ |
| **Frontend/UI**  | `style` | 🎨      |
| **Logic/API**    | `feat`  | ✨      |
| **Dependencies** | `build` | 📦      |
| **Optimization** | `perf`  | ⚡      |

## ⚠️ Requirements

- Best used with an AI CLI that can read local `git diff` output.
- Assumes a standard web project structure (e.g., `/src`, `/api`, `/public`).
