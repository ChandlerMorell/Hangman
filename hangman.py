"""Created by Chandler Morell."""
# These imports could probably be shorter but hey it works
import random
import sys
import time

from time import sleep
from os import system, name

from words import easy_words_list
from words import intermediate_words_list
from words import hard_words_list


def print_slow(string):
    """Create the slow typing effect."""
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


def time_convert(sec):
    """Convert the time given by the timer."""
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    print("That took {0}:{1}. Good job!".format(int(mins), sec))


def get_difficulty():
    """List the difficulties for the user."""
    difficulties = [
        '1) Easy (5-letter word)',
        '2) Intermediate (7-letter word)',
        '3) Hard (10-letter word)'
    ]

    print_slow("Let\'s play a game of hangman.\n")
    sleep(.5)
    clear()

    print_slow("To get started, select your game difficulty.\n")
    print("Select the number of your desired choice.")
    sleep(.25)

    print("\n" + "\n".join(difficulties))
    mode = input("\n")

    return mode


# Get's a random word from the arrays
def get_word(mode):
    """Let the player choose their difficulty."""
    if mode == "1":
        word = random.choice(easy_words_list)
    elif mode == "2":
        word = random.choice(intermediate_words_list)
    elif mode == "3":
        word = random.choice(hard_words_list)

    return word.upper()


def play(word):
    """Logic of the game."""
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    clear()
    # A letter initially starts as an _ before being guessed
    word_completion = "_" * len(word)

    guessed = False
    guessed_letters = []
    guessed_words = []

    attempts = 6

    print(display_hangman(attempts))  # Gets the different hangman stages
    print(word_completion + "\n")  # Prints the word as it's being guessed

    # Logic of the game. Checks if words/letters have been guessed and if they
    # are correct or incorrect. Deducts tries if incorrect. Pretty self-
    # explanatory
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
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]

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

                attempts -= 6
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
        print("Guessed letters: " + ', '.join(guessed_letters))

    if guessed:
        print_slow("Congratulations, that was the word!")

        sleep(2.5)
        clear()
    else:
        print_slow("\nYou ran out of attempts. ")
        sleep(.25)

        print_slow("Game over. ")
        sleep(.25)

        print_slow("The word was: " + word)

        sleep(2.5)
        clear()


def display_hangman(attempts):
    """Contains the different hangman phases."""
    stages = ['''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
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


def clear():
    """Clear the console for neatness."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    """Get the game going."""
    clear()

    begin = time.time()

    mode = get_difficulty()

    word = get_word(mode)

    play(word)

    sleep(2)
    clear()

    # Asks the user if they want to play the game again
    end = time.time()
    elapsed = end - begin
    elapsed = int(elapsed)

    time_convert(elapsed)
    while input("Wanna go again? (y/n): ").lower() == "y":
        word = get_word(mode)
        play(word)


if __name__ == "__main__":
    main()
