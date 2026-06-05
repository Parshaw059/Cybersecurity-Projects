Pass=input("Enter password to check the Strength of it :-")

upper = False
lower = False
digit = False
special = False

for char in Pass:
    if char.isupper():
        upper=True
    elif char.islower():
        lower=True
    elif char.isdigit():
        digit=True
    else:
        special=True

if len(Pass)>=8 and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
