#Making A TO DO List

'''
Step 1: Have the user input add input, show or exit items
Step n: Add a new feature called edit where the user can edit the existing list items
'''

while True:
    user_prompt = input("Enter an option: add, show, edit,complete or exit: ")
    user_prompt = user_prompt.strip()

    #match case has no help, as its a keyword

    match user_prompt:
        case 'add' in user_prompt:
            todo = input("Enter a todo item: ") + "\n"

            """Method 1
            file = open('todos.txt', 'r')
            
            todos = file.readlines() #returns a list where each line is an element
            print(todos)
            file.close()"""

            with open('todos.txt', 'r') as file:
                  todos = file.readlines()

            todos.append(todo)
            print(todos)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            #Method1 to remove blank line of print(row) in console
            """new_todos = []
            for item1 in todos:
                item1 = item1.strip('\n')
                new_todos.append(item1)"""

            """Method2 to remove blank line of print(row) in console
            List Comprehension
            new_todos = [item.strip('\n') for item in todos]
            """#for loop in 1 line

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                    item = item.strip("\n")
                    row = f"{index+1}-{item}"
                    print(row)
                #print(index, item) #index and item still variables outside the loop,print last value

        case 'edit':
            print("The complete list is: ", todos)
            index = int(input("Enter the position of the item you want to edit: "))#for  user, position is index 1
            index = index-1
            newItem = input("Enter the new edited item: ")

            with open("todos.txt", 'r') as file:
                todos = file.readlines() #thats why file.readlines() is stored as a list, so it can be edited

                todos[index] = newItem + '\n'
                print(todos)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter the number of item to be removed: "))
            number = number - 1 #offsetting index by 1 for user

            with open("todos.txt", 'r') as file:
                todos = file.readlines()
                todos.pop(number)
                print(todos)

            with open("todos.txt", 'w') as  file:
                file.writelines(todos)

        case 'exit':
            break;
        case _ :
            print('Invalid option, enter correct option again:')

print("Bye")



#mylist = [1,2,3]
#a = enumerate(mylist)
#a
'''<enumerate object at 0x00000297A482E480>
str(a)
'<enumerate object at 0x00000297A482E480>'
list(a)
[(0, 1), (1, 2), (2, 3)]'''

'''enumerate object is a collection of  tuples'''

