import keyboard
import re

def text_expander(text):
  """Expands text by replacing short forms with their expansions."""
  expansions = {
    "lol": "laugh out loud",
    "rofl": "rolling on the floor laughing",
    "wtf": "what the f*ck",
    "brb": "be right back",
    "ttyl": "talk to you later",
  }
  for short_form, expansion in expansions.items():
    text = re.sub(short_form, expansion, text)
  return text

def expand_text_as_you_type():
  """Expands text as you type."""
  expansions = {
    "lol": "laugh out loud",
    "rofl": "rolling on the floor laughing",
    "wtf": "what the f*ck",
    "brb": "be right back",
    "ttyl": "talk to you later",
  }
  for short_form, expansion in expansions.items():
    keyboard.add_abbreviation(short_form, expansion)

if __name__ == "__main__":
  expand_text_as_you_type()
  while True:
    text = input("Enter text: ")
    print(text_expander(text))
