names= ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names[-2])
print(names[2:])
names[0] = "Henry"
print(names)

# Write a program to find the largest number in a list
numbers = [1, 2, 3, 5, 4, 9, 6, 7, 2]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)