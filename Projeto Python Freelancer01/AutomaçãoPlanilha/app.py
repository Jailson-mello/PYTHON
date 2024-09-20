# PRECISO TER UM BOOT ASSISTENTE QUE FAÇA MINHAS FUNÇÕES DE LANÇAMENTO CONTÁBIL DA EMPRESA QUE TRABALHO, POIS O PRÓPRIO
# SISTEMA É MUITO MASSANTE, E GOSTARIA DE FAZER OS LANÇAMENTOS NO EXCEL, ENTREGAR AO BOT O EXCEL PRONTO PARA O BOT IR LANÇANDO
# ENQUANTO FAÇO OUTRAS ATIVIDADES. TENTEI CRIAR UM AQUI PELOS VÍDEOS DO CANAL, O pyautogui FUNCIONA PERFEITAMENTE, MAS NA HORA
# DE LER O .txt OU ALGUM OUTRO ARQUIVO .xlsx ELE AVISA PELO PYLINT QUE ESTÁ ERRADO A LINHA DE CÓDIGO, E POR ISSO NA HORA DE
# EXECUTAR OS PARÂMETROS TRAVA NA HORA DE LANÇAR COM OS DADOS. PRECISO DE AJUDA URGENTIMENTE


# ------------------------------------------------------------------------------------------------------------------------------
# ESSE PROJETO ESTÁ RODANDO ATÉ O MOMENTO NO DISCO LOCAL ( C:\ )
# cd "C:\AppIfam\PYTHON\Projeto Python Freelancer01\AutomaçãoPlanilha"

# CAMINHO PARA ENTRAR NA PASTA, SAINDO DO DISCO (C) ENTRANDO NO DISCO (E) / PELO TERMINAL
# cd "E:\ARQUIVOS SSD\DOCUMENTOS GERAL JAILSON\CONTROLE COMPLETO\TRABALHO - REPOSITORIO GITHUB\PYTHON"

# CRIANDO AMBIENTE VIRTUALL
# python -m venv ambienteVirtual

# ATIVANDO AMBIENTE VIRTUAL
# .\ambienteVirtual\Scripts\activate

# BIBLIOTECAS USADAS NESSE PROJETO
# Manipular planilhas excel - openpyxl
# automação de mouse e teclado - pyautogui
# pip install openpyxl
# pip install pyautogui

# BIBLIOTECA MOVIMENTAÇÃO MOUSE
# pip install mouseinfo
# depois de instalar digite - python
# depois digite - from mouseinfo import mouseInfo
# e por ultimo - mouseInfo()

# ---------------------------------------------------------------------------------------------------------
# AULA - https://www.youtube.com/watch?v=LwTbvEIOsKI&list=PLnNURxKyyLIJ5ftIIYFLNNLyCmBx5uXYM
# A PASTA DA INTERFACE GRÁFICA ESTÁ EM OUTRO DIRETÓRIO

# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook(
    'vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    # nome
    pyautogui.click(488, 335, duration=1.5)
    pyautogui.write(linha[0].value)
    # produto
    pyautogui.click(500, 361, duration=1.5)
    pyautogui.write(linha[1].value)
    # quantidade
    pyautogui.click(520, 386, duration=1.5)
    pyautogui.write(str(linha[2].value))
    # categoria
    pyautogui.click(574, 411, duration=1.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(448, 439, duration=1.5)
    # pyautogui.click(1256, 581, duration=1.5)


