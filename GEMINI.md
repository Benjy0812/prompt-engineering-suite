# GEMINI.md - Project Context for AI Agent

This document provides context for the `ai-prompts` repository, which is a
non-code project focused on collecting and managing AI prompts.

## Directory Overview

The repository, named "Prompt Engineering Suite," is a curated collection of
text-based prompts designed to be used with large language models (LLMs) like
Gemini. The primary goal is to standardize the output for common development and
documentation tasks, such as generating Markdown files and Git commit messages.

The core content is located in the `git/commit-prompts/` directory. There is
also a legacy directory, `git/web-dev-commit/`, which contains an older version
of a commit prompt.

## Key Files

- **`README.md`**: The main `README` file serves as a comprehensive
  `markdownlint` style guide, defining the strict rules that generated Markdown
  should follow.

- **`git/commit-prompts/README.md`**: This `README` file explains the contents
  of the `commit-prompts` directory, which houses the main prompt collection. It
  details the different prompts available and their intended use cases.

- **`git/commit-prompts/markdown_strict_prompt.txt`**: A prompt that instructs
  the AI to act as an expert technical writer and generate Markdown that is
  fully compliant with a strict set of `markdownlint` rules. This is for
  producing clean, production-ready documentation.

- **`git/commit-prompts/markdown_relaxed_prompt.txt`**: A prompt that also asks
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
