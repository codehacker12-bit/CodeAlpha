

import random

# List of words for the game
words = ["python", "hangman", "programming", "developer", "code"]

def select_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Get ready to guess! Welcome to the Hangman Game!")
    word_to_guess = select_random_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\nThe mystery word:")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("GoOOD GUESS!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        print("\nThe mystery word:")
        print(display_word(word_to_guess, guessed_letters))

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nWOHOO CONGRATULATIONS! You guessed the word:", word_to_guess)
            break
    else:  # This `else` belongs to the `while` loop and executes if the loop is not broken.
        print("\nYOU LOST! The word was:", word_to_guess)

# Corrected main check
if __name__ == "__main__":
    hangman()


