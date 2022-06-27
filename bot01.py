import pyautogui as pi
import PySimpleGUI as sg
from time import sleep

qt = []
for i in range(1, 1001):
    qt.append(int(i))

sg.theme('GreenTan')
layout = [
    [sg.Text('Quantas mensagens deseja enviar?', font=('bold, 15')), sg.Combo(qt, key='qtde', size=(10, 1))],
    [sg.Text('Digite a mensagem aqui!', font=('bold, 15'))],
    [sg.Multiline(size=(36, 10), key='msg', font=('bold, 15'))],
    [sg.Button('Enviar', font=('bold, 15'))]
]

janela = sg.Window('BOT', layout)
while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
    if values['qtde'] == '':
        sg.popup_error('Selecione quantas mensagens deseja enviar!', font=('bold, 12'))
    elif values['msg'] == '':
        sg.popup_error('Digite a mensagem!!!', font=('bold, 12'))
    else:
        a = values['qtde']
        if events == 'Enviar':
            sleep(2)
            for i in range(a):
                pi.write(values['msg'])
                pi.press('Enter')
            sg.popup('SPAM EFETUADO COM SUCESSO!!!', font=('bold, 12'))
