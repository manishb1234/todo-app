#Feet To Inches Convertor, add an exit button and apply a black theme

import FreeSimpleGUI as sg
from section_18_coding_exercise_1_backend import convert


sg.theme("Black")

feet_label = sg.Text("Enter Feet:")
feet_input = sg.InputText("", key="feet")

inches_label = sg.Text("Enter Inches:")
inches_input = sg.InputText("", key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")

output_label = sg.Text(key="output", text_color = "green")

col1 = sg.Column([[feet_label], [inches_label]], justification="right")
col2 = sg.Column([[feet_input],[inches_input]], justification="left")
col3 = sg.Column([[sg.Push(),convert_button],[sg.Push(),exit_button]], justification="left")
window = sg.Window("Convertor",
                   layout=[[col1, col2,col3],[output_label]])
while True:
    event,values = window.read()
    print(event)
    print(values)
    #event is Convert
    #values are {'feet': '3', 'inches': '4'}
    match event:
        case 'Convert':
            try:
                feet_value = int(values["feet"])
                inches_value = int(values["inches"])

                if feet_value<0 or inches_value < 0:
                    raise ValueError

                metres_value = convert(feet_value, inches_value)
                print(feet_value, type(feet_value))
                print(inches_value, type(inches_value))
                print(metres_value, type(metres_value))

                result = f"{feet_value} feet & {inches_value} inches = {metres_value} metres"

                window["output"].update(value=result)
            except ValueError:
                sg.popup("Please enter Feet and inches in whole numbers", font=("Helvetica", 10))

        case'Exit':
            break
        case sg.WIN_CLOSED:
            break


window.close()