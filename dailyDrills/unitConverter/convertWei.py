# Convert Weight
# Instructions

# Write a function called `solution` that converts kilograms to grams and pounds.

# The function receives one value, `kilograms`, and must return a three-line report in this exact format:

# Kilograms: <kilograms>
# Grams: <grams>
# Pounds: <pounds>

# Rules:
# - Convert the input to a number using `float()`.
# - 1 kilogram = 1000 grams.
# - 1 kilogram = 2.20462 pounds.
# - Round pounds to 2 decimal places.
# - Return the final multi-line string.
# - Do not print.

def solution(kilograms):
    kilograms = float(kilograms)

    grams = kilograms * 1000
    pounds = kilograms * 2.20462

    return f"Kilograms: {kilograms}\nGrams: {grams}\nPounds: {round(pounds, 2)}"
