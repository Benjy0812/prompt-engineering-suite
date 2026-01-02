# 🤖 Global Git Commit Agent

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com/)
[![Audience: Professional](https://img.shields.io/badge/Audience-Professional-blue)](https://github.com/)
[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](../../LICENSE.md)

A context-aware automation agent designed to produce industry-standard commit
messages and terminal commands instantly.

## 🚀 Overview

The **Global Git Commit Agent** eliminates the friction of writing manual logs.
By analyzing your actual code changes, it selects the appropriate
[Conventional Commit](https://www.conventionalcommits.org/) type and
[Gitmoji](https://gitmoji.dev/), providing you with a ready-to-run terminal
command.

## ✨ Key Features

- **Contextual Intelligence:** Automatically detects if your change is a `fix`,
  `feat`, or `refactor` based on code diffs.
- **Emoji-Enhanced Logs:** Uses visual markers to make your `git log` scannable
  and professional.
- **CLI Optimized:** Outputs raw bash commands for immediate copy-pasting or
  execution.
- **Best Practices Enforced:** Adheres to the 50/72 character rule and
  imperative mood for professional logs.

## 🛠 Usage

1. **Analysis:** Run your AI CLI (e.g., Gemini CLI) and provide the output of
   `git diff`.
2. **Command Generation:** The agent will return a block like:

   ```bash
   git add -A
   git commit -m "fix(ui): 🐛 resolve z-index overlap on mobile header"
   ```
