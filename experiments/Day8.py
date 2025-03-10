with open("../files/doc.txt") as file:
    print("hello")

#file.read() file closes implicitly, variable exists but that variable is associated with a closed file outside  with
#ValueError: I/O operation on closed file.
#default argument of  open is 'r', check help(open)

with open("../files/doc.txt") as file:
    file.read()
    content = file.read()

print(content)
print(content)

#no output  of this as read() method is exhausted and cursor moves to end of line
