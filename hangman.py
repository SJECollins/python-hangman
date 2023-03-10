"""
Simple hangman game???
"""
import requests
import re

STAGES = [
    """
        ##=======#
        ||       ¦
        ||
        ||
        ||
        ||
        ||
    [][][][][]
    """,
    """
        ##=======#
        ||       ¦
        ||       O
        ||
        ||
        ||
        ||
    [][][][][]
    """,
        """
        ##=======#
        ||       ¦
        ||       O
        ||       |
        ||
        ||
        ||
    [][][][][]
    """,
        """
        ##=======#
        ||       ¦
        ||       O
        ||      /|
        ||
        ||
        ||
    [][][][][]
    """,
        """
        ##=======#
        ||       ¦
        ||       O
        ||      /|)
        ||
        ||
        ||
    [][][][][]
    """,
        """
        ##=======#
        ||       ¦
        ||       O
        ||      /|)
        ||      /
        ||
        ||
    [][][][][]
    """,
            """
        ##=======#
        ||       ¦
        ||       O
        ||      /|)
        ||      /¦
        ||
        ||
    [][][][][]
    """,
]

WORD = ""
GUESSES = ""
CORRECT = 0
LIVES = 7
WON = False

def get_word():
    api_url = 'https://random-word-api.herokuapp.com/word'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        global WORD
        WORD = re.sub(r'\W+', '', response.text)
        if len(WORD) > 10:
            get_word()
    else:
        print("Error:", response.status_code, response.text)


def print_hangman():
    print(STAGES[(len(STAGES) - LIVES)])


def print_word(guess):
    print("The word: ", end = "")
    for letter in WORD:
        if letter in guess:
            print(letter, end = "")
        else:
            print("_", end = "")
    print("")
    print("Your guesses: ", guess)


def check_guess(user_guess):
    global GUESSES
    global LIVES
    global CORRECT
    GUESSES += user_guess
    if user_guess in WORD:
        CORRECT += 1
        print(f"Correct! {user_guess} is in the word!")
    else:
        LIVES -= 1
        print(f"Wrong!")


def get_guess():
    while True:
        user_guess = input("Guess a letter: ").strip().lower()
        if len(user_guess) > 1:
            print("Ah ah ah! One letter at a time.")
        elif user_guess in GUESSES:
            print("You guessed that one already.")
        elif user_guess == "":
            print("Try entering a letter.")
        else:
            check_guess(user_guess)
            break


def check_win():
    global WON
    WON = all(item in GUESSES for item in WORD)


def end_game():
    if LIVES == 0:
        print("Uh oh...")
    else:
        print("You did it!")
    print(f"The word was: ", WORD)


if __name__ == "__main__":
    print("Let's play HANGMAN!")
    print("Guess one letter a time.")
    print("Save the man.")
    get_word()

    while LIVES > 0 and not WON:
        check_win()
        print_hangman()
        print_word(GUESSES)
        get_guess()

    end_game()
