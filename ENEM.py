from tkinter import * 
win = Tk()
def media():
   me = float(reda_entrada.get())+float(ling_entrada.get())+float(huma_entrada.get())+float(natu_entrada.get())+float(Mate_entrada.get())
   med = me/5
   notafinal["text"] = f'Média: {med}'
#ajustar tamanho da janela
win.maxsize(width=400, height=350)
win.minsize(width=400, height=350)
#cor da janela
#win["bg"] = "blue"
#titulo da janela
win.title("Gustah Tocantins")
fonte = ("arial", "15", "bold")
fonte1 = ("arial", "13")
#titulo
titulo = Label(win, text="NOTAS DO ENEM", font=("arial","24","bold"), fg="blue")
titulo.pack()
titulo.place()
#Linguagens
ling = Label(win, text="Linguagens: ", font=fonte)
ling.pack()
ling.place(bordermode=OUTSIDE, x=10, y=40)
#Lnguagens2
ling_entrada = Entry(win, font=fonte1)
ling_entrada.pack()
ling_entrada.place(bordermode=OUTSIDE, x=135, y=40, height=25)

#Humanas
huma = Label(win, text="Humanas: ", font=fonte)
huma.pack()
huma.place(bordermode=OUTSIDE, x=10, y=80)
#humanas
huma_entrada = Entry(win, font=fonte1)
huma_entrada.pack()
huma_entrada.place(bordermode=OUTSIDE, x=135, y=80, height=25)

#Natureza
natu = Label(win, text="Natureza: ", font=fonte)
natu.pack()
natu.place(bordermode=OUTSIDE, x=10, y=120)
#Natureza
natu_entrada = Entry(win, font=fonte1)
natu_entrada.pack()
natu_entrada.place(bordermode=OUTSIDE, x=135, y=120, height=25)
#Matematica
Mate = Label(win, text="Matematica: ", font=fonte)
Mate.pack()
Mate.place(bordermode=OUTSIDE, x=10, y=160)
#Matematica2
Mate_entrada = Entry(win, font=fonte1)
Mate_entrada.pack()
Mate_entrada.place(bordermode=OUTSIDE, x=135, y=160, height=25)
#Redação
reda = Label(win, text="Redação: ", font=fonte)
reda.pack()
reda.place(bordermode=OUTSIDE, x=10, y=200)
#redação
reda_entrada = Entry(win, font=fonte1)
reda_entrada.pack()
reda_entrada.place(bordermode=OUTSIDE, x=135, y=200, height=25)

#Calcular
botao = Button(win, text="Calcular", command=media, bg="blue",font=("arial", "15", "bold"), fg="white")
botao.pack()
botao.place(bordermode=OUTSIDE, x=150, y=250, width=90, height=30)

#Resultado
notafinal = Label(win, text="Média: ", font=("arial","25","bold"), fg="green")
notafinal.pack()
notafinal.place(bordermode=OUTSIDE, x=10,y=300)
win.mainloop()
