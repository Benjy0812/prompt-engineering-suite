# CLI Instructions for Using Prompts

This guide provides instructions on how to effectively use the prompts from this
repository with command-line interface (CLI) tools, specifically focusing on
Gemini CLI and Claude Code CLI.

## General Usage

Most prompts in this repository are designed to be copied and pasted directly
into your AI assistant's input. For CLI usage, you can either:

1.  **Copy-paste**: Read the content of the prompt file (e.g.,
    `cat git/web-dev-commit/prompt.txt`) and paste it into your CLI tool's
    prompt input.
2.  **Pipe content**: If your CLI tool supports reading from standard input or a
    file, you can pipe the prompt content directly.

## Using with Gemini CLI

Assuming you have a Gemini CLI tool set up and configured, here are some general
ways to use these prompts:

### Method 1: Direct Input (Copy-paste)

1.  View the prompt content:

    ```bash
    cat git/web-dev-commit/prompt.txt
    ```

2.  Copy the output.
3.  Execute your Gemini command and paste the prompt when requested, or pass it
    as an argument if your CLI supports it:

    ```bash
    gemini ask "PASTE_YOUR_PROMPT_HERE"
    # Or
    gemini chat
    # Then paste the prompt into the interactive session.
    ```

### Method 2: Piped Input (If supported)

If your Gemini CLI tool can read a prompt from a file or standard input:

```bash
cat git/web-dev-commit/prompt.txt | gemini generate --model gemini-1.5-flash
# Or, if it accepts a file path
gemini generate --model gemini-1.5-flash --prompt-file git/web-dev-commit/prompt.txt
```

> **Note**: Replace `gemini generate` and `--prompt-file` with the actual
> commands and flags of your Gemini CLI.

## Using with Claude Code CLI

Similarly, for a Claude Code CLI tool:

### Method 1: Direct Input (Copy-paste)

1.  View the prompt content:

    ```bash
    cat git/web-dev-commit/prompt.txt
    ```

2.  Copy the output.
3.  Execute your Claude Code command and paste the prompt:

    ```bash
    claude-code chat "PASTE_YOUR_PROMPT_HERE"
    # Or, if it has an interactive mode
    claude-code interactive
    # Then paste the prompt into the interactive session.
    ```

### Method 2: Piped Input (If supported)

If your Claude Code CLI tool can read a prompt from a file or standard input:

```bash
cat git/web-dev-commit/prompt.txt | claude-code query --model claude-3-opus-20240229
# Or, if it accepts a file path
claude-code query --model claude-3-opus-20240229 --file git/web-dev-commit/prompt.txt
```

> **Note**: Replace `claude-code query` and `--file` with the actual commands
> and flags of your Claude Code CLI.

---

> **Important**: Always refer to the official documentation for your specific
> Gemini CLI and Claude Code CLI implementations for the most accurate and
> up-to-date usage instructions.
