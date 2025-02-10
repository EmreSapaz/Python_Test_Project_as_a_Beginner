#Number Guess#
import random

lowest_number = 1
highest_number = 1000
answer = random.randint(lowest_number,highest_number)

Guesses = 0
is_running =True

print("Python Number Guessing Game")
print(f"Select a Number Between {lowest_number}-{highest_number}")

while is_running:
    Guess = int(input("Your Guess:"))
    if Guess.is_integer():
        Guess = int(Guess)
        Guesses +=1

        if Guess<lowest_number or Guess>highest_number:
            print("Number is Out of Range")
            print(f"Please Select a Number Between {lowest_number}-{highest_number}")
        elif Guess < answer :
            print("Pick a Bigger Number!!")
        elif Guess > answer :
            print("Pick a Smaller Number")
        elif Guess == answer:
            print(f"Correct!! The answer was {answer}")
            print(f"Number of Guesses : {Guesses}")
            is_running = False

    else:
        print("Invalid Guess")
        print(f"Please Select a Number Between {lowest_number}-{highest_number}")
