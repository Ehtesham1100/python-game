# I acknowledge the use of Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/) to create the code in this file
# Small improvement for to show merge
import tkinter as tk
import random
def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret:
            result_label.config(text="Correct! Well done, You guessed the number")
        else:
            result_label.config(text=f"Wrong! The correct number was {secret}.")
    except ValueError:
        result_label.config(text="please enter a valid number.")

def play_again():
    global secret
    secret = random.randint(1, 10)
    entry.delete(0, tk.END)
    result_label.config(text="New game started! Guess again.")

secret = random.randint(1, 10)

window = tk.Tk()
window.title("Guessing Game - GUI Version")

label = tk.Label(window, text="Guess a number between 1 and 10:")
label.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk. Button(window, text="Submit Guess", command=check_guess)
button.pack(pady=5)

play_again_button = tk.Button(window,text="Play Again", command=play_again)
play_again_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()