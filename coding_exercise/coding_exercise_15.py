#Your task is to create a program that generates a random whole number
'''
Output
Enter the lower bound: 1
Enter the upper bound: 10
7
'''

import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

random_number = random.randrange(lower_bound, upper_bound+1) #add 1 to upper_bound because randrange does not include the upper_bound number.
print(random_number)
#or use randint()

def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """

