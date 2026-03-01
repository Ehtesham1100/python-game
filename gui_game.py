# I acknowledge the use of Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/) to create the code in this file

import tkinter as tk
import random
def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret:
            result_label.config(text="Correct! You guessed the number")
        else:
            result_label.config(text=f"Wrong! The correct number was {secret}.")
    except ValueError:
        result_label.config(text="please enter a valid number.")

secret = random.randint(1, 10)

window = tk.Tk()
window.title("Guessing Game")

label = tk.Label(window, text="Guess a number between 1 and 10:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk. Button(window, text="Submit Guess", command=check_guess)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()