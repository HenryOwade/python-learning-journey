for item in "Python":
    print(item)

for item in ["Henry", "John", "Jovan"]:
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

# Write a program that calculate the total prices in this imaginary shopping cart.
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print(f"The total cost of all the items is {total}")

name = "Henry"
print(f"Name in uppercase is {name.upper()}")
print(f"Number of characters in the name is {len(name)}")
