def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(first_name = "Henry", last_name = "Owade")
greet_user(first_name = "Mary", last_name = "Anyango")
print("Finish")

def create_account(name, age, country, email, phone, occupation):
    print("==== ACCOUNT DETAILS ====")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone}")
    print(f"Occupation: {occupation}")
    print("==========================")
    print("= ACCOUNT CREATED SUCCESSFULLY =")


print("Welcome to Registration System")

create_account(
    name = "Henry Owade",
    age = 24,
    country = "Kenya",
    email = "henryowade@gmail.com",
    phone = "0114364956",
    occupation = "Electronics and Computer Engineer"
)

print("Thank you for registering")


