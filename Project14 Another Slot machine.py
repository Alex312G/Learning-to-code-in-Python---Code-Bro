#Pacaneaua
import random
def spin_row():
    symbols = ("🍒", "🍉", "🍋", "🔔", "⭐")
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100
    is_running = 1
    print("-------------------------------")
    print("Welcome to your worst nightmare")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("-------------------------------")
    while balance > 0 and is_running:
        print(f"Current balance is: {balance:5.2f}€")
        bet = input("Place your bet: ")
        if not bet.isdigit():
            print("Please enter a valid amount!")
            continue
        bet = int(bet)
        if bet <= balance and bet > 0:
            balance -= bet
            row = spin_row()
            print("Spinning...\n")
            print_row(row)
            print()
            payout = get_payout(row, bet)
            if payout > 0:
                print(f"You won ${payout}")
            else:
                print("Try again!")
            balance+=payout
        else:
            print("Please enter a valid amount!")
            continue
        play_again = input("Do you want to spin again? (Y/N): ")
        if play_again.upper() != 'Y':
            is_running = 0 
    print("--------------------------------------------")
    print(f"Game over! Your final balance is ${balance}")
    print("--------------------------------------------")
        
if __name__ == '__main__':
    main()