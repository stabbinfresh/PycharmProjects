import PySimpleGUI as sg
from converters import convert

sg.theme("DarkBlack")

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convert Feet and Inches to Meters",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = round(convert(feet, inches), 3)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()
