user_prompt  = "Enter a todo:" todo1=input(user_prompt)
#todo1 var is associated with output of  the input function- a string
todo2 = input(user_prompt)
todo3 = input(user_prompt)

#whitespace doesnt  matter in python interpreter
#expressions 1 in each line

print(todo1, todo2, todo3) #success.print can take many arg
#no yes no #print doesnt return anything, so cant store it in a var
print(todo1)
print(todo2)
print(todo3)

print([todo1,todo2,todo3])
#['no', 'yes', 'no']

print(type(user_prompt))
print(type(todo1))
#you get the type of the value that the var is associated with