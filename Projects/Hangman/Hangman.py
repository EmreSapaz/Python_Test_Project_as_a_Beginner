#Hangman#
import random
import time
from Animal_names import words
import os
import sys

hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\ ",
                  "   "),
               5:(" o ",
                  "/|\\ ",
                  "/  "),
               6:(" o ",
                  "/|\\ ",
                  "/ \\ ")}


def display_man(wrong_guess):
    print("********")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():

    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:

        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Enter a Letter:").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            time.sleep(1)
            continue

        if guess.isdigit():
            print("Invalid Input")
            time.sleep(1)
            continue


        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guess += 1

        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU WIN!!")
            ask = input("Wanna play again?(Y/N):").upper()
            if ask == "Y":
                main()
            else:
                is_running = False

        elif wrong_guess >= len(hangman_art) - 1 :
            display_man(wrong_guess)
            display_answer(answer)
            print("YOU LOSE!!")
            ask = input("Wanna play again?(Y/N):").upper()
            if ask == "Y":
                main()
            else:
                is_running = False



if __name__ == "__main__":
    main()