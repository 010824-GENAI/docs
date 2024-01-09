"""
Regular Expression is a sequence of characters that defines a search pattern. It is used for matching and manipulating strings, typically within text or character data. Regular expressions provide a flexible and efficient way to search, match, and manipulate text based on certain patterns.
"""
import re

text = "In a deep dark forest, there are 10 wolves, 2 bears, and 1 bunny who ruled them all."
# Literals
# r in front of the string stands for raw string, it will not escape any characters
pattern = r"bunny"
# Match vs Search
print("search", re.search(pattern, text))

# Match expects the text to "start" with the pattern
print("match", re.match(pattern, text))

# Character Classes
pattern = r"[aeiou]"

# Special characters that stands for certain character classes
# \w = matches all alphanumeric character [A-Za-z0-9]
# \W = not \w
# \d = all digits
# \D = not \d

pattern = r"\w"
print(re.findall(pattern, text))

pattern = r"bunny"
replace = "cat"

print(re.sub(pattern, replace, text))
# Quantifiers
# ^ $ + * {}
# ^: means look at the beginning of the text
# $: means this pattern must be at the end of the text
pattern = "bunny"
print(re.search(pattern, text))

phone_pattern = r"\d{3}-\d{3}-\d{4}"
phone_text = "my phone number is 234-238-4383"
print(re.search(phone_pattern, phone_text))
