# 📖 Repository & Code Explainer

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../../LICENSE.md)

An agentic AI prompt designed to transform complex source code into structured,
professional-grade documentation.

## 🚀 Overview

The **Repository Explainer** functions as a virtual Lead Developer. It goes
beyond simple code comments to explain the "Big Picture"—mapping how different
files interact, identifying the tech stack, and providing clear setup
instructions for new contributors.

## ✨ Key Features

- **Structural Stack Analysis:** Detects entry points and dependencies
  instantly.
- **Dependency Mapping:** Visualizes the relationships between internal modules.
- **Onboarding Optimized:** Structured specifically to help new developers
  understand a codebase in minutes.
- **Architectural Insights:** Identifies design patterns and suggests technical
  improvements.

## 🛠 Usage

1. **Context Collection:** If using a CLI agent, it will automatically run `ls`
   and `cat`. For standard AI, paste your file tree and core files.
2. **Generation:** The agent will output a clean, well-structured Markdown
   document.
3. **Deployment:** Save the resulting text as `EXPLAINER.md` or use it to
   populate your project Wiki.

## 📊 Documentation Structure

| Section        | Focus                                          |
| :------------- | :--------------------------------------------- |
| **Overview**   | High-level project goal and stack.             |
| **Structure**  | Folder-by-folder responsibility mapping.       |
| **Core Logic** | Explanation of complex functions/classes.      |
| **Usage**      | Practical commands for installation/execution. |

## ⚠️ Requirements

- Best results are achieved when providing configuration files (e.g.,
  `package.json`, `go.mod`, `pyproject.toml`).
