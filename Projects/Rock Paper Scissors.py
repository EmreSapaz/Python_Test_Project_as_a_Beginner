import random
import time

print("""
Rules:
    Rock>Scissors
    Paper>Rock
    Scissors>Paper
""")


options = ("rock","paper","scissors")

play = True
option = ("rock","paper","scissors","x")

while play:

    player = None
    computer = random.choice(options)


    while player not in option:
        player = input("Enter a Choice:").lower()

    print("To Quit Press X")
    if player == "x":
        play = False
        print("Quitting From The Game ")

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("Tie!")
        time.sleep(1)

    elif player == "rock" and computer == "scissors":
        print("You win!")
        time.sleep(1)

    elif player == "paper" and computer == "rock":
        print("You Win!")
        time.sleep(1)

    elif player == "scissors" and computer == "paper":
        print("You Win!")
        time.sleep(1)

    else:
        print("You Lose!")
        time.sleep(1)

    if not input("Wanna Play Again (Y/N):").lower() == "y":
        play = False
print("Thanks for Playing")