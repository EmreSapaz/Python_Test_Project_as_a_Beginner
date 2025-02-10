#Concession Stand#

menu = {"Pizza" : 3.00,
        "Nachos" : 4.50,
        "PopCorn" : 6.00,
        "Fries" :  2.50,
        "Chips" : 1.00,
        "Pretzel" : 3.50,
        "Soda" : 3.00,
        "Lemonade" : 4.25}

Cart = []
Total = 0

print("-----------MENU-----------")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select foods(X to Quit):")
    if food.upper() == "X":
        break
    elif menu.get(food) is not None:
        Cart.append(food)
    else:
        print("Food is not in the MENU")

print("-----------------------------------")
for food in Cart:
    Total += menu.get(food)

    print("Food added to Cart:",food,end="\n")

print("-----------------------------------")
print("-------Your Cart---------------")
for i in Cart:
    print(i)
print("-----------------------------------")
print(f"Total = {Total}")