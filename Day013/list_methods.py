numbers = [2, 4, 5, 3, 3, 7]
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
numbers.insert(0, 10)
print(numbers)
numbers.remove(4)
print(numbers)
print(numbers.index(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.clear()
print(numbers)

#Write a program to remove duplicates in a list
numbers = [1, 2, 2, 3, 3, 5, 4, 7, 8]
print(numbers)
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
