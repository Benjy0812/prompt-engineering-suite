# Prompt Engineering Suite

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A curated collection of text-based prompts designed for Large Language Models (LLMs) like Gemini and Claude. This suite aims to standardize and enhance the output of LLMs for common development and documentation tasks, such as generating well-formatted Markdown files and consistent Git commit messages.

## Table of Contents

- [Introduction](#introduction)
- [Prompt Categories](#prompt-categories)
  - [Markdown Generation Prompts](#markdown-generation-prompts)
  - [Git Commit Message Prompts](#git-commit-message-prompts)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In an era of increasing reliance on AI for development and content creation, maintaining consistency and quality is paramount. The Prompt Engineering Suite provides a robust set of expertly crafted prompts, allowing developers, technical writers, and content creators to leverage LLMs more effectively. By using these prompts, you can ensure that your generated content adheres to specific formatting standards and maintains a professional tone.

## Prompt Categories

### Markdown Generation Prompts

These prompts guide LLMs to produce Markdown output tailored for different levels of strictness and readability.

- **`prompts/markdown/markdown_strict_prompt.txt`**:
  This prompt instructs the AI to act as an expert technical writer, generating Markdown that is fully compliant with a strict set of `markdownlint` rules. Ideal for producing clean, production-ready documentation where formatting consistency is critical.

- **`prompts/markdown/markdown_relaxed_prompt.txt`**:
  This prompt also asks the AI to generate Markdown, but with a more flexible and relaxed set of rules. It prioritizes readability and natural language flow over strict linting compliance, suitable for less formal documentation or quick drafts.

### Git Commit Message Prompts

These prompts assist in generating standardized and informative Git commit messages.

- **`prompts/git/global_commit_message_prompt.txt`**:
  A global prompt for generating Git commit messages, applicable to any project. It has been updated with examples relevant to changes made within a prompt engineering project, promoting consistent and clear commit history.

- **`prompts/git/web-dev-commit/prompt.txt`**:
  A specialized prompt designed to help LLMs generate concise and meaningful Git commit messages, particularly for web development contexts. It encourages adherence to common commit message conventions, improving repository history clarity.

## Usage

The prompts within this repository are designed to be easily integrated with various Large Language Model (LLM) CLI tools (e.g., Gemini CLI, Claude Code CLI).

You can use these prompts by either:

1. **Copy-pasting the content:**
   View the content of the desired prompt file (e.g., using `cat`) and paste it directly into your LLM CLI tool's prompt input.

   ```bash
   cat prompts/markdown/markdown_strict_prompt.txt
   # Copy the output and paste into your LLM CLI tool.
   gemini ask "PASTE_YOUR_PROMPT_HERE"
   ```

2. **Piping the content (if supported by your CLI tool):**
   Many modern LLM CLI tools support reading prompt content directly from a file or standard input.

   ```bash
   cat prompts/markdown/markdown_strict_prompt.txt | gemini generate --model gemini-1.5-flash
   # Or, if your CLI accepts a file path directly:
   gemini generate --model gemini-1.5-flash --prompt-file prompts/markdown/markdown_strict_prompt.txt
   ```

   > **Note**: Replace `gemini ask`, `gemini generate`, `--model`, and `--prompt-file` with the actual commands and flags of your specific LLM CLI tool. Refer to your CLI's official documentation for precise usage.

For more detailed instructions on using these prompts with specific CLI tools, please refer to `USAGE_INSTRUCTIONS.md`.

## Prerequisites

To effectively use the prompts in this repository, you will need:

- A configured and functional Large Language Model (LLM) CLI tool (e.g., [Google Gemini CLI](https://ai.google.dev/docs/gemini_api_overview), [Anthropic Claude CLI](https://docs.anthropic.com/claude/reference/claude-api)).
- Basic familiarity with using command-line interfaces.

## Contributing

We welcome contributions to expand and improve this Prompt Engineering Suite! If you have well-crafted prompts that enhance LLM output for common development tasks, please consider submitting a pull request.

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-prompt-name`).
3. Add your prompt(s) to an appropriate category, or create a new one.
4. Include a brief `README.md` within your new prompt directory explaining its purpose and usage.
5. Commit your changes (`git commit -m 'feat: Add new awesome prompt'`).
6. Push to the branch (`git push origin feature/your-prompt-name`).
7. Open a pull request with a clear description of your contribution.

## Repository Structure

```text
C:.
│   .gitignore
│   GEMINI.md
│   LICENSE
│   README.md
│   USAGE_INSTRUCTIONS.md
│
├───project-specific
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
