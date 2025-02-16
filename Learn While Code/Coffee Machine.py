import time

Coffee_types = {
    "Espresso" : ["50ml water","18g coffee","$1.50"],
    "Latte" : ["200ml water","24g coffee","150ml milk"],
    "Cappuccino" : ["250ml water","24g coffee","100ml milk"]
}
Coffee_machine = [300,200,100]

while True:
    ask = input("What would you like?\nEspresso,Latte or Cappuccino:")
    if ask == "Espresso":
        print("☕")
        break
    if ask == "Espresso":
        print("☕")
        break
    if ask == "Espresso":
        print("☕")
        break
    if ask.lower() == "off":
        time.sleep(.4)
        print("Machine is shutting down...")
        time.sleep(.4)
        break
    if ask.lower() == "report":
        time.sleep(.5)
        print(f"Water  :  {Coffee_machine[0]}\nMilk   :  {Coffee_machine[1]}\nCoffee :  {Coffee_machine[2]}")
        break









