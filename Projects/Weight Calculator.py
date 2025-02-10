#Weight#

print("Weight Conversion")
weight = float(input("Enter Your Weight : "))
unit = input("Kg for Kilogram / Lb for Pound:")
if unit =="Kg":
    weight = weight * 2.205
    unit = "Lb"
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "Lb":
    weight = weight/2.205
    unit = "Kg"
    print(f"Your weight is {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid unit")


