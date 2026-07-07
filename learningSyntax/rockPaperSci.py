
import random

def get_choice():
    player = input("make a choice from rock,paper or scissors:  ")
    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    result = {"computer": computer_choice, "player": userInput}

    return result

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it is a tie"
    elif player == "rock" and computer == "paper":
        return "paper cover rock, You loss"
    elif player == "rock" and computer == "scissors":
        return "rock smashes scissors: You win! "
    else:
        return "you lose"
re = check_win("rock", "scissors")
print(re)