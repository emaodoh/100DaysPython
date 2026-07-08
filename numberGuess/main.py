
import random

def guess():
    question = ""
    while True:
        
        computer_choice = random.randint(0, 100)
        
        attempt = 5
        while attempt > 0:
            user_num = input("Enter a number from 0-100: ").strip()
            
            try:
                user_num = int(user_num)
            except ValueError:
                print("input must be a number\n")
                continue
            if user_num > 100 or user_num < 0:
                print("number must be between 0 and 100")
                continue
            if user_num != computer_choice:
                if  user_num > computer_choice:
                    print("Your guess is too big\n")
                else:
                    print("Your guess is too small\n")
            
            else:
                print("congratulations You win\n")
                break
                
            
            attempt -=1
            print(f"you have {attempt} attempts left")
            if attempt == 0:
                print(f"You lose secret number is {computer_choice}\n")
                
        
        question = input("Play again? (y/n):  ").lower()
        if question == "y":
                break
    return "Goodbye"

print(guess())