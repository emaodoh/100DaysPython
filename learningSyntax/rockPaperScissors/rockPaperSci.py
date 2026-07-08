
import random

def get_choice():
    print("Enter q to stop")
    while True:
            player = input("make a choice from rock,paper or scissors:  ").lower()

            if player == "rock" or player == "paper" or player == "scissors":
                options = ["rock", "paper", "scissors"]
                computer_choice = random.choice(options)
                return {"computer": computer_choice, "player": player}
            if player == "q":
                return "quit"

            print ("Invalid input (options rock,paper or scissors)")

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "it is a tie"
    elif player == "rock":
        if computer == "paper":
            return "paper cover rock, You loss"
        else:
            return "rock smaches scissors: You win!"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock: You win!"
        else:
            return "scissors cuts paper: You lose"
    elif player == "scissors":
        if computer ==   "paper":
            return "scissors cuts paper: You win!"
        else:
            return "rock smaches scissors: You lose"
    else:
        return "invalid input"

choices = get_choice()
if choices == "quit":
    print ("Thanks for playing the game")
else:
    player_choice = choices["player"]
    computer_choice = choices["computer"]

    result = check_win(player_choice, computer_choice)

    print(result)