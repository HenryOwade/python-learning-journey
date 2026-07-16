# This project is like rolling a dice, it should generate two 
# numbers each time we roll a dice

import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  #This returns values as a tuple. No need to add parenthesis
    

dice = Dice()
print(dice.roll())