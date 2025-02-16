import time

Coffee_types = {
    "Espresso" : {
    "Water" : 50,
    "Milk"  : 0,
    "Coffee": 18,
    "Price" : 1.5
    }
,
    "Latte" : {
    "Water" : 200,
    "Milk"  : 150,
    "Coffee": 24,
    "Price" : 2.5
    }
,
    "Cappuccino" : {
    "Water" : 250,
    "Milk"  : 100,
    "Coffee": 24,
    "Price" : 3
    }

}
Coffee_machine = {
    "Water" : 300,
    "Milk"  : 200,
    "Coffee": 100,
    "Money" : 0
    }

Coins = {
    "Penny"  : .01,
    "Nickel" : .05,
    "Dime"   : .10,
    "Quarter": .25
}


while True:
    ask = input("What would you like?\nEspresso,Latte or Cappuccino:")
    if ask.capitalize() == "Espresso":
        if Coffee_types["Espresso"]["Water"] <= Coffee_machine["Water"] and Coffee_types["Espresso"]["Coffee"]<=Coffee_machine["Coffee"] :
            payment_penny = float(input("Insert your Pennies : "))
            payment_nickel = float(input("Insert your Nickels : "))
            payment_dime = float(input("Insert your Dimes : "))
            payment_quarter = float(input("Insert your Quarters : "))
            payment = payment_penny * .01 + payment_nickel * .05 + payment_dime * .1 + payment_quarter * .25

            if payment == Coffee_types["Espresso"]["Price"]:
                print("Your order is preparing... ")
                time.sleep(2)
                print("Here is your order☕...")
                Coffee_machine["Water"] -= Coffee_types["Espresso"]["Water"]
                Coffee_machine["Coffee"] -= Coffee_types["Espresso"]["Coffee"]
                time.sleep(3)
                Coffee_machine["Money"] += Coffee_types["Espresso"]["Price"]

            elif payment > Coffee_types["Espresso"]["Price"]:
                change = payment - Coffee_types["Espresso"]["Price"]
                print(f"Your change : ${change:.2f}")
                print("Your order is preparing... ")
                time.sleep(1)
                print("Here is your order☕...")
                Coffee_machine["Water"] -= Coffee_types["Espresso"]["Water"]
                Coffee_machine["Coffee"] -= Coffee_types["Espresso"]["Coffee"]
                time.sleep(3)
                Coffee_machine["Money"] += Coffee_types["Espresso"]["Price"]
            else:
                print("Insufficient money...")
                time.sleep(3)
        else:
            print("Sorry not enough resources")
            time.sleep(3)


    if ask.capitalize() == "Latte":
        if Coffee_types["Latte"]["Water"] <= Coffee_machine["Water"] and Coffee_types["Latte"]["Coffee"] <= Coffee_machine["Coffee"] and Coffee_types["Latte"]["Milk"] <= Coffee_machine["Milk"]:
            payment_penny = float(input("Insert your Pennies : "))
            payment_nickel = float(input("Insert your Nickels : "))
            payment_dime = float(input("Insert your Dimes : "))
            payment_quarter = float(input("Insert your Quarters : "))
            payment = payment_penny * .01 + payment_nickel * .05 + payment_dime * .1 + payment_quarter * .25

            if payment == Coffee_types["Latte"]["Price"]:
                print("Your order is preparing... ")
                time.sleep(1)
                print("Here is your order☕...")
                Coffee_machine["Water"] -= Coffee_types["Latte"]["Water"]
                Coffee_machine["Coffee"] -= Coffee_types["Latte"]["Coffee"]
                Coffee_machine["Milk"] -= Coffee_types["Latte"]["Milk"]
                time.sleep(3)
                Coffee_machine["Money"] += Coffee_types["Latte"]["Price"]

            elif payment > Coffee_types["Latte"]["Price"]:
                change = payment - Coffee_types["Latte"]["Price"]
                print(f"Your change : ${change:.2f}")
                print("Your order is preparing... ")
                time.sleep(1)
                print("Here is your order☕...")
                Coffee_machine["Water"] -= Coffee_types["Latte"]["Water"]
                Coffee_machine["Coffee"] -= Coffee_types["Latte"]["Coffee"]
                Coffee_machine["Milk"] -= Coffee_types["Latte"]["Milk"]
                time.sleep(3)
                Coffee_machine["Money"] += Coffee_types["Latte"]["Price"]
            else:
                print("Insufficient money...")
                time.sleep(3)
        else:
            print("Sorry not enough resources...")
            time.sleep(3)


    if ask.capitalize() == "Cappuccino":
        if Coffee_types["Cappuccino"]["Water"] <= Coffee_machine["Water"] and Coffee_types["Cappuccino"]["Coffee"] <= Coffee_machine["Coffee"] and Coffee_types["Cappuccino"]["Milk"] <= Coffee_machine["Milk"]:
            payment_penny = float(input("Insert your Pennies : "))
            payment_nickel = float(input("Insert your Nickels : "))
            payment_dime = float(input("Insert your Dimes : "))
            payment_quarter = float(input("Insert your Quarters : "))
            payment = payment_penny * .01 + payment_nickel * .05 + payment_dime * .1 + payment_quarter * .25

            if payment == Coffee_types["Cappuccino"]["Price"]:
                print("Your order is preparing... ")
                time.sleep(1)
                print("Here is your order☕...")
                Coffee_machine["Water"] -= Coffee_types["Cappuccino"]["Water"]
                Coffee_machine["Coffee"] -= Coffee_types["Cappuccino"]["Coffee"]
                Coffee_machine["Milk"] -= Coffee_types["Cappuccino"]["Milk"]
                Coffee_machine["Money"] += Coffee_types["Cappuccino"]["Price"]
                time.sleep(3)

            elif payment > Coffee_types["Cappuccino"]["Price"]:
                change = payment - Coffee_types["Cappuccino"]["Price"]
                print(f"Your change : ${change:.2f}")
                print("Your order is preparing... ")
                time.sleep(1)
                print("Here is your order☕...")
                Coffee_machine["Water"] -= Coffee_types["Cappuccino"]["Water"]
                Coffee_machine["Coffee"] -= Coffee_types["Cappuccino"]["Coffee"]
                Coffee_machine["Milk"] -= Coffee_types["Cappuccino"]["Milk"]
                Coffee_machine["Money"] += Coffee_types["Cappuccino"]["Price"]
                time.sleep(3)
            else:
                print("Insufficient money...")
                time.sleep(3)
        else:
            print("Sorry not enough resources...")
            time.sleep(3)


    if ask.lower() == "off":
        time.sleep(.4)
        print("Machine is shutting down...")
        time.sleep(.4)
        break


    if ask.lower() == "report":
        time.sleep(.5)
        print(f"Water  :  {Coffee_machine["Water"]}\nMilk   :  {Coffee_machine["Milk"]}\nCoffee :  {Coffee_machine["Coffee"]}\nMoney  :  ${Coffee_machine["Money"]}")










