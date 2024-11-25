import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_round(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    messagebox.showinfo("Result", result_text)

def create_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    rock_button = tk.Button(frame, text="Rock", command=lambda: play_round("rock"))
    rock_button.pack(side=tk.LEFT, padx=10)

    paper_button = tk.Button(frame, text="Paper", command=lambda: play_round("paper"))
    paper_button.pack(side=tk.LEFT, padx=10)

    scissors_button = tk.Button(frame, text="Scissors", command=lambda: play_round("scissors"))
    scissors_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
