# Making A TO DO List

'''
Step 1: Have the user input add input, show or exit items
Step n: Add a new feature called edit where the user can edit the existing list items
'''
# from todolist_lecture4 import user_prompt

import time
now = time.strftime("%Y-%m-%d (%b) %H:%M:%S")
print(now)

from modules import functions
while True:
    user_prompt = input("Enter an option: add, show, edit,complete or exit: ")
    user_prompt = user_prompt.strip()

    if user_prompt.startswith('add'):

        todo = user_prompt[4:]
        todos = functions.get_todos("../todos.txt")
        todos.append(todo + '\n')
        print(todos)

        functions.write_todos("../todos.txt", todos)

    elif user_prompt.startswith('show'):
        # Method1 to remove blank line of print(row) in console
        """new_todos = []
        for item1 in todos:
            item1 = item1.strip('\n')
            new_todos.append(item1)"""

        """Method2 to remove blank line of print(row) in console
        List Comprehension
        new_todos = [item.strip('\n') for item in todos]
        """  # for loop in 1 line

        todos = functions.get_todos("../todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
        # print(index, item) #index and item still variables outside the loop,print last value

    elif user_prompt.startswith('edit'):
        #print("The complete list is: ", todos)
        try:
            index = int(user_prompt[5:])  # for  user, position is index 1
            index = index - 1

            if index < 0 or index >= len(todos):  # Check if index is out of range
                raise IndexError

            newItem = input("Enter the new edited item: ")

            todos = functions.get_todos("../todos.txt")
            # thats why file.readlines() is stored as a list, so it can be edited

            todos[index] = newItem + '\n'
            print(todos)

            functions.write_todos("../todos.txt", todos)

        except (IndexError, ValueError):
            print("Your command is not valid. Enter command again")
            continue

    elif user_prompt.startswith('complete'):
        try:
            number = int(user_prompt[9:])
            number = number - 1  # offsetting index by 1 for user

            if number < 0 or number >= len(todos):  # Check if index is out of range
                raise IndexError

            todos = functions.get_todos("../todos.txt")

            print("The removed item is", f"{number + 1}-{todos[number]}")
            todos.pop(number)
            print(todos)

            functions.write_todos("../todos.txt", todos)
        except (ValueError, IndexError):
            print("Your command is not valid. Enter command again")
            continue

    elif user_prompt == 'exit':
        break

    else:
        print('Invalid option, enter correct option again:')


