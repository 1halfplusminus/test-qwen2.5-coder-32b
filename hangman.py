# hangman.py

import random

def get_random_word():
    words = ["python", "hangman", "challenge", "developer", "code", "programming"]
    return random.choice(words)

def display_game_state(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f"Current word: {display}")

def hangman():
    word_to_guess = get_random_word()
    guessed_letters = set()
    attempts_remaining = 6

    print("Welcome to Hangman!")
    while attempts_remaining > 0:
        display_game_state(word_to_guess, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts_remaining -= 1
            print(f"Incorrect! Attempts remaining: {attempts_remaining}")

        if set(word_to_guess).issubset(guessed_letters):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
