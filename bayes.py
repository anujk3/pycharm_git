import numpy as np


def coin_tosses(n=10, p=0.5):
    total = sum(np.random.choice(np.arange(2), size=10, p=[p, 1 - p]))
    if total == n:
        return 1
    else:
        return 0


bag = ["F" for i in range(99)] + ["UF"]

a = 0  # number of times we see 10 heads in a row and coin was unfair
b = 0  # number of times we see 10 heads in a row

for _ in range(1000000):
    pick_coin = bag[np.random.randint(low=0, high=100)]
    if pick_coin == "F":
        b += coin_tosses(n=10, p=0.5)
    else:
        a += coin_tosses(n=10, p=0.0)

print(a / (a + b))
