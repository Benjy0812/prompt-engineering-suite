# [SYSTEM_CONTEXT: ai-prompts]

## [IDENTITY_LOGIC]
- **Repository**: `ai-prompts` (Prompt Engineering Suite)
- **Ruleset**: Strictly follows `README.md` (Markdownlint standards).
- **Core Rule**: Exactly 1 space after list markers (`- Item`) per MD030.

## [OPERATIONAL_FLOW]
1. **Locate**: Identify the correct prompt file by navigating the repository structure.
2. **Load**: Read the corresponding `.md` file (e.g., `generate-commit-message.md`) for specific instructions.
3. **Output**: Return raw content or generated code only. Zero conversational filler.