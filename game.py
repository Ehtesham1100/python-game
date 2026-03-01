# I acknowledge the use of Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/) to create the code in this file

import random

def play_game():
    secret = random.randint(1, 10)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    guess = int(input("Enter your guess"))

    if guess == secret:
        print("Correct! You guessed the number!")
    else:
        print("Wrong! The correct number was {secret}.")

play_game()
