import PySimpleGUI as sg
import PIL
from converter import convertImage
import os

#Define o tema do layout
sg.theme("DarkRed")

#Define o conteudo da tela
layout = [
    [sg.Text("Selecione um arquivo:"), sg.Input(), sg.FileBrowse(key="InputImage")],
    [sg.Text("Selecione um formato:"),sg.Combo(["JPG", "PNG", "PDF", "ICO"], default_value="JPG",key='FormatOption')],
    [sg.Button("Converter")]
]

#Cria o contexto da janela
window = sg.Window("Light Image Converter", layout, icon="imgs/icon.ico")

while True:
    event, values = window.read()

    #verifica se a janela foi fechada, se ocorrer, finaliza a aplicação
    if event == sg.WINDOW_CLOSED or event == "Quit":
        break
    if event == "Converter": #Chamada a função de conversão
        convertImage(values['InputImage'], values['FormatOption'])
        sg.popup("Imagem convertida!")

window.close()