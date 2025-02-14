import random


def main():
    min_number = 0
    max_number = 100
    random_number = random.randint(min_number, max_number)
    guess_number = 0
    print(f"Guess a number between {min_number} and {max_number}")

    while True:
        guess = int(input("Enter your guess : "))
        if guess<random_number:
            guess_number += 1
            print("Too Low")
        elif guess>random_number:
            guess_number += 1
            print("Too High")
        elif guess == random_number:
            print("*********************************")
            print("Your Guess Correct")
            print(f"Total guess : {guess_number}")
            print("*********************************")

            ask= input("Wanna play again?\nY or N:")
            if ask.upper() == "Y":
                main()
            else:
                break
main()