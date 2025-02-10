#Temperature Conversion#

print("Temperature Conversion")
print("C for Celsius / F for Fahrenheit")
unit = input ("Enter the unit:")
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((temp * (9/5)) + 32,1)
    unit = "F"
    print(f"Temperature is {temp} {unit}")
elif unit == "F":
    temp = round((temp - 32) * (5/9),1)
    unit = "C"
    print(f"Temperature is {temp} {unit}")
else:
    print(f"{unit} is not valid for measurement")