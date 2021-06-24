from currency import rates
import PySimpleGUI as sg


layout = []
for k,v in rates().items():
    layout.append([sg.Text(f'{k} - {v}')])

layout.append([sg.OK(), sg.Cancel()])

window = sg.Window('Currencies', layout, location=(0,0))


event, values = window.read()

window.close()