import glob

myfiles = glob.glob("*.txt")
output = []
for filepath in myfiles:
    with open(filepath, 'r') as file:
        #output = output + file.readlines()
        print(file.read().upper())

print(myfiles)
print(output)

