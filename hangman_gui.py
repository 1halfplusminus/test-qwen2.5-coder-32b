# hangman_gui.py

import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.words = ["python", "hangman", "challenge", "developer", "code", "programming"]
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.attempts_remaining = 6
        
        self.label = tk.Label(root, text="Welcome to Hangman!", font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.word_display = tk.Label(root, text=self.get_display_word(), font=("Helvetica", 14))
        self.word_display.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.make_guess)
        
        self.guess_button = tk.Button(root, text="Guess", font=("Helvetica", 14), command=self.make_guess)
        self.guess_button.pack(pady=10)
        
        self.attempts_label = tk.Label(root, text=f"Attempts remaining: {self.attempts_remaining}", font=("Helvetica", 12))
        self.attempts_label.pack(pady=10)
        
    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word_to_guess])
    
    def make_guess(self, event=None):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You've already guessed that letter.")
            return
        
        self.guessed_letters.add(guess)
        
        if guess in self.word_to_guess:
            self.word_display.config(text=self.get_display_word())
            if set(self.word_to_guess).issubset(self.guessed_letters):
                messagebox.showinfo("Congratulations", f"You've guessed the word: {self.word_to_guess}")
                self.root.quit()
        else:
            self.attempts_remaining -= 1
            self.attempts_label.config(text=f"Attempts remaining: {self.attempts_remaining}")
            if self.attempts_remaining == 0:
                messagebox.showinfo("Game Over", f"Game over! The word was: {self.word_to_guess}")
                self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
