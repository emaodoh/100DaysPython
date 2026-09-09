# Instructions

# Write a function called `solution` that converts a Celsius temperature to Fahrenheit.

# The function receives one value, `celsius`, and must return the Fahrenheit value rounded to 2 decimal places.

# Formula:

# fahrenheit = (celsius * 9 / 5) + 32

# Rules:
# - Convert the input to a number using `float()`.
# - Return the converted value.
# - Round the answer to 2 decimal places.
# - Do not print.
# - Do not ask for input.

def solution(celsius):
    celsius = float (celsius)

    fehrenheit = (celsius * 1.8) + 32

    return fehrenheit
