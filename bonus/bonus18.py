import FreeSimpleGUI as sg
from zip_extractor_bonus18 import extract_file

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.InputText(key="first_input")
button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.InputText(key="second_input")
button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")

output_label = sg.Text(key="output", text_color = "green")

window = sg.Window("Archive Extractor", layout=[[label1, input1, button1],
                                                [label2, input2, button2],
                                                [extract_button, output_label]])
while True:
    event,values = window.read()
    print(event)
    print(values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    extract_file(archive_path, dest_dir)
    window["output"].update(value="Extraction Successful")

window.close()