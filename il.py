# Copyright (c) 2025 iiPython

# Modules
from typing import Optional

# Version
__version__ = "0.1.0"

# Begin methods
@staticmethod
def cprint(text: str, color: int) -> None:
    """Generate a line of colored text; yes, that's all it does."""
    print(f"\033[{color}m{text}")

@staticmethod
def box(size: int, left: str, right: str, color: int = 34) -> None:
    """Generate a box (header) of the given size, text, and color.
    Ensure you include the sides (2 characters) in your size, as they will be subtracted."""
    size -= 2  # Account for sides
    print(f"\033[{color}m┌{'─' * size}┐")
    print(f"│ {left}{' ' * (size - 2 - len(left) - len(right))}{right} │")
    print(f"└{'─' * size}┘")

@staticmethod
def rule(size: int, color: int = 34) -> None:
    """Generate a horizontal rule given size and color."""
    cprint("─" * size, color)

@staticmethod
def indent(text: str, color: int = 34, indent: int = 2) -> None:
    """Generate a line of indented text, meant to sit between horizontal rules."""
    cprint(f"{' ' * indent}{text}", color)

@staticmethod
def request(
    path: str,
    remote_ip: str,
    summary: str,
    summary_color: int,
    time_taken_seconds: float | int,
    detail_text: Optional[str] = None,
    verb: Optional[str] = "REQ"
) -> None:
    """Generate a log given request parameters."""
    total_time = time_taken_seconds * 1000
    spacing = " " * (len(path) - len(summary))  # This should have 2 subtracted, but for now it's tab aligned

    print(f"\033[33m\u26A1 {verb} {path}\t[{remote_ip}]")
    if detail_text is not None:
        print(f"\033[90m   │   \033[{summary_color}m{detail_text}")

    print(f"\033[90m   └→  \033[{summary_color}m{summary}{spacing}\t\033[33m[{total_time:.1f}ms]")
