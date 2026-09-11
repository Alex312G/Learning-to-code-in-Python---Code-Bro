#reading temp
unit = input("Is this temperature in Celsius or Fahrenheit (C/F) : ")
temp = float(input("Temperature is : "))

if(unit == "C"):
    print(f"Your temperature in Fahrenheit is : {(9*temp)/5+32}")
elif unit == "F":
    
    print(f"Your temperature in Celsius is : {(temp-32) * 5 / 9}")
else:
    print(f"Your unit {unit} is wong")