# Using of Random Number. This program is Giving generating  random number for dice.
# First we have to import Random number Function
import random
# Define a function that will take number from 1 to the entered value of "num".


def roll_dice(num):

    return random.randint(1, num)

# This line print that calling the roll_dice function and printing the value.


print("your number is:", roll_dice(6))
