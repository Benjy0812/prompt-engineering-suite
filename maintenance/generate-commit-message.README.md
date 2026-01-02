# 📝 Git Assistant: Prompt Suite

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)  
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)  
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../LICENSE.md)

A specialized Git automation agent tailored for managing prompt engineering repositories and documentation workflows.

## 🚀 Overview

The **Prompt Suite Assistant** is optimized for the unique structure of prompt libraries. It tracks changes to specific logic blocks and documentation files, ensuring your version history clearly reflects which prompts were added, refined, or refactored.

## ✨ Key Features

- **Prompt-Centric Mapping:** Categorizes changes specifically as features (new prompts) or refactors (logic tuning).
- **Two-Tier Detail:** Generates a high-level summary followed by a file-specific breakdown.
- **CLI Ready:** Returns executable bash commands to keep you in the terminal.
- **Gitmoji Standard:** Uses visual cues to make the prompt history scannable.

## 🛠 Usage

1. **Trigger:** Provide your `git diff` or let your CLI agent run `git status`.
2. **Execute:** Copy the output code block into your terminal.
3. **Review:** Your logs will now show clear, professional prompt-specific updates.

## 📊 Mapping Standards

| Icon | Type       | Context                                       |
| :--- | :--------- | :-------------------------------------------- |
| ✨   | `feat`     | New prompt files or core logic updates.       |
| ♻️   | `refactor` | Tuning prompt instructions for better output. |
| 📝   | `docs`     | Modifying READMEs or metadata.                |
| 🎨   | `style`    | Formatting Markdown or fixing indentation.    |

## ⚠️ Requirements

- Git initialized in the project directory.
- An AI assistant with terminal access or diff-reading capabilities.
