#!/usr/bin/env python3
"""
OpenClaw ASCII Art Animated Greeting
Pure Python stdlib -- no dependencies.
"""
import sys
import time

# ANSI color codes for rainbow gradient
COLORS = [
    "\033[38;5;196m",  # red
    "\033[38;5;202m",  # orange
    "\033[38;5;208m",  # dark orange
    "\033[38;5;214m",  # gold
    "\033[38;5;220m",  # yellow
    "\033[38;5;226m",  # bright yellow
    "\033[38;5;118m",  # lime
    "\033[38;5;46m",   # green
    "\033[38;5;48m",   # spring green
    "\033[38;5;51m",   # cyan
    "\033[38;5;45m",   # sky blue
    "\033[38;5;39m",   # dodger blue
    "\033[38;5;33m",   # blue
    "\033[38;5;63m",   # slate blue
    "\033[38;5;129m",  # purple
    "\033[38;5;165m",  # magenta
    "\033[38;5;201m",  # hot pink
]
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

BANNER = [
    r"  ___  ____  _____ _   _  ____ _        _ __        __",
    r" / _ \|  _ \| ____| \ | |/ ___| |      / \\ \      / /",
    r"| | | | |_) |  _| |  \| | |   | |     / _ \\ \ /\ / / ",
    r"| |_| |  __/| |___| |\  | |___| |___ / ___ \\ V  V /  ",
    r" \___/|_|   |_____|_| \_|\____|_____/_/   \_\\_/\_/   ",
]

CLAW = [
    r"        ,     ,",
    r"       (\____/)",
    r"        (_oo_)",
    r"          (O)",
    r"        __||__    \)",
    r"     []/______\[] /",
    r"     / \______/ \/",
    r"    /    /__\       ",
    r"   (\   /____\     ",
]

TOP_BORDER    = "+" + "=" * 60 + "+"
BOTTOM_BORDER = "+" + "=" * 60 + "+"
SIDE          = "|"

TAGLINE = "Self-improving since 2026"
SUBTITLE = "~ Intent-driven iteration engine ~"


def colorize_char(ch, idx):
    """Apply rainbow color based on character position."""
    if ch == " ":
        return ch
    color = COLORS[idx % len(COLORS)]
    return f"{color}{ch}{RESET}"


def colorize_line(line, row_offset=0):
    """Apply rainbow gradient across a full line."""
    return "".join(colorize_char(ch, i + row_offset) for i, ch in enumerate(line))


def type_effect(text, delay=0.008):
    """Print text character by character with a typing delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def center(text, width=58):
    """Center text within a given width."""
    padding = max(0, width - len(text))
    left = padding // 2
    right = padding - left
    return " " * left + text + " " * right


def print_framed_line(content, width=58):
    """Print a line inside the box frame."""
    padded = content.ljust(width)[:width]
    sys.stdout.write(f"{DIM}{SIDE}{RESET} {padded} {DIM}{SIDE}{RESET}\n")
    sys.stdout.flush()


def main():
    delay = 0.008
    fast = "--fast" in sys.argv or "--test" in sys.argv
    if fast:
        delay = 0

    # Top border with typing effect
    type_effect(f"{BOLD}{COLORS[3]}{TOP_BORDER}{RESET}", delay=delay * 0.5)

    # Empty line
    print_framed_line("")
    time.sleep(delay * 5)

    # Claw art
    for i, line in enumerate(CLAW):
        colored = colorize_line(center(line), row_offset=i * 3)
        visible_len = len(center(line))
        actual_len = len(colored)
        extra = actual_len - visible_len
        framed = f"{DIM}{SIDE}{RESET} {colored.ljust(58 + extra)} {DIM}{SIDE}{RESET}"
        sys.stdout.write(framed + "\n")
        sys.stdout.flush()
        time.sleep(delay * 8)

    print_framed_line("")
    time.sleep(delay * 5)

    # Separator
    sep = f"{COLORS[10]}{'-' * 58}{RESET}"
    sys.stdout.write(f"{DIM}{SIDE}{RESET} {sep} {DIM}{SIDE}{RESET}\n")
    sys.stdout.flush()
    time.sleep(delay * 10)

    print_framed_line("")

    # Big OPENCLAW banner
    for i, line in enumerate(BANNER):
        colored = colorize_line(center(line), row_offset=i * 7)
        visible_len = len(center(line))
        actual_len = len(colored)
        extra = actual_len - visible_len
        framed = f"{DIM}{SIDE}{RESET} {colored.ljust(58 + extra)} {DIM}{SIDE}{RESET}"
        sys.stdout.write(framed + "\n")
        sys.stdout.flush()
        time.sleep(delay * 12)

    print_framed_line("")
    time.sleep(delay * 5)

    # Separator
    sys.stdout.write(f"{DIM}{SIDE}{RESET} {sep} {DIM}{SIDE}{RESET}\n")
    sys.stdout.flush()
    time.sleep(delay * 10)

    print_framed_line("")

    # Tagline with rainbow
    tag_centered = center(TAGLINE)
    tag_colored = colorize_line(tag_centered, row_offset=42)
    tag_visible = len(tag_centered)
    tag_extra = len(tag_colored) - tag_visible
    line_content = f"{BOLD}{tag_colored}{RESET}"
    sys.stdout.write(f"{DIM}{SIDE}{RESET} {line_content.ljust(58 + tag_extra + len(BOLD) + len(RESET))} {DIM}{SIDE}{RESET}\n")
    sys.stdout.flush()
    time.sleep(delay * 15)

    # Subtitle
    sub_centered = center(SUBTITLE)
    sub_colored = f"{DIM}{COLORS[11]}{sub_centered}{RESET}"
    sub_extra = len(sub_colored) - len(sub_centered)
    sys.stdout.write(f"{DIM}{SIDE}{RESET} {sub_colored.ljust(58 + sub_extra)} {DIM}{SIDE}{RESET}\n")
    sys.stdout.flush()
    time.sleep(delay * 10)

    print_framed_line("")

    # Bottom border
    type_effect(f"{BOLD}{COLORS[3]}{BOTTOM_BORDER}{RESET}", delay=delay * 0.5)

    # Final newline
    print()


if __name__ == "__main__":
    main()
