menu = {"cartoafe": 2.5,
        "pepeni":3,
        "limonada":4,
        "jucarie": 5,
        "burgar":3,
        "chifla":4,
        "peste":5}
cart = []
total = 0
print("----Menu----")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f} dollars")
print("---------")
while True:
    food = input("Select an item(q for quit): ")
    if(food.lower() == "q"):
        break
    elif menu.get(food.lower()) is not None:
        cart.append(food.lower())
print("Your items are: ", end = " ")
for food in cart:
    total+=menu.get(food)
    print(food, end = " ")
print()
print(f"Your total is: {total:.2f} dollars")