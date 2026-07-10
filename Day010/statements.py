# Python Statements

a = 10
b = 14
c = 11; d = 24

print("Area of a Rectangle = ", a * c)

# Multi-Line Statements
## Use line continuation character (\)
## This is called explicit continuation
addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70
print(addition)

## Use parentheses ()
## This is called implicit continuation
addition = (10 + 20 +
            30 + 40 +
            50 + 60 + 70)
print(addition)

## Delete (del) statement
x = 10
y = 30
print(x, y)

# del(x, y)
# print(x, y)

# return Statement
def addition(num1, num2):
    return num1 + num2
result = addition(10, 20)
print(result)

def my_function(num1, num2, num3, num4, num5):
    return num1 + num2 - num3 * num4 / num5

result = my_function(10, 20, 30, 40, 50)
print(result)

x = 15
y = 6
print(x / y)
print(x // y)
print(x % y)




