# Prompt Engineering Suite

[![License: OpenRAIL-S](https://img.shields.io/badge/License-OpenRAIL--S-yellow.svg)](LICENSE.md)

A curated collection of text-based prompts designed for Large Language Models
(LLMs) like Gemini and Claude. This suite aims to standardize and enhance the
output of LLMs for common development and documentation tasks, such as
generating well-formatted Markdown files and consistent Git commit messages.

## Table of Contents

- [Introduction](#introduction)
- [Prompt Categories](#prompt-categories)
  - [Code Analysis](#code-analysis)
  - [Git & Maintenance](#git--maintenance)
  - [Infrastructure as Code](#infrastructure-as-code)
  - [Markdown Generation](#markdown-generation)
  - [Refactoring](#refactoring)
  - [Testing](#testing)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In an era of increasing reliance on AI for development and content creation,
maintaining clarity and quality is helpful. The Prompt Engineering Suite
provides a robust set of expertly crafted prompts, allowing developers,
technical writers, and content creators to leverage LLMs more effectively. By
using these prompts, you can ensure that your generated content follows
professional conventions and maintains a clear tone.

## Prompt Categories

### Code Analysis

- **`prompts/code/explain-code.md`**: Provides a detailed, multi-level
  explanation of code snippets, from high-level purpose to line-by-line
  analysis.

### Git & Maintenance

- **`prompts/git/global-commit.md`**: Generates professional Conventional Commit
  messages with Gitmojis, suitable for any project.
- **`prompts/git/web-dev-commit.md`**: A specialized prompt for web development
  contexts, including stack-aware scoping (API, UI, Auth, etc.).
- **`maintenance/generate-commit-message.md`**: Specifically designed for this
  repository's two-tier commit message style.
- **`maintenance/generate-prompt.md`**: A meta-prompt to assist in generating
  new, high-quality prompts for this suite.

### Infrastructure as Code

- **`prompts/iac/generate-dockerfile.md`**: Generates optimized, secure, and
  production-ready Dockerfiles based on application requirements.

### Markdown Generation

- **`prompts/markdown/markdown-strict.md`**: Instructs the AI to act as an
  expert technical writer, generating Markdown that follows standard conventions
  and consistency.
- **`prompts/markdown/markdown-relaxed.md`**: Prioritizes readability and
  natural language flow, suitable for less formal documentation.

### Refactoring

- **`prompts/refactoring/suggest-improvements.md`**: Analyzes code for potential
  bottlenecks, anti-patterns, and readability issues, providing actionable
  refactoring suggestions.

### Testing

- **`prompts/testing/generate-unit-tests.md`**: Generates comprehensive unit
  tests with high edge-case coverage using appropriate testing frameworks.

## Usage

The prompts within this repository are designed to be easily integrated with
various Large Language Model (LLM) CLI tools (e.g., Gemini CLI, Claude Code
CLI).

You can use these prompts by either:

1. **Copy-pasting the content:** View the content of the desired prompt file and
   paste it directly into your LLM CLI tool's prompt input.

   ```bash
   cat prompts/markdown/markdown-strict.md
   # Copy the output and paste into your LLM CLI tool.
   gemini ask "PASTE_YOUR_PROMPT_HERE"
   ```

2. **Piping the content (if supported by your CLI tool):** Many modern LLM CLI
   tools support reading prompt content directly from a file or standard input.

   ```bash
   cat prompts/markdown/markdown-strict.md | gemini generate --model gemini-1.5-flash
   # Or, if your CLI accepts a file path directly:
   gemini generate --model gemini-1.5-flash --prompt-file prompts/markdown/markdown-strict.md
   ```

   > **Note**: Replace `gemini ask`, `gemini generate`, `--model`, and
   > `--prompt-file` with the actual commands and flags of your specific LLM CLI
   > tool. Refer to your CLI's official documentation for precise usage.

For more detailed instructions on using these prompts with specific CLI tools,
please refer to `USAGE_INSTRUCTIONS.md`.

## Prerequisites

To effectively use the prompts in this repository, you will need:

- A configured and functional Large Language Model (LLM) CLI tool (e.g.,
  [Google Gemini CLI](https://ai.google.dev/docs/gemini_api_overview),
  [Anthropic Claude CLI](https://docs.anthropic.com/claude/reference/claude-api)).
- Basic familiarity with using command-line interfaces.

## Contributing

We welcome contributions to expand and improve this Prompt Engineering Suite! If
you have well-crafted prompts that enhance LLM output for common development
tasks, please consider submitting a pull request.

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-prompt-name`).
3. Add your prompt(s) to an appropriate category, or create a new one.
4. Include a brief `README.md` within your new prompt directory explaining its
   purpose and usage.
5. Commit your changes (`git commit -m "feat: ✨ add new awesome prompt"`).
6. Push to the branch (`git push origin feature/your-prompt-name`).
7. Open a pull request with a clear description of your contribution.

## Repository Structure

```text
.
│   .gitignore
│   CONTRIBUTING.md
│   GEMINI.md
│   LICENSE.md
│   README.md
│   USAGE_INSTRUCTIONS.md
│
├───maintenance
│   ├───generate-commit-message.md
│   ├───generate-commit-message.README.md
│   ├───generate-prompt.md
│   └───generate-prompt.README.md
│
└───prompts
    ├───code
    │   ├───explain-code.md
    │   └───explain-code.README.md
    ├───git
    │   ├───global-commit.md
    │   ├───global-commit.README.md
    │   ├───web-dev-commit.md
    │   └───web-dev-commit.README.md
    ├───iac
    │   ├───generate-dockerfile.md
    │   └───generate-dockerfile.README.md
    ├───markdown
    │   ├───markdown-relaxed.md
    │   ├───markdown-relaxed.README.md
    │   ├───markdown-strict.md
    │   └───markdown-strict.README.md
    ├───refactoring
    │   ├───suggest-improvements.md
    │   └───suggest-improvements.README.md
    └───testing
        ├───generate-unit-tests.md
        └───generate-unit-tests.README.md
```

## License

This project is licensed under the OpenRAIL-S License - see the
[LICENSE.md](LICENSE.md) file for details.
