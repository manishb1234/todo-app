

"""
def convert1(value):
    parts = feet_inches.split(" ") #returns a list
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet* 0.3048 + inches* 0.0254
    return meters

result1 = convert1(feet_inches)
"""
from files.bonus.convert13 import convert
from files.bonus.parse13 import parse

#Decoupling - Parsing and converting into 2 different modules

feet_inches = input("Enter feet and inches : ")

#feet_inches_tuple = parse(feet_inches)
f,i = parse(feet_inches)
print("fi",f, i)
result = convert(f, i)

print(f"{result} meters")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


