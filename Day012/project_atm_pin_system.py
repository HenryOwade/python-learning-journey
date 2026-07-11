# Challenge: ATM PIN System
## Scenario
## Imagine you're building a simple ATM.

## The user has 3 attempts to enter the correct PIN.
## The correct PIN is: 1234

# Requirements
## Ask the user to enter the PIN.
## If the PIN is correct:
##  Access Granted
# Then stop the program immediately.

## If the PIN is incorrect:
## Display
## Incorrect PIN

## Decrease the remaining attempts.

## For example:
## Attempts left: 2

## If all three attempts are used:
## Display
## Your account has been locked.

attempts = 3

while attempts > 0:
    pin = input("Enter your 4-digit PIN")
    
    if not pin.isdigit():
        print("PIN must have numbers only")
        continue
    
    if pin == "1234":
        print("Access Granted")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("Incorrect PIN")
            print(f"Attempts remaining: {attempts}")
        else:
            print("Your account has been locked")
        

        


