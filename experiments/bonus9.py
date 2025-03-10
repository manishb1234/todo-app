#To create a password checker program which will print Strong password if it satisfies 3 conditions -
#1. It should be greater than or equal to 7 characters long
#2. It should have at least 1 digit
#3. It should have at least 1 uppercase character
#And print weak password otherwise

password = input("Enter the password: ")

result = {}

if len(password) >= 7:
    result["length"] = True
else:
    result["length"] = False


digit = False
for i in password:
   digit = digit or i.isdigit()

if digit:
    result["digit"] = True
else:
    result["digit"] = False

upper = False
for i in password:
    upper = upper or i.isupper()

if upper:
    result["upper"] =  True
else:
    result["upper"] = False

ans = True
for i in result.values():
    ans = ans and i

if ans:
    print(result)
    print("Strong password")
else:
    print(result)
    print("Weak password")


#Can't use or case in start as need for loop to iterate over  the password
