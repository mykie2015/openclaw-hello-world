"""Tests for hello_web.html - OpenClaw interactive web greeting."""
import os
import unittest

REPO_DIR = "/home/node/repos/hello-world-validation"
HTML_FILE = os.path.join(REPO_DIR, "hello_web.html")


class TestHelloWebExists(unittest.TestCase):
    """Test that the HTML file exists and is non-empty."""

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(HTML_FILE), f"{HTML_FILE} does not exist")

    def test_file_not_empty(self):
        size = os.path.getsize(HTML_FILE)
        self.assertGreater(size, 0, "hello_web.html is empty")


class TestHelloWebContent(unittest.TestCase):
    """Test that the HTML contains required interactive elements."""

    @classmethod
    def setUpClass(cls):
        with open(HTML_FILE, "r", encoding="utf-8") as f:
            cls.html = f.read()

    def test_has_canvas_element(self):
        self.assertIn("<canvas", self.html, "Missing <canvas> element for animation")

    def test_has_openclaw_text(self):
        self.assertIn("OPENCLAW", self.html, "Missing OPENCLAW text")

    def test_has_subtitle(self):
        self.assertIn("Self-improving since 2026", self.html, "Missing subtitle text")


class TestHelloWebStructure(unittest.TestCase):
    """Test that the HTML has valid structure."""

    @classmethod
    def setUpClass(cls):
        with open(HTML_FILE, "r", encoding="utf-8") as f:
            cls.html = f.read().lower()

    def test_has_html_tag(self):
        self.assertIn("<html", self.html, "Missing <html> tag")

    def test_has_head_tag(self):
        self.assertIn("<head>", self.html, "Missing <head> tag")
        self.assertIn("</head>", self.html, "Missing </head> tag")

    def test_has_body_tag(self):
        self.assertIn("<body>", self.html, "Missing <body> tag")
        self.assertIn("</body>", self.html, "Missing </body> tag")

    def test_has_doctype(self):
        self.assertTrue(self.html.strip().startswith("<!doctype html"), "Missing DOCTYPE")


if __name__ == "__main__":
    unittest.main()
