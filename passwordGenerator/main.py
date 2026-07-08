
import random

def password():
    upperchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerchar = "abcdefghijklmnopqrstuvwxyz"
    symbolchar = "!@#$%^&*"
    digitchar = "1234567890"
    character = ""
    length = input("Enter the length of pass:  ")
    try:
        length = int(length)
    except ValueError:
        print("enter a valid number ")
    lower  = input("optional: select between \nlower (y/n): ").strip()
    upper  = input("upper (y/n): ").strip()
    symbol  = input("symbol (y/n): ").strip()
    digit = input("digit (y/n): ").strip()

    if lower == "y":
        character += lowerchar
    if upper == "y":
        character += upperchar
    if digit == "y":
        character += digitchar
    if symbol == "y":
        character += symbolchar
    gen = random.choices(character, k=int(length))
    gen = "".join(gen)
    
   
    return gen
password = password()
print(f"password: {password}")