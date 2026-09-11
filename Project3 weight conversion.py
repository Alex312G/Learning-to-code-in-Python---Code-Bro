weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds: ")
if unit == "kilograms":
    print(f"Your weight in pounds : {2.20462*weight}")
elif unit == "pounds":
    print(f"Your weight in kilograms : {0.45359*weight}")
else:
    print("Eroare")
