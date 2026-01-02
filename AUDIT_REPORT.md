# Prompt Audit Report - 2026-01-02

## Overview

Existing prompts were audited against the standards defined in
`conductor/tracks/project_foundation_20260102/spec.md`.

## Standards Checked

1. **Structure:** MUST have headings: `## Role`, `## Task`, `## Constraints`,
   `## Output Format`.
2. **Placeholders:** MUST use `{{VAR}}` syntax.
3. **Documentation:** MUST have a corresponding `.README.md` file.

## Findings

### 1. Documentation (READMEs)

- **Status:** ✅ PASS
- All 8 existing prompts have corresponding `.README.md` files.

### 2. Placeholder Syntax

- **Status:** ✅ PASS
- No old-style `[VAR]` or `<VAR>` syntax was detected in the existing prompts.

### 3. Structure (Headings)

- **Status:** ❌ FAIL
- All 8 prompts are missing the standardized headings. They use varied heading
  structures (e.g., `## Identity`, `## Analysis Logic`, `## Core Directives`).

| Prompt Path                                   | Missing Headings                                           |
| --------------------------------------------- | ---------------------------------------------------------- |
| `prompts/code/explain-code.md`                | `## Role`, `## Task`, `## Output Format`                   |
| `prompts/git/global-commit.md`                | `## Role`, `## Task`, `## Output Format`                   |
| `prompts/git/web-dev-commit.md`               | `## Role`, `## Task`, `## Output Format`                   |
| `prompts/iac/generate-dockerfile.md`          | `## Role`, `## Task`, `## Output Format`                   |
| `prompts/markdown/markdown-relaxed.md`        | `## Role`, `## Task`, `## Constraints`, `## Output Format` |
| `prompts/markdown/markdown-strict.md`         | `## Role`, `## Task`, `## Constraints`, `## Output Format` |
| `prompts/refactoring/suggest-improvements.md` | `## Role`, `## Task`, `## Output Format`                   |
| `prompts/testing/generate-unit-tests.md`      | `## Role`, `## Task`, `## Output Format`                   |

## Next Steps

- Standardize all prompts to include the required headings during the
  implementation phases of the track.
