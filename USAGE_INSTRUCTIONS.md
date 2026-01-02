# Usage Guide

## Quick Start

1. **Select**: Find the target prompt folder in the tree below.
2. **Read**: Open the `prompt.md` file within that folder.
3. **Use**: Copy the content into your AI chat or use it via CLI.

## CLI Usage

```bash
# Pipe content directly to your tool
cat prompts/git/web-dev-commit/prompt.md | ai-tool "your query"

# Use as a file argument (if supported)
ai-tool --prompt prompts/git/web-dev-commit/prompt.md
```

## Workflow Integration

- **Shell Aliases**: Map frequent prompts to shell commands for instant access.
- **Automation**: Use `maintenance` tools to maintain and grow this library.

---

## Directory Tree

```text
C:.
│   CONTRIBUTING.md
│   GEMINI.md
│   LICENSE.md
│   README.md
│   USAGE_INSTRUCTIONS.md
│
├───maintenance
│       generate-commit-message.md
│       generate-commit-message.README.md
│       generate-prompt.md
│       generate-prompt.README.md
│
└───prompts
    ├───code
    │       explain-code.md
    │       explain-code.README.md
    │
    ├───git
    │       global-commit.md
    │       global-commit.README.md
    │       web-dev-commit.md
    │       web-dev-commit.README.md
    │
    ├───iac
    │       generate-dockerfile.md
    │       generate-dockerfile.README.md
    │
    ├───markdown
    │       markdown-relaxed.md
    │       markdown-relaxed.README.md
    │       markdown-strict.md
    │       markdown-strict.README.md
    │
    ├───refactoring
    │       suggest-improvements.md
    │       suggest-improvements.README.md
    │
    └───testing
            generate-unit-tests.md
            generate-unit-tests.README.md
```
