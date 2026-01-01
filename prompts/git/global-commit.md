# Global Git Agent

Analyze `git status` and `git diff` to generate a professional Conventional Commit.

## Execution Rules

1. **Format:** `<type>(<scope>): <gitmoji> <summary>`
2. **Types:** feat (✨), fix (🐛), docs (📝), style (🎨), refactor (♻️), test (✅), chore (🔧), perf (⚡), build (📦), ci (🤖).
3. **Standards:** Imperative mood. Summary ≤ 50 chars. Body wrap at 72 chars.
4. **Staging:** Use `git add -A` unless specific files are identified in the diff.

## Constraints

- Output ONLY a single code block with shell commands.
- Use double quotes for the commit message.
- NO conversational filler.

## Example Output

git add -A
git commit -m "feat(auth): ✨ implement JWT refresh token logic"
