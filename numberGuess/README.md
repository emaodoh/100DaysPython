START

LOOP forever

    Generate a random number from 0–100
    Set attempts to 5

    WHILE attempts > 0

        Ask the user to enter a number between 0 and 100

        IF input is not a number
            Display "Input must be a number"
            Continue

        IF number is outside 0–100
            Display "Number must be between 0 and 100"
            Continue

        IF user's number == secret number
            Display "Congratulations! You win"
            Break

        IF user's number > secret number
            Display "Your guess is too big"

        ELSE
            Display "Your guess is too small"

        Decrease attempts by 1
        Display remaining attempts

    END WHILE

    IF attempts == 0
        Display "You lose"
        Display the secret number

    Ask the user:
        "Play again? (y/n)"

    IF answer is not "y"
        Exit the program

END LOOP