
def Show_Balance():
    print(f"Your balance is: {balance:5.2f}€")
def Deposit():
    deposited = int(input("How much money do you want to deposit?: "))
    if(deposited < 0):
        print("That is not a valid amount")
        return 0
    return deposited
def Withdraw():
    withdrawn = int(input("Enter the withdrawn amount: "))
    if(withdrawn > balance):
        print("Insufficient funds")
        return 0
    elif withdrawn < 0:
        print("Amount should be greater than 0")
    else:
        return withdrawn

balance = 0
is_running = True
while is_running:
    print("----Banca Transilvania----")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")
    if choice == '1':
        Show_Balance()
    elif choice == '2':
        balance += Deposit()
    elif choice == '3':
        balance -= Withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Error! Write a valid command!")