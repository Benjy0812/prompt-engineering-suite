import os
import subprocess
import unittest

class TestLinting(unittest.TestCase):
    def test_prettier_config_exists(self):
        """Prettier configuration file should exist."""
        self.assertTrue(os.path.exists('.prettierrc'), ".prettierrc not found")

    def test_prettier_check(self):
        """All files should be formatted with Prettier."""
        try:
            result = subprocess.run(
                ['npx', 'prettier', '--check', '.'],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0, f"Prettier check failed:\n{result.stdout}\n{result.stderr}")
        except FileNotFoundError:
            self.fail("npx or prettier not found")

if __name__ == '__main__':
    unittest.main()

