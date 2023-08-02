import keyboard
import re

def read_expansions_from_file(file_name):
  """Reads the expansions from a file."""
  with open(file_name, "r") as f:
    expansions = f.read()
  expansions = expansions.split("\n")
  return expansions

expansions = read_expansions_from_file("expansions.txt")

for expansion in expansions:
  short_form, expansion = expansion.split(":")
  keyboard.add_abbreviation(short_form, expansion)
