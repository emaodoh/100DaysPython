
import random

def password():
    while True:
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
            continue
        lower  = input("optional: select between \nlower (y/n): ").strip().lower()
        if lower != "y" and lower != "n":
            print("select y for YES and n for NO")
            continue
        
        upper  = input("upper (y/n): ").strip().lower()
        if upper != "y" and upper != "n":
            print("select y for YES and n for NO")
            continue
        symbol  = input("symbol (y/n): ").strip().lower()
        if symbol != "y" and symbol != "n":
            print("select y for YES and n for NO")
            continue
        digit = input("digit (y/n): ").strip().lower()
        if digit != "y" and digit != "n":
            print("select y for YES and n for NO")
            continue
         
        
        if lower == "y":
            character += lowerchar
        if upper == "y":
            character += upperchar
        if digit == "y":
            character += digitchar
        if symbol == "y":
            character += symbolchar
        if character == "":
            print("Select at least one character type")
            continue
    
        gen = random.choices(character, k=length)
        gen = "".join(gen)
    
   
        return gen


password = password()
print(f"password: {password}")