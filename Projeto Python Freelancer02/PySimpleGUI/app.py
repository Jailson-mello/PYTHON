import PySimpleGUI as sg

# Definir o tema da janela
sg.theme('reddit')

# Definir o layout da janela
janela_principal = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher pasta anexo', target='input_anexos'),
     sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher pasta planilha', target='input_planilha'),
     sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]
]

# Criar a janela
janela = sg.Window('Principal', layout=janela_principal)

# Loop de eventos
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break

# Fechar a janela
janela.close()
