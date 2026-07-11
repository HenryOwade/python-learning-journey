weight = int(input("Enter your weight in either kgs or pounds: "))
unit = input("Kgs(K) or Lbs(L) ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your weight is {converted} kilograms")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds")