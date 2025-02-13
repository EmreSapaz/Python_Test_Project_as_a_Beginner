from Animal_names import words
import random
import time

Hangman_art = { 0 : ("   _______  ",
                    "  |/      |  ",
                    "  |          ",
                    "  |          ",
                    "  |          ",
                    "  |          ",
                    "__|___       ",),
                1 : ("   _______ " ,
                     "  |/      |" ,
                     "  |      (_)",
                     "  |         ",
                     "  |         ",
                     "  |         ",
                     "__|___      ",),
                2 : ("   _______ " ,
                     "  |/      |" ,
                     "  |      (_)",
                     "  |       | ",
                     "  |         ",
                     "  |         ",
                     "__|___      ",),
                3 : ("   _______  ",
                     "  |/      | ",
                     "  |      (_)",
                     "  |      \\| ",
                     "  |         ",
                     "  |         ",
                     "__|___      ",),
                4 : ("   _______  ",
                    "  |/      |  ",
                    "  |      (_) ",
                    "  |      \\|/ ",
                    "  |          ",
                    "  |          ",
                    "__|___       ",),
                5 : ("   _______  ",
                     "  |/      | ",
                     "  |      (_)",
                     "  |      \\|/",
                     "  |       | ",
                     "  |         ",
                     "__|___      ",),
                6 : ("   _______  ",
                     "  |/      | ",
                     "  |      (_)",
                     "  |      \\|/",
                     "  |       | ",
                     "  |      /  ",
                     "__|___      ",),
                7 : ("   _______ ",
                     "  |/      |",
                     "  |      (_)",
                     "  |      \\|/",
                     "  |       |",
                     "  |      / \\",
                     "__|___         ",)

}

def display_hangman(wrong_guess):
    print("***********************************")
    for i in Hangman_art[wrong_guess]:
        print(i)
    print("***********************************")

def show_hint(hint):
    print(" ".join(hint))

def show_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()

    while True:
        time.sleep(.4)
        display_hangman(wrong_guess)
        show_hint(hint)
        guess = input("Enter your guess : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input...")
            time.sleep(.3)

        if guess in guessed_letters:
            print(f" {guess} is already guessed")

        if not guess in guessed_letters:
            guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if not "_" in hint :
            display_hangman(wrong_guess)
            show_answer(answer)
            print("You Won!!!")
            break

        elif wrong_guess >= len(Hangman_art) - 1:
            display_hangman(wrong_guess)
            show_answer(answer)
            print("YOU LOSE!!")
            break

main()