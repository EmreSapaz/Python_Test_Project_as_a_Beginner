#Banking#
import time


def show_balance(balance):
    print("******************************")
    print(f"Balance : ${balance:.2f}")
    print("******************************")
def deposit():
    amount = float(input("Enter an amount to be deposited : "))
    if amount < 0 :
        print("******************************")
        print("That is not a valid amount")
        print("******************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn:"))

    if amount > balance:
        print("******************************")
        print("Insufficient Funds")
        print("******************************")
        return 0
    elif amount < 0 :
        print("******************************")
        print("Amount must be greater than 0")
        print("******************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_runnig = True

    while is_runnig:
        print("******************************")
        print("Banking Program")
        print("******************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("******************************")

        choice = input("Enter Your Choice:")

        if choice == "1":
            time.sleep(1)
            show_balance(balance)
            time.sleep(1)

        elif choice == "2":
            time.sleep(1)
            balance += deposit()
            time.sleep(1)
            print(f"New Balance : ${balance}")
            time.sleep(1)

        elif choice == "3":
            time.sleep(1)
            balance -=withdraw(balance)
            time.sleep(1)
            print(f"New Balance : ${balance}")

        elif choice == "4":
            is_runnig = False
            time.sleep(1)

        else:
            print("Invalid Choice")
            time.sleep(1)

    print("Thank You. Have a Nice Day!")

if __name__ == "__main__":
    main()