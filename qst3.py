from tkinter import *

def gerar_iniciais(nome):
    letras = ''
    
    for letra in nome:
        if letra.isupper():
            letras = letras + letra    
        
    letras_min = letras.lower()
    return letras_min

def gerar_email():
    nome = valor1.get()
    email = gerar_iniciais(nome) + '@empresa.com.br'
    
    msg['text']= email

app=Tk()

frame1 = Frame(pady=3)
frame1.pack()

frame2 = Frame(pady=6)
frame2.pack()

frame3 = Frame(pady=3)
frame3.pack()

Label(frame1,text='Nome :').pack(side=LEFT)
valor1=Entry(frame1,width=50)
valor1.pack(side=LEFT)

gerar=Button(frame2, text='Gerar e-mail',command=gerar_email)
gerar.pack(side=LEFT)

Label(frame3,text='E-mail: ').pack(side=LEFT)
msg=Label(frame3,width=30)
msg.pack(side=LEFT)

app.mainloop()