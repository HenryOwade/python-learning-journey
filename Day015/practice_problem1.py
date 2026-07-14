# Exercise 1: Arithmetic Product and Conditional Logic

# Write a Python function that accepts two integer numbers. 
# If the product of the two numbers is less than or equal to 1000, 
# return their product; otherwise, return their sum.

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

def calculate(number1, number2):
    product = number1 * number2

    if product <= 1000:
        return product
    else:
        return number1 + number2
    

result = calculate(number1, number2)

print("Result:", result)


