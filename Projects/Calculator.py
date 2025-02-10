#Calculator#
print("Calculator\n")
print("Operators:\n+ for addition\n- for substraction\n* for multiplication\n/ for division")
operator = input("Enter an operator:")

num_1 = float(input("Enter the 1st Number:"))
num_2 = float(input("Enter the 2nd Number:"))

if operator == "+":
    result = num_1 + num_2
    print(round(result,3))
elif operator == "-":
    result = num_1 - num_2
    print(round(result,3))
elif operator == "*":
    result = num_1 * num_2
    print(round(result,3))
elif operator == "/":
    result = num_1 / num_2
    print(round(result,3))

else:
    print(f"{operator} Is Not A Valid Operator")