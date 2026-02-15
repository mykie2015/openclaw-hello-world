"""Tests for hello.py — validates the iteration loop works end-to-end."""
import subprocess
import sys
import unittest


class TestHello(unittest.TestCase):
    def run_hello(self):
        return subprocess.run(
            [sys.executable, "hello.py"],
            capture_output=True,
            text=True,
            cwd="/home/node/repos/hello-world-validation",
        )

    def test_output_contains_greeting(self):
        result = self.run_hello()
        self.assertIn("Hello from OpenClaw!", result.stdout)

    def test_exits_cleanly(self):
        result = self.run_hello()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
