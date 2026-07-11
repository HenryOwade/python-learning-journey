attempts = 0
attempts_limit = 3
correct_pin = "1234"

while attempts < attempts_limit:
    pin = input("Enter Your 4-digit PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        remaining_attempts = attempts_limit - attempts

        if remaining_attempts > 0:
            print("Wrong PIN")
            print(f"Attempts Remaining: {remaining_attempts}")

else:
    print("Your account has been blocked")