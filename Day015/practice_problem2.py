# Exercise 2: Cumulative Sum of a Range

# Iterate through the first 10 numbers (0 - 9).
# In each iteration, print the current number, the previous number 
# and their sum.

print("Printing current and previous number and sum in range 10")
previous_number = 0

for number in range(10):
    total = number + previous_number

    print(f"Current number: {number} Previous number: {previous_number} Sum: {total}" )
    
    previous_number = number