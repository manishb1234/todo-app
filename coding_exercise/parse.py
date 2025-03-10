import random

def parse(input):
    list_input = input.split(',')
    lower_bound = int(list_input[0])
    upper_bound = int(list_input[1])
    return {"lower_bound" : lower_bound, "upper_bound" : upper_bound}

while True:
    user_input = input("Enter a lower bound and an upper bound divided by a comma (e.g., 2,10): ")

    parsed = parse(user_input)

    rand = random.randint(parsed["lower_bound"], parsed["upper_bound"])

    print(rand)