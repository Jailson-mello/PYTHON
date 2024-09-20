# CRIANDO O SISTEMA INTERFACE GRÁFICA

# CAMINHO PARA ENTRAR NA PASTA, SAINDO DO DISCO (C) ENTRANDO NO DISCO (E) / PELO TERMINAL
# cd "E:\ARQUIVOS SSD\DOCUMENTOS GERAL JAILSON\CONTROLE COMPLETO\TRABALHO - REPOSITORIO GITHUB\PYTHON"

# Instalando a Biblioteca interface gráfica -  PySimpleGUI
# pip install pysimplegui

# COMANDO PARA TESTE PARA EXIBIR A MENSAGEM DA PYSMPLEGUI, ... CLIQUE NO PLAYER, PARA EXIBIR A MENSAGEM
# import PySimpleGUI as sg
# sg.popup('ok')

# acompanhar a aula -   https://www.youtube.com/watch?v=06vmYgk2Fys  - no minuto 12:00

# SITE PARA CONFIGURAR A LICENÇA
# https://pysimplegui.com/pricingMurilo BarrosCadeira
# https://pysimplegui.com/sign-up?pack=Hobbyst

# CONTA CRIADA
# Jailson Melo / jailsonaranha38@gmail.com / G-91456962123

# INFORMAÇÕES APÓS A CRIAÇÃO DA CONTA
# https://pysimplegui.com/account/license-information/non-commercial


import PySimpleGUI as sg

# Definir o tema da janela
sg.theme('reddit')

# Definir o layout da janela
janela_principal = [
    [sg.Text('Cliente'), sg.Input(key='cliente')],
    [sg.Text('Produto'), sg.Input(key='produto')],
    [sg.Text('Quantidade'), sg.Input(key='quantidade')],
    [sg.Text('Categoria do Produto'), sg.Input(key='categoriaProduto')],
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


# Definir o tema da janela
sg.theme('reddit')

# Definir o layout da janela
janela_principal = [
    [sg.Text('Cliente'), sg.Input(key='cliente')],
    [sg.Text('Produto'), sg.Input(key='produto')],
    [sg.Text('Quantidade'), sg.Input(key='quantidade')],
    [sg.Text('Categoria do Produto'), sg.Input(key='categoriaProduto')],
    [sg.Button('Salvar')]
]

# Criar a janela
janela = sg.Window('Principal', layout=janela_principal)

# Loop de eventos
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        # Aqui você pode adicionar o código para salvar os dados, por exemplo:
        # cliente = values['cliente']
        # produto = values['produto']
        # quantidade = values['quantidade']
        # categoriaProduto = values['categoriaProduto']

        # Limpar os campos de entrada
        janela['cliente'].update('')
        janela['produto'].update('')
        janela['quantidade'].update('')
        janela['categoriaProduto'].update('')

# Fechar a janela
janela.close()
