import random
from pathlib import Path
for i in range(3):
    print(random.random())
    print(random.randint(10,34))


members =['John', 'Mary', 'Peter', 'Mosh']
print(random.choice(members))


class Dice:
    def roll(self):
        # for i in range(2):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        dice_values = (x, y)
        return dice_values


dice1 = Dice()
print(dice1.roll())

path=Path()
print(path.exists())
# print(path.mkdir())
# print(path.rmdir())
for file in path.glob('*'):
    print(file)


