#!/usr/bin/env python3
"""
Tests for Approach 1: Traditional CLI
"""

import subprocess
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_cli_basic():
    """Test basic CLI functionality."""
    result = subprocess.run(
        [sys.executable, "approach1_cli.py"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    assert "Hello World!" in result.stdout
    assert "OpenClaw" in result.stdout


def test_cli_with_name():
    """Test CLI with custom name."""
    result = subprocess.run(
        [sys.executable, "approach1_cli.py", "--name", "Mykie"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    assert "Hello Mykie!" in result.stdout


def test_cli_json_output():
    """Test JSON output format."""
    result = subprocess.run(
        [sys.executable, "approach1_cli.py", "--format", "json", "--name", "Test"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    
    # Parse JSON output
    data = json.loads(result.stdout)
    assert data["greeting"] == "Hello Test!"
    assert data["source"] == "OpenClaw"
    assert "timestamp" in data
    assert data["approach"] == "Traditional Python CLI"


def test_cli_help():
    """Test help output."""
    result = subprocess.run(
        [sys.executable, "approach1_cli.py", "--help"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    assert "OpenClaw Hello World" in result.stdout
    assert "--name" in result.stdout
    assert "--format" in result.stdout


def test_cli_version():
    """Test version output."""
    result = subprocess.run(
        [sys.executable, "approach1_cli.py", "--version"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    assert result.returncode == 0
    assert "OpenClaw Hello World v1.0.0" in result.stdout


if __name__ == "__main__":
    # Run tests manually if needed
    test_cli_basic()
    test_cli_with_name()
    test_cli_json_output()
    test_cli_help()
    test_cli_version()
    print("✅ All CLI tests passed!")