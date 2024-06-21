import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    user_choice = ''
    if choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Paper'
    elif choice == 3:
        user_choice = 'Scissors'

    result = ''
    if user_choice == computer_choice:
        result = 'Draw'
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = 'You win'
    else:
        result = 'You lose'

    messagebox.showinfo("Result", f'You picked: {user_choice}\nPlayer 2 picked: {computer_choice}\n\n{result}')

def exit_game():
    root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors")

label = tk.Label(root, text="Choose an option:")
label.pack()

button_rock = tk.Button(root, text="Rock", command=lambda: play(1))
button_rock.pack()

button_paper = tk.Button(root, text="Paper", command=lambda: play(2))
button_paper.pack()

button_scissors = tk.Button(root, text="Scissors", command=lambda: play(3))
button_scissors.pack()

button_exit = tk.Button(root, text="Exit", command=exit_game)
button_exit.pack()

root.mainloop()
