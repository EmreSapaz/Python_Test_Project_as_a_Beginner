#Shopping Cart#
import time

Foods = []
Prices = []
Total = 0

while True:
    food = input("Enter a food to buy (Press X to quit):")
    if food.upper() == "X":
        break
    else:
        price = float(input(f"Enter the price of {food} : $"))
        Foods.append(food)
        Prices.append(price)
        time.sleep(.3)


for price in Prices:
    Total += price


print("-------Cart-------")
for food,price in zip(Foods,Prices):
    print(f"{food} ----> ${price}")
print(f"Total : ${Total}")
print("-------Cart-------")