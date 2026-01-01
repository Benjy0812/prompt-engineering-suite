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
- **Automation**: Use `project-specific` tools to maintain and grow this library.
- **Standards**: Use `markdown-strict` for documentation to ensure zero linting errors.

---

## Directory Tree

```text
C:.
│   .gitignore
│   GEMINI.md
│   LICENSE
│   README.md
│   USAGE_INSTRUCTIONS.md
│
├───.vscode
│       settings.json
│
├───project-specific
│   ├───generate-commit-message
│   │       prompt.md
│   │       README.md
│   │
│   └───generate-prompt
│           prompt.md
│           README.md
│
└───prompts
    ├───code
    │   └───explain-code
    │           prompt.md
    │           README.md
    │
    ├───git
    │   ├───global-commit
    │   │       prompt.md
    │   │       README.md
    │   │
    │   └───web-dev-commit
    │           prompt.md
    │           README.md
    │
    ├───iac
    │   └───generate-dockerfile
    │           prompt.md
    │           README.md
    │
    ├───markdown
    │   ├───markdown-relaxed
    │   │       prompt.md
    │   │       README.md
    │   │
    │   └───markdown-strict
    │           prompt.md
    │           README.md
    │
    ├───refactoring
    │   └───suggest-improvements
    │           prompt.md
    │           README.md
    │
    └───testing
        └───generate-unit-tests
                prompt.md
                README.md
```
