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
            # Check if npx and prettier are available
            subprocess.run(['npx', '--version'], check=True, capture_output=True, text=True)
            subprocess.run(['prettier', '--version'], check=True, capture_output=True, text=True)

            result = subprocess.run(
                ['npx', 'prettier', '--check', '.'],
                capture_output=True,
                text=True
            )
            self.assertEqual(result.returncode, 0, f"Prettier check failed:\n{result.stdout}\n{result.stderr}")

        except FileNotFoundError:
            self.fail("npx or prettier not found")

        except subprocess.CalledProcessError as e:
            if 'No files were changed' in e.output:
                print("All files are already formatted with Prettier.")
            else:
                raise
