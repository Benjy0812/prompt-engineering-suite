# Markdown Style Guide

This document outlines the standards for creating clean, consistent, and valid
Markdown files. Adhering to these guidelines ensures that our documentation is
readable, maintainable, and professional.

## Headings

- Heading levels must increment by one and should not be skipped.
- The document must contain only one top-level heading (`#`).
- Headings must start at the beginning of a line with a single space after the
  `#` characters.
- Do not add any trailing punctuation to headings.
- Ensure headings are unique to avoid confusion.
- Surround every heading with a single blank line.

## General Formatting

- Use spaces for indentation instead of hard tabs.
- Remove any trailing spaces from the end of lines.
- Avoid multiple consecutive blank lines.
- End every file with a single newline character.
- Wrap long lines of text to a reasonable length to improve readability.

## Lists

- Use a single, consistent marker for unordered lists (`-`).
- Use exactly one space after the dash for all list items.
- Indent list items consistently at the same level.
- Surround lists with a single blank line to separate them from other content.

## Emphasis and Text

- Use `*italic*` for italicized text and `**bold**` for bold text.
- Do not use emphasis as a substitute for headings.
- Avoid adding spaces inside emphasis markers.

## Links and Images

- Do not use bare URLs; always use proper link syntax:
  `[Descriptive Link Text](https://example.com)`.
- Link text should clearly describe the destination.
- All images must include descriptive alt text:
  `![Alt text for image](path/to/image.png)`.
- Use a consistent style for links, preferably inline.
- Ensure all link fragments are valid.

## Code Blocks

- Use fenced code blocks only; do not use indented code blocks.
- Always specify a language for the block (e.g., `javascript`, `python`).
- If no language is obvious, such as for plain text or pseudocode, use `text`.
- Surround every fenced code block with blank lines.
- Use triple backticks (```) consistently as the fence style.
- Do not include spaces inside `inline code` spans.

```markdown
# Example Heading

This is a paragraph.

- List item one
- List item two

This is some **bold** and *italic* text.

```javascript
function greet() {
  console.log("Hello, World!");
}
```
```

## Tables

- Surround tables with blank lines.
- Ensure column counts are consistent across all rows.
- Align content within columns consistently using pipes (`|`).

```markdown
| Header 1 | Header 2 |
| :--- | :--- |
| Cell 1 | Cell 2 |
| Cell 3 | Cell 4 |
```

## Blockquotes

- Use a single space after the `>` character.
- Do not include blank lines within a single blockquote.

```markdown
> This is a correctly formatted blockquote.
```

## Naming Conventions

- Use correct capitalization for proper names and technologies.
- Examples: GitHub, Markdown, Node.js, JavaScript.

