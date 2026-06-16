# Conditional Statements and Loops

# If Statement

num = int(input("Enter Number: "))
if num >= 0:
    print("Number is Positive")


# If-Else Statement

num = int(input("Enter the Number: "))
if num >= 0:
    print("Number is Positive")
else:
    print("Number is Negative")

# Elif Statement/ Nested Elif Statement

marks = float(input("Enter the Marks: "))

if marks >= 90:
    print("Distinction")
elif marks >= 65:
    print("First Class")
elif marks >= 45:
    print("Second Class")
elif marks >= 35:
    print("PASS")
else:
    print("FAIL")

## For Loop

fruits = ["Apples", "Mangoes", "Grapes"]

print(fruits)

for i in fruits:
    print(i)

# While Loops

count = 0
while count > 5:
    count += 1
    print(count)
