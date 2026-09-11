import random
print("---Python Number Guessing Game---")
print("--------Chose your numbers-------")
while True:
    low = int(input("Starting number is: "))
    high = int(input("Last number is(bigger than starting number): "))
    if(low > high):
        print("Your numbers are wrong, please try again.")
    else:
        break
ans = random.randint(low, high)
guesses = 0 
is_running = True

while is_running:
    guess = input(f"Select a number between {low} and {high}: ")
    if(guess.isdigit()):
        guess = int(guess)
        if guess > high or guess < low:
            print("Invalid answear")
        else:
            guesses+=1
            if guess == ans:
                print(f"You guessed it in {guesses} guesses, the number is {ans}")
                is_running = 0
            elif guess < ans:
                print("The number is too low")
            else:
                print("The number is too high")
    else:
        print("Invalid guess")
