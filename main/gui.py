# see how to create .exe, giving error section 18, video 177, giving error while running pyinstaller in venv
import functions
import FreeSimpleGUI as sg
import time
import os

if  not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass


sg.theme("Black")

clock = sg.Text("", key='clock')
label = sg.Text("Enter a todo")
inputBox = sg.InputText(tooltip="Enter todo", key="todo")
#add_button = sg.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2",
#                       tooltip="Add Todo", key="Add")
#event takes either the label 'add or  the key 'Add'
add_button = sg.Button("Add")
listbox = sg.Listbox(values=functions.get_todos(), key="todos",
                     enable_events = True, size=[45 ,10])

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My to-do app', layout=[[clock],
                                           [label],
                                           [inputBox, add_button],
                                           [listbox, edit_button, complete_button],
                                           [exit_button]],
                                        font=('Helvetica', 20))
while True:
    event, values= window.read(timeout=200) #milliseconds allows running the window every millisecond
    window["clock"].update(value=time.strftime("%Y-%m-%d (%b) %H:%M:%S"))
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
            try:
                todos=functions.get_todos()
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)

            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))

        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_to_complete = values['todos'][0]

                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica, 20'))


        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break




print("Hello")

window.close()