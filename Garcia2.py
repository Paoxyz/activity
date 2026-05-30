import random

bag = ["Red"] * 5 + ["Blue"] * 3 + ["Green"] * 2

red = 0
blue = 0
green = 0

for _ in range(500):
    ball = random.choice(bag)

    if ball == "Red":
        red += 1
    elif ball == "Blue":
        blue += 1
    else:
        green += 1

print("Red Probability:", red / 500)
print("Blue Probability:", blue / 500)
print("Green Probability:", green / 500)
