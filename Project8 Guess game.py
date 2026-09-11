
questions = ("How many legs does an ostrich have?: ",
             "Whinch is the champion in motogp 2025?: ",
              "Where can you find Mona Lisa?: ",
              "How fast can u drive in a school zone?: ",
              "How can u stop a train?: ")
options = (("1", "2", "3"),
 ("Marc Márquez", "Marco Bezzecchi", "Alex Marquez"),
 ("Rome", "Paris", "Nice"), 
 ("30", "40", "50"), 
 ("With an rpg", "With a tank", "You can't"))
answers = (("2"), ("Marc Márquez"), ("Paris"), ("50"), ("You can't"))
guesses = []
score = 0
question_num = 0
for question in questions:
    print("-------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answear: ")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answear")
    question_num+=1
print("--------------")
print(f"Your score is: {score/ len(questions)*100}%")
print("--------------")

print("answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()
print("guess: ", end = "")
for guess in guesses:
    print(guess, end = " ")