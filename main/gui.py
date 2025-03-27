
import functions

import FreeSimpleGUI as sg

label = sg.Text("Enter a todo")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events = True, size=[45 ,10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My to-do app', layout=[[label],
                                           [inputBox, add_button],
                                           [listbox, edit_button, complete_button],
                                           [exit_button]])
while True:
    event, values= window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            todo_to_be_added = values['todo'] + '\n'
            todos.append(todo_to_be_added)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todos=functions.get_todos()
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case 'Complete':
            todos = functions.get_todos()
            todo_to_complete = values['todos'][0]

            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break




print("Hello")

window.close()