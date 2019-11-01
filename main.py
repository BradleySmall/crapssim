import random

ROLLS = [[random.randint(1, 6), random.randint(1, 6)] for _ in range(1000000)]

print({x: [sum(roll) for roll in ROLLS].count(x) for x in range(2, 13)})
# print(rolls)

with open("rolls.txt", "w") as file:
    for a, b in ROLLS:
        file.write(f"{a},{b}\n")
