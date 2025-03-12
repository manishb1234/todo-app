import functions

import FreeSimpleGUI as sg

label = sg.Text("Enter a todo")
inputBox = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My to-do app', layout=[[label],[inputBox, add_button]])

window.read()

print("Hello")

window.close()