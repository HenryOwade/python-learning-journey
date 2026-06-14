# Day003

## Strings

first_name = "john"
second_name = "conner"

Full_name = first_name + " " + second_name

print(Full_name)



text = "Python Programming"

length = len(text)

# Checking and printing the length

print("The length of the given string is :", length)

# Converting to Uppercase and Lowercase

print("Text in Uppercase:", text.upper())
print("Text in lowercase:", text.lower())

# String Slicing

text = "Learn Python with Simplilearn"

print("The first 12 characters are:", text[:12])
print("The rest of the characters after 12 char are:", text[12:])

# Text Matching and Replacing

text = "I like programming in Java"
next_text = text.replace("Java", "Python")

print(next_text)

# Check if a specific part of a string is present

text = "I like Programing in Python"

if "Python" in text:
    print("Text is Found")

else:
    print("Text is Not Found")

text = "I like programming in Java"

if "Python" in text:
    print("Text is Found")

else:
    print("Text is NOT Found")
    


    





