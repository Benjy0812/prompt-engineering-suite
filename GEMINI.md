# GEMINI.md - Project Context for AI Agent

This document provides context for the `ai-prompts` repository, which is a
non-code project focused on collecting and managing AI prompts.

## Directory Overview

The repository, named "Prompt Engineering Suite," is a curated collection of
text-based prompts designed to be used with large language models (LLMs) like
Gemini. The primary goal is to standardize the output for common development and
documentation tasks, such as generating Markdown files and Git commit messages.

The current directory structure is as follows:

- `CLI_INSTRUCTIONS.md`
- `GEMINI.md`
- `README.md`
- `prompts/git/global_commit_message_prompt.txt`
- `prompts/git/web-dev-commit/prompt.txt`
- `prompts/git/web-dev-commit/README.md`
- `prompts/markdown/markdown_relaxed_prompt.txt`
- `prompts/markdown/markdown_strict_prompt.txt`
- `prompts/markdown/README.md`

## Key Files

- **`README.md`**: The main `README` file serves as a comprehensive
  `markdownlint` style guide, defining the strict rules that generated Markdown
  should follow.

- **`prompts/git/global_commit_message_prompt.txt`**: A global prompt for generating Git commit messages, applicable to any project, and updated with examples relevant to this prompt engineering suite.
- **`prompts/git/web-dev-commit/prompt.txt`**: A prompt specifically for generating web development related commit messages.
- **`prompts/git/web-dev-commit/README.md`**: Explanation for the `web-dev-commit` prompt.

- **`prompts/markdown/markdown_strict_prompt.txt`**: A prompt that instructs
  the AI to act as an expert technical writer and generate Markdown that is
  fully compliant with a strict set of `markdownlint` rules. This is for
  producing clean, production-ready documentation.

- **`prompts/markdown/markdown_relaxed_prompt.txt`**: A prompt that also asks
  the AI to generate Markdown, but with a more flexible and relaxed set of
  rules, prioritizing readability over strict linting compliance.

- **`CLI_INSTRUCTIONS.md`**: This file contains the instructions for the AI agent
  itself, defining how it should analyze a directory and generate this
  `GEMINI.md` file.

## Usage

The prompts within this repository are intended to be copied from their
respective `.txt` files and used as instructional context for an AI model. The
user provides the prompt to the AI, follows any additional instructions within
the prompt (like providing context), and then uses the AI-generated output for
their specific task (e.g., writing a `README.md`, creating a Git commit).
