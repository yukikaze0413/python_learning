import random


def roll():
    (a, b) = random.randint(1, 6), random.randint(1, 6)
    print(f"({a},{b})")


roll()
