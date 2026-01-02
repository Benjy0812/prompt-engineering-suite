# 🛠️ Prompt Architect Agent

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)  
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)  
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../LICENSE.md)

The core engine for the "Prompt Engineering Suite" designed to build other high-quality prompts.

## 🚀 Overview

The **Prompt Architect Agent** is a meta-prompt. It uses senior-level engineering principles to draft, structure, and lint new AI instructions. It ensures that every prompt added to your suite is consistent, professional, and optimized for LLM reasoning.

## ✨ Key Features

- **Persona Injection:** Automatically assigns high-authority roles to the AI.
- **Markdownlint Integration:** Every generated prompt is pre-validated against MD001–MD060 standards.
- **Agentic Logic:** Structures instructions to favor "Step-by-Step" execution.
- **Production Standard:** Generates files that are ready for immediate repository commit.

## 🛠 Usage

1. **Input:** Define the task (e.g., "Create a prompt for SQL optimization").
2. **Generation:** The Architect generates a full `.md` file following the suite's standards.
3. **Save:** Place the output in the appropriate category folder of your repository.

## 📊 Quality Standards

| Rule            | Implementation                                   |
| :-------------- | :----------------------------------------------- |
| **Hierarchy**   | Sequential headers (`#`, `##`, `###`).           |
| **Formatting**  | Fenced code blocks with language hints.          |
| **Variables**   | Standardized `[Bracketed]` placeholders.         |
| **Cleanliness** | Zero trailing spaces or consecutive blank lines. |

## ⚠️ Requirements

- Best used in conjunction with a Markdown linter to verify final output.
