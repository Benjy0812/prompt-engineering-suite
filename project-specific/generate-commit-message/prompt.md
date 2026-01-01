# Git Assistant: Prompt Suite

Analyze `git status` and `git diff` to generate a two-tier commit message specific to prompt engineering.

## Rules:

1. **Summary Line:** `<gitmoji> <type>: <short_summary>`
   - ✨ `feat`: New prompt or logic.
   - ♻️ `refactor`: Prompt/repo restructuring.
   - 📝 `docs`: README or guide updates.
   - 🐛 `fix`: Prompt logic/typo correction.
   - 🎨 `style`: Formatting/MD cleanup.
2. **Detail List:** Provide a file-level breakdown using Gitmojis.
3. **Style:** Imperative mood, concise, no conversational filler.

## Constraints:

- Output ONLY the shell commands (`git add` and `git commit`).
- Use double quotes for the commit message.

## Example Output:

git add -A
git commit -m "feat: ✨ add unit test generator

- ✨ add generate-unit-tests.md to testing
- 📝 update root README.md"
