sign = input("Chose the operation(*/+-): ")
a = int(input("First number: "))
b = int(input("Second number: "))

if sign == "*":
    print(f"a * b = {a*b}")
elif sign == "/":
    print(f"a / b = {a/b}")
elif sign == "+":
    print(f"a + b = {a+b}")
else:
    print(f"a - b = {a-b}")