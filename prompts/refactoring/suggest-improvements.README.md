# 📈 Project Improvement Agent

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../../LICENSE.md)

An agentic AI prompt designed to act as a code reviewer and architectural
consultant within your CLI workflow.

## 🚀 Overview

The **Project Improvement Agent** delivers high-signal, actionable feedback on
any codebase. It identifies architectural weaknesses, security risks, and
performance gaps, providing clear "Before/After" examples to guide your
refactoring process.

## ✨ Key Features

- **Full-Spectrum Analysis:** Covers quality, performance, security, and
  infrastructure.
- **Actionable Refactors:** Provides direct code examples to illustrate
  suggested changes.
- **CLI-First Design:** Optimized for terminal-based AI tools to provide instant
  feedback without manual copy-pasting.
- **Context Awareness:** Adjusts suggestions based on the detected language and
  framework.

## 🛠 Usage

1. **Analysis:** Run your CLI AI tool and provide the source file or directory
   list.
2. **Review:** The agent generates a structured improvement report in Markdown.
3. **Refactor:** Use the provided suggestions to update your code and resolve
   technical debt.

## 📊 Evaluation Categories

| Category         | Focus Area                                          |
| :--------------- | :-------------------------------------------------- |
| **Code Quality** | DRY principle, SOLID patterns, and naming.          |
| **Performance**  | Algorithmic efficiency and resource management.     |
| **Security**     | Vulnerability scanning and credential safety.       |
| **CI/CD**        | Modernization, containerization, and test coverage. |

## ⚠️ Requirements

- For directory-wide analysis, ensure the AI has access to the file tree and
  core configuration files.
