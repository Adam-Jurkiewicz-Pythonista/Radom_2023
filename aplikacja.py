from mail_funcs.email_functions import mail_report

import PySimpleGUI as sg


# All the stuff inside your window.
layout = [  [sg.Text('Adam Jurkiewicz')],
            [sg.Text('Wprowadź tekst w wierszu 2'), sg.InputText()],
            [sg.Text('Wprowadź tekst w wierszu 3'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('MAIL'), sg.Button('KONIEC')],
            ]

# Create the Window
window = sg.Window('Nasze okienko', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        sg.popup_annoying("HEJ - nie klikaj X")
    elif event == 'KONIEC': # if user closes window or clicks cancel
        break
    elif event == "MAIL":
        sg.popup("wysyłam maila")

    # w innym przypadku (a więc OK) - sprawdzamy IP
    #


    print(f'You entered {values=}')
    if values[1] == "END":
        print("Endzik")

window.close()