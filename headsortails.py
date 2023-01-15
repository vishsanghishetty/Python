import random

print("Heads or Tails ??")

random_side = random.randint(0, 1)

if random_side == 0:
    print(f"Tossing the coin \n You got 0, 0 means Tails")
else:
    print(f"Tossing the coin \n You got 1, 1 means Heads")


