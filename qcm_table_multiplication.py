import random
from tkinter import*
def multiplication1():
    frame2 = Frame(fenetre)
    frame2.pack_forget()
    a=random.randint(1,10)
    b=random.randint(1,10)
    mon_tuple=("combien", "font", str(a),"x", str(b), "?")
    question = (mon_tuple[0] + " " +  mon_tuple[1] + " " + mon_tuple[2] + " " +  mon_tuple[3] + " " + mon_tuple[4] + " " + mon_tuple[5])
    qcm_entry.delete(0,END)
    qcm_entry.insert(0,question)
    c=a*b
    d=random.randint(1,4)
    e=random.randint(1,100)
    f=random.randint(1,100)
    g=random.randint(1,100)
    def vert():
        fenetre. configure(bg='green')
        frame. configure(bg='green')
        label_title.configure(bg='green',fg='white')
        label_subtitle.configure(bg='green')
        frame2.pack_forget()
        frame2.configure(bg='green')
    def rouge():
        fenetre. configure(bg='red')
        frame. configure(bg='red')
        label_title.configure(bg='red',fg='white')
        label_subtitle.configure(bg='red')
        frame2.configure(bg='red')

    def mult2():

        button_a=Button(frame2,text= c, command=vert, font =("times",20, 'italic'))
        button_a.grid(row=0, column=0, sticky=W, padx = 25)
        button_b=Button(frame2,text= e,command=rouge, font =("times",20, 'italic'))
        button_b.grid(row=0, column=1, sticky=W, padx = 25)
        button_c=Button(frame2,text= f,command=rouge, font =("times",20, 'italic'))
        button_c.grid(row=0, column=2, sticky=W, padx = 25)
        button_d=Button(frame2,text= g,command=rouge, font =("times",20, 'italic'))
        button_d.grid(row=0, column=3, sticky=W, padx = 25)
    def mult3():

        button_a=Button(frame2,text= e,command=rouge, font =("times",20, 'italic'))
        button_a.grid(row=0, column=0, sticky=W, padx = 25)
        button_b=Button(frame2,text= c,command=vert, font =("times",20, 'italic'))
        button_b.grid(row=0, column=1, sticky=W, padx = 25)
        button_c=Button(frame2,text= f,command=rouge, font =("times",20, 'italic'))
        button_c.grid(row=0, column=2, sticky=W, padx = 25)
        button_d=Button(frame2,text= g,command=rouge, font =("times",20, 'italic'))
        button_d.grid(row=0, column=3, sticky=W, padx = 25)
    def mult4():

        button_a=Button(frame2,text= e,command=rouge, font =("times",20, 'italic'))
        button_a.grid(row=0, column=0, sticky=W, padx = 25)
        button_b=Button(frame2,text= f,command=rouge, font =("times",20, 'italic'))
        button_b.grid(row=0, column=1, sticky=W, padx = 25)
        button_c=Button(frame2,text= c,command=vert, font =("times",20, 'italic'))
        button_c.grid(row=0, column=2, sticky=W, padx = 25)
        button_d=Button(frame2,text= g,command=rouge, font =("times",20, 'italic'))
        button_d.grid(row=0, column=3, sticky=W, padx = 25)
    def mult5():

        button_a=Button(frame2,text= e,command=rouge, font =("times",20, 'italic'))
        button_a.grid(row=0, column=0, sticky=W, padx = 25)
        button_b=Button(frame2,text= f,command=rouge, font =("times",20, 'italic'))
        button_b.grid(row=0, column=1, sticky=W, padx = 25)
        button_c=Button(frame2,text= g,command=rouge, font =("times",20, 'italic'))
        button_c.grid(row=0, column=2, sticky=W, padx = 25)
        button_d=Button(frame2,text= c,command=vert, font =("times",20, 'italic'))
        button_d.grid(row=0, column=3, sticky=W, padx = 25)

    if d==1:
        mult2()

    elif d==2:
        mult3()

    elif d==3:
        mult4()

    else:
        mult5()
    frame2.pack(expand=YES)







#creer fenetre
fenetre = Tk() #creer fenetre
fenetre.title("QCM sur les tables de multiplications") #nom fenetre
fenetre.geometry("1080x720") #taille fenetre
fenetre.minsize(480,360) #taille minimal
fenetre.iconbitmap("cahier.ico") #icone
fenetre.configure(background= "#d0e6ff") #couleur fenetre

#creer frame

frame = Frame(fenetre, bg='#d0e6ff')

#creer titre
label_title = Label(frame, text="QCM en ligne", font =("times",20, 'italic'), background= "#d0e6ff" )
label_title.pack()

#ajout second texte
label_subtitle = Label(frame, text=" ", font=("times",20, 'italic'), background= "#d0e6ff")
label_subtitle.pack()

#creer une entrÃ©e
qcm_entry = Entry(frame, font =("times",20, 'italic') )
qcm_entry.pack()


#creer bouton


valider_button = Button(frame, text="Suivant", font =("times",20, 'italic'), command=multiplication1)
valider_button.pack(pady=25, fill=X)

quitter_button = Button(frame, text="Quitter",font =("times",20, 'italic'), command=fenetre.destroy)
quitter_button.pack(fill=X)

#afficher la frame
frame.pack(expand=YES)

#afficher la fenetre
fenetre.mainloop()