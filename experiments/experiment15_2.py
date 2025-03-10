import csv

with open("customers-100.csv", "r") as file:
    print(csv.reader(file))
    data = list(csv.reader(file)) #list of lists

for i in data:
    print(i)

index = input("Enter index: ")

for row in data:
    if row[0] == index:
        print(row[1:])