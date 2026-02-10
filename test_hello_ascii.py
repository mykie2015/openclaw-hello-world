#!/usr/bin/env python3
"""
Tests for hello_ascii.py — OpenClaw ASCII art greeting.
Uses unittest (stdlib only, no pytest).
"""
import os
import subprocess
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(SCRIPT_DIR, "hello_ascii.py")


class TestHelloAscii(unittest.TestCase):
    """Test suite for the ASCII art greeting script."""

    def _run_script(self):
        """Helper: run hello_ascii.py with --test flag (disables delays)."""
        result = subprocess.run(
            ["python3", SCRIPT_PATH, "--test"],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=SCRIPT_DIR,
        )
        return result

    def test_exits_cleanly(self):
        """Script should exit with return code 0."""
        result = self._run_script()
        self.assertEqual(
            result.returncode,
            0,
            f"Script exited with code {result.returncode}.\n"
            f"stderr: {result.stderr}",
        )

    def test_output_contains_openclaw(self):
        """Output must contain OPENCLAW banner and tagline."""
        result = self._run_script()
        import re
        clean = re.sub(r"\033\[[0-9;]*m", "", result.stdout)
        self.assertIn(
            "SELF-IMPROVING SINCE 2026",
            clean.upper(),
            "Output does not contain tagline.",
        )
        # ASCII art banner contains the figlet-style OPENCLAW letters
        self.assertIn("____", clean, "Output does not contain ASCII art banner.")

    def test_output_contains_ansi_codes(self):
        """Output must contain ANSI escape sequences for color."""
        result = self._run_script()
        self.assertIn(
            "\033[",
            result.stdout,
            "Output does not contain ANSI escape codes.",
        )


if __name__ == "__main__":
    unittest.main()
