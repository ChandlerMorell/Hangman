# These imports could probably be shorter but hey it works
import random
import sys, time

from time import sleep
from os import system, name
from words import word_list

# Creates the slow typing effect
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

# Get's a random word from the array
def get_word():
    word = random.choice(word_list)
    return word.upper()

# Main game logic
def play(word):
    word_completion = "_" * len(word) # A letter initially starts as an _ before being guessed

    guessed = False
    guessed_letters = []
    guessed_words = []

    attempts = 6

    print_slow("\nLet\'s play a game of hangman.\n")
    sleep(.5)
    print_slow("My money is on me.\n")
    sleep(2)
    clear()

    print(display_hangman(attempts)) # Gets the different hangman stages
    print(word_completion + "\n") # Prints the word as it's being guessed

    # Logic of the game. Checks if words/letters have been guessed and if they
    # are correct or incorrect. Deducts tries if incorrect. Pretty self-explanatory
    while not guessed and attempts > 0:
        guess = input("Guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter.")

                sleep(1.5)
                clear()

            elif guess not in word:
                print(guess, "is not correct.")

                attempts -= 1
                guessed_letters.append(guess)

                sleep(1.5)
                clear()
            else:
                print("Good guess")

                guessed_letters.append(guess)
                words_in_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    words_in_list[index] = guess
                word_completion = "".join(words_in_list)

                if "_" not in word_completion:
                    guessed = True

                sleep(1.5)
                clear()

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You\'ve already guessed this word.")

                sleep(1.5)
                clear()

            elif guess != word:
                print("That is not the word.")

                attempts -= 1
                guessed_words.append(guess)

                sleep(1.5)
                clear()

            else:
                guessed = True
                word_completion = word
        else:
            print("That guess is not valid.")

            sleep(1.5)
            clear()

        print(display_hangman(attempts))
        print(word_completion + "\n")

    if guessed:
        print_slow("Congratulations, that was the word! PogU!")

        sleep(2.5)
        clear()
    else:
        print_slow("You ran out of attempts. Game over. The word was: " + word)

        sleep(2.5)
        clear()

# Array of the different stages of the game
def display_hangman(attempts):
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    ========='''
    ]

    return stages[attempts]

# Clears the console and should work for all OS's
def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Gets the game started
def main():
    clear()
    word = get_word()

    play(word)

    sleep(2)
    clear()
    # Asks the user if they want to play the game again
    while input("\nWanna go again? (y/n): ").lower() == "y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
