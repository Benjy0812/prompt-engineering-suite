# [SYSTEM_CONTEXT: ai-prompts]

## [IDENTITY_LOGIC]

- **Repository**: `ai-prompts` (Prompt Engineering Suite)

## [OPERATIONAL_FLOW]

1. **Locate**: Identify the correct prompt file by navigating the repository structure.
2. **Load**: Read the corresponding `.md` file (e.g., `generate-commit-message.md`) for specific instructions.
3. **Output**: Return raw content or generated code only. Zero conversational filler.

## [SHELL_COMMAND_GUIDELINES]

- **Single Commands**: NEVER use `&&` or other operators to combine multiple commands in a single `run_shell_command` tool call. Always use separate tool calls for independent actions.
