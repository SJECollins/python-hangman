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
        ||      /|\
        ||
        ||
        ||
    [][][][][]
    """,
        """
        ##=======#
        ||       ¦
        ||       O
        ||      /|\
        ||      /
        ||
        ||
    [][][][][]
    """,
            """
        ##=======#
        ||       ¦
        ||       O
        ||      /|\
        ||      / \
        ||
        ||
    [][][][][]
    """,
]

WORD = ""
GUESSES = ""
LIVES = 7

def get_word():  
    api_url = 'https://random-word-api.herokuapp.com/word'
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        global WORD
        WORD = re.sub(r'\W+', '', response.text)
    else:
        print("Error:", response.status_code, response.text)


def print_hangman(lives):
    print(STAGES[(len(STAGES) - lives)])


def print_word(GUESSES):
    print("The word: ", end = "")
    for letter in WORD:
        if letter in GUESSES:
            print(letter)
        else:
            print("_", end = "")
    print("")
    print("Your guesses: ", GUESSES)


def check_guess(user_guess, GUESSES, LIVES):
    GUESSES += user_guess
    if user_guess in WORD:
        print(f"Correct! {user_guess} is in the word!")
    else:
        LIVES -= 1
        print(f"Wrong!")


def get_guess(GUESSES, LIVES):
    while True:
        user_guess = input("Guess a letter: ").strip().lower()
        if len(user_guess) > 1:
            print("Ah ah ah! One letter at a time.")
        else:
            check_guess(user_guess, GUESSES, LIVES)
            break


if __name__ == "__main__":
    print("Let's play HANGMAN!")
    print("Guess one letter a time.")
    print("Save the man.")
    print_hangman(LIVES)
    get_word()

    while LIVES > 0:
        get_guess(GUESSES, LIVES)
        print_hangman(LIVES)
        print_word(GUESSES)
