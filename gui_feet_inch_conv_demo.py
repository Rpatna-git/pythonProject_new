import FreeSimpleGUI as sg

label1=sg.Text("Enter Feet:")
textb1=sg.InputText("")
label2=sg.Text("Enter inches:")
textb2=sg.InputText("")
button1=sg.Button("Convert")

window=sg.Window('Converter',layout =[[label1,textb1],[label2,textb2],[button1]])
window.read()
window.close()
