#E-mail Slicer#


email = input("Enter Your E-mail:")

index = email.index("@")
username = email[:index]
domain = email[index + 1:]

print(f"Username : {username}\nDomain : {domain}")