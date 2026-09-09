# Convert Length
# Instructions

# Write a function called `solution` that converts meters to centimeters and millimeters.

# The function receives one value, `meters`, and must return a two-line report in this exact format:

# Centimeters: <centimeters>
# Millimeters: <millimeters>

# Rules:
# - Convert the input to a number using `float()`.
# - 1 meter = 100 centimeters.
# - 1 meter = 1000 millimeters.
# - Return the final multi-line string.
# - Do not print.
# - Do not ask for input.

def solution(meters):
    meters = float(meters)

    centimeters = meters * 100
    milimeters = meters * 1000

    return f"Centimeters: {centimeters}\nMillimeters: {milimeters}"
