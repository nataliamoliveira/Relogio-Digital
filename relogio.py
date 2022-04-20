from datetime import datetime
from tkinter import *

# Definição das opções de cores do relógio

cor1 = "#DDA0DD" # Plum
cor2 = "#9370DB" # Purple
cor3 = "#FFFFFF" # Branco
cor4 = "#000000" # Preto
cor5 = "#808080" # Cinza
cor6 = "#4682B4" # Azul

fundo = cor4
cor = cor1

# Parâmetros da janela onde o relógio será exibido
janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=fundo)

# Função def para mostrar os dados obtidos
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "   " + str(dia) +
              "/" + str(mes) + "/" + (ano))


l1 = Label(janela, text="10:05:05", font=('Arial  50'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(janela,  font=('Arial  15'), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)


# Execução
relogio()
janela.mainloop()
