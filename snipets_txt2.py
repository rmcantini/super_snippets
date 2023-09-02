import re
import pyperclip
import keyboard


def expand_text_as_you_type():
    """Expands text as you type."""


mentions = "raphaela.monteiro", "paati"

expansions = {
    "lol": "laugh out loud",
    "rofl": "rolling on the floor laughing",
    "wtf": "what the f*ck",
    "lo": "¯\_(ツ)_/¯",
    # "eu": add_keystroke,
}


for short_form, expansion in expansions.items():
    keyboard.add_abbreviation(short_form, expansion)

while True:
    text = input("Enter text: ")
    print(text)


def put_text_into_clipboard(text):
    """Puts text into the clipboard."""
    pyperclip.copy(text)


if __name__ == "__main__":
    text = "@raphaela.monteiro @Patricia Fuhrmann Botelho @Anne Luyse Boeck"
    put_text_into_clipboard(text)


def add_keystroke():
    """Adds a keystroke."""
    keyboard.press("shift")
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    keyboard.release("shift")


if __name__ == "__main__":
    add_keystroke()
