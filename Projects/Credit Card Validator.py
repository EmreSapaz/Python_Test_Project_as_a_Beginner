sum_odd_digits = 0
summ_even_digits = 0
total = 0
 #Step 1
card_number = input("Enter Credit Card Number:")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

#Step 2
for x in card_number[::2]:
    sum_odd_digits += int(x)

#Step 3
for x in card_number[1::2]:
    x = int(x)*2
    if x>=10:
        summ_even_digits += 1 + (x%10)
    else:
        summ_even_digits += x

#Step 4
total = summ_even_digits + sum_odd_digits

#Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")