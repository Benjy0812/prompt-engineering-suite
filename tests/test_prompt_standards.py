import os
import re
import unittest

class TestPromptStandards(unittest.TestCase):
    PROMPT_DIR = 'prompts'
    REQUIRED_HEADINGS = ['## Role', '## Task', '## Constraints', '## Output Format']
    PLACEHOLDER_REGEX = r'\{\{[A-Z_]+\}\}'

    def get_prompts(self):
        prompts = []
        for root, dirs, files in os.walk(self.PROMPT_DIR):
            for file in files:
                if file.endswith('.md') and not file.endswith('.README.md'):
                    prompts.append(os.path.join(root, file))
        return prompts

    def test_readme_exists(self):
        """Every prompt MUST have a corresponding [name].README.md file."""
        prompts = self.get_prompts()
        for prompt_path in prompts:
            readme_path = prompt_path.replace('.md', '.README.md')
            with self.subTest(prompt=prompt_path):
                self.assertTrue(os.path.exists(readme_path), f"Missing README for {prompt_path}")

    def test_required_headings(self):
        """All prompts MUST follow the structure: Role, Task, Constraints, Output Format."""
        prompts = self.get_prompts()
        for prompt_path in prompts:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                content = f.read()
            with self.subTest(prompt=prompt_path):
                for heading in self.REQUIRED_HEADINGS:
                    if heading not in content:
                        self.fail(f"Missing heading '{heading}' in {prompt_path}")

    def test_placeholder_syntax(self):
        """All prompts MUST use the unified placeholder syntax (e.g., {{CODE}})."""
        # This test checks if there are any old-style placeholders like [PLACEHOLDER] or <PLACEHOLDER>
        # that should be converted to {{PLACEHOLDER}}.
        # For now, let's just check if it contains at least one {{PLACEHOLDER}} if it has any placeholders.
        # More specifically, let's look for common old patterns.
        prompts = self.get_prompts()
        old_syntax_patterns = [
            r'\[[A-Z_]+\]',  # [VAR]
            r'<[A-Z_]+>',    # <VAR>
        ]
        
        for prompt_path in prompts:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                content = f.read()
            with self.subTest(prompt=prompt_path):
                found_old_syntax = any(re.search(pattern, content) for pattern in old_syntax_patterns)
                if found_old_syntax:
                    self.fail(f"Old placeholder syntax found in {prompt_path}")
