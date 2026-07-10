# ==========================
# Important Python Concepts
# ==========================

# input()
# Used to collect input from the user through the Command Line Interface (CLI).
# It always returns a string.

name = input("Enter your name: ")
age = input("Enter your age: ")

# --------------------------

# try/except
# Used to handle errors (exceptions) so your program doesn't crash.

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("The value you entered is not a number.")
    # Use:
    # return -> inside a function
    # continue -> inside a loop
    # break -> to exit a loop
    # pass -> do nothing

# --------------------------

# random.choice()
# Returns one random item from a sequence (list, tuple, string, etc.).

import random

fruits = ["apple", "banana", "orange", "mango"]
fruit = random.choice(fruits)
print(fruit)

# --------------------------

# random.randint(a, b)
# Returns a random integer between a and b (both numbers are included).

import random

num = random.randint(0, 100)
print(num)

# --------------------------

# Remember:
# input() -> Get data from the user.
# try/except -> Handle errors safely.
# random.choice() -> Pick one random item.
# random.randint() -> Generate a random integer in a given range.