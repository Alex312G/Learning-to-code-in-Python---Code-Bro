
principle = 0 
rate = 0
time = 0

while principle <= 0:
    principle = float(input("What is the principle: "))
    if principle <= 0:
        print("The principle is incorrect")

while rate <= 0:
    rate = float(input("What is the rate (0-100): "))
    if rate <= 0:
        print("The rate is incorrect")


while time <= 0:
    time = int(input("What is the time period (years): "))
    if time <= 0:
        print("The time is incorrect")

print(f"Your balance after {time} year/s: {principle * pow(1 + rate/12, time):+.2f}")