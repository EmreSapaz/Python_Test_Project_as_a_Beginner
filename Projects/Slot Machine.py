import time
import random


def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*******************")
    print(" ".join(row))
    print("*******************")

def display():
    pass

def get_pay_out(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 1.5
        elif row[0] == "🍉":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 2.5
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "⭐":
            return bet * 10
    else:
        return 0

def main():
    balance = 100

    print("****************************")
    print(" Welcome  to  the PytSloth   ")
    print(" Symbols : 🍒 🍉 🍋 🔔 ⭐ ")
    print("****************************")

    while balance > 0:
        print(f"Current Balance : ${balance}")

        bet = input("Place Your Bet Amount:")

        if not bet.isdigit():
            print("Please Enter a Valid Number")
            time.sleep(1)
            continue

        bet = int(bet)

        if bet > balance :
            print("Insufficient Funds")
            time.sleep(1)
            continue

        if bet <= 0 :
            print("Bet must be greater than zero")
            time.sleep(1)
            continue

        balance -= bet

        row = spin_row()
        print("Spinning..")
        time.sleep(1)
        print_row(row)

        pay_out = get_pay_out(row,bet)

        if pay_out > 0:
            print(f"You Won ${pay_out}")
        else:
            print("You Lost This Round")

        balance += pay_out

        play_again = input("Wanna Play Again? (Y/N):").upper()

        if play_again != "Y":
            break

    print("************************************************")
    print(f"Game Over! Your final balance is ${balance}")
    print("************************************************")


if __name__ == "__main__" :
    main()