temperature = 30

if temperature >= 30:
    print("It is a hot day")
else:
    print("It is not a hot day")

name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")