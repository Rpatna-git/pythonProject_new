import FreeSimpleGUI as sg

label=sg.Text("enter to list item")
inputext=sg.InputText("Enter item here")
add_button=sg.Button("Add")
window=sg.Window('My TODO List App',layout=[[label],[inputext, add_button]])
window.read()
window.close()

