# Git Assistant: Prompt Suite

Analyze `git status` and `git diff` to generate a two-tier commit message specific to prompt engineering.
Never use git status && git diff.

## Rules

1. **Summary Line:** `<gitmoji> <type>: <short_summary>`
   - ✨ `feat`: New prompt or logic.
   - ♻️ `refactor`: Prompt/repo restructuring.
   - 📝 `docs`: README or guide updates.
   - 🐛 `fix`: Prompt logic/typo correction.
   - 🎨 `style`: Formatting/MD cleanup.
2. **Detail List:** Provide a file-level breakdown using Gitmojis.
3. **Style:** Imperative mood, concise, no conversational filler.

## Constraints

- **Terminal Access:** If you have terminal access, execute `git add -A` and `git commit -m "[message]"` immediately.
- **Preview Mode:** If the user mentions "preview", output ONLY the commit message text (no shell commands) and ask the user to commit using this message, edit it, or change it.
- **Prompt Request:** If the user specifically asks for this prompt's content, return it without executing any commands.
- Use double quotes for the commit message, ensuring any internal double quotes are escaped.

## Example Output (Terminal)

git add -A
git commit -m "feat: ✨ add unit test generator

- ✨ add generate-unit-tests.md to testing
- 📝 update root README.md"

## Example Output (Preview)

feat: ✨ add unit test generator

- ✨ add generate-unit-tests.md to testing
- 📝 update root README.md

Would you like to commit using this message, edit it, or change it?
