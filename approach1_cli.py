#!/usr/bin/env python3
"""
Approach 1: Traditional Python CLI
Demonstrates OpenClaw's ability to create clean, documented CLI tools.
"""

import argparse
import sys
from datetime import datetime
from typing import Optional


class HelloWorldCLI:
    """A classic CLI implementation showing OpenClaw's coding style."""
    
    def __init__(self, name: Optional[str] = None):
        self.name = name or "World"
        self.timestamp = datetime.now().isoformat()
    
    def greet(self) -> str:
        """Generate personalized greeting."""
        return f"Hello {self.name}! from OpenClaw at {self.timestamp}"
    
    def run(self, output_format: str = "text") -> None:
        """Execute the greeting with optional formatting."""
        greeting = self.greet()
        
        if output_format == "json":
            import json
            result = {
                "greeting": f"Hello {self.name}!",
                "source": "OpenClaw",
                "timestamp": self.timestamp,
                "approach": "Traditional Python CLI"
            }
            print(json.dumps(result, indent=2))
        elif output_format == "yaml":
            try:
                import yaml
                result = {
                    "greeting": f"Hello {self.name}!",
                    "source": "OpenClaw",
                    "timestamp": self.timestamp,
                    "approach": "Traditional Python CLI"
                }
                print(yaml.dump(result, default_flow_style=False))
            except ImportError:
                print("YAML output requires PyYAML. Install with: pip install pyyaml")
                print(greeting)
        else:
            print(greeting)


def main():
    """Command-line interface entry point."""
    parser = argparse.ArgumentParser(
        description="OpenClaw Hello World - Approach 1: Traditional CLI",
        epilog="Example: python approach1_cli.py --name Mykie --format json"
    )
    
    parser.add_argument(
        "--name", "-n",
        default="World",
        help="Name to greet (default: World)"
    )
    
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json", "yaml"],
        default="text",
        help="Output format (default: text)"
    )
    
    parser.add_argument(
        "--version", "-v",
        action="version",
        version="OpenClaw Hello World v1.0.0"
    )
    
    args = parser.parse_args()
    
    # Create and run the CLI
    cli = HelloWorldCLI(name=args.name)
    cli.run(output_format=args.format)


if __name__ == "__main__":
    main()