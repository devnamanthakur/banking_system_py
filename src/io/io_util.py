import os
from typing import Optional


def clear_screen() -> None:
    """Clears the terminal screen."""
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For macOS and Linux
    else:
        _ = os.system("clear")


def get_input_string(prompt: str) -> str:
    """
    Prompts the user for input and returns it as a trimmed string.

    Args:
        prompt: The message to display to the user.

    Returns:
        The user's input, stripped of leading/trailing whitespace.
    """
    return input(prompt).strip()


def get_input_int(prompt: str) -> Optional[int]:
    """
    Prompts the user for an integer input and parses it.

    Args:
        prompt: The message to display to the user.

    Returns:
        The parsed integer on success, None otherwise.
    """
    try:
        return int(get_input_string(prompt))
    except ValueError:
        return None


def get_input_float(prompt: str) -> Optional[float]:
    """
    Prompts the user for a float input and parses it.

    Args:
        prompt: The message to display to the user.

    Returns:
        The parsed float on success, None otherwise.
    """
    try:
        return float(get_input_string(prompt))
    except ValueError:
        return None


def press_enter_to_continue() -> None:
    """Pauses the program until the user presses Enter."""
    input("\nPress Enter to continue...")
