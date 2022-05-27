import requests
from tkinter import *


def calculo_imc():
    kg = float(caixa_peso.get())
    altura = float(caixa_altura.get())

    imc = round(kg / (altura * altura), 2)

    resultado_imc["text"] = imc

    if imc < 18.5:
        laudo_imc["text"] = "Voce esta ABAIXO DO PESO"
    elif imc >= 18.5 and imc <= 24.9:
        laudo_imc["text"] = "Voce esta no PESO IDEAL"
    elif imc >= 25 and imc <= 29.9:
        laudo_imc["text"] = "Voce esta com SOBREPESO"
    elif imc >= 30 and imc <= 34.99:
        laudo_imc["text"] = "Voce esta com OBESIDADE GRAU 1"
    elif imc >= 35 and imc <= 39.99:
        laudo_imc["text"] = "Voce esta com OBESIDADE SEVERA"
    else:
        laudo_imc["text"] = "Voce esta com OBESIDADE MORBIDA"



janela = Tk()
janela.title("Calculadora de IMC")

texto_peso = Label(janela, text="Quantos kg voce tem?")
texto_peso.grid(column=0, row=0, sticky=W)
caixa_peso = Entry(janela, background="white", width=25)
caixa_peso.grid(column=1, row=0)

texto_altura = Label(janela, text="Qual sua altura?")
texto_altura.grid(column=0, row=1, sticky=W)
caixa_altura = Entry(janela, background="white", width=25)
caixa_altura.grid(column=1, row=1)

botao_calcular = Button(janela, text="Calcular", command=calculo_imc, width=15, background="gray")
botao_calcular.grid(column=0, row=2, padx=0, pady=20)

titulo_resultado_imc = Label(janela, text="Seu IMC é de =")
titulo_resultado_imc.grid(column=0, row=3, sticky=E)
resultado_imc = Label(janela, text="", foreground='green')
resultado_imc.grid(column=1, row=3, sticky=W)

titulo_laudo = Label(janela, text="Resultado =")
titulo_laudo.grid(column=0, row=4, sticky=E)
laudo_imc = Label(janela, text="", foreground='green')
laudo_imc.grid(column=1, row=4, sticky=W)


janela.mainloop()
