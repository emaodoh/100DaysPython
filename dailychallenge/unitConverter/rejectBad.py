# Reject Bad Input
# Instructions

# Write a function called `solution` that safely converts a value to a number and doubles it.

# If the value can be converted to a number, return the doubled value rounded to 2 decimal places.

# If the value cannot be converted to a number, return this exact string:

# Invalid number

# Rules:
# - Use `float()` inside a `try` block.
# - Use `except ValueError` to catch bad input.
# - Return "Invalid number" for bad input.
# - Do not print.
# - Do not ask for input.

# This challenge matches the Day 2 safe parsing idea: ask, attempt to convert, handle failure, and continue without crashing.

def solution(value):
    try:
        value = float(value)
    except ValueError:
        return "Invalid number"
    num = value * 2
    return round(num, 2)
