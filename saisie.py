from turtle import heading, left, right
import xml.etree.ElementTree as e
from tkinter import *
from more_itertools import padded
#fonction de saisie:
mytree=e.parse('auteur.xml')
myroot=mytree.getroot()
def saisie_info():
    nom_info=nom.get()
    prenom_info=prenom.get()
    age_info=age.get()
    nomlivre_info=nomlivre.get()
    genre_info=genre.get()
    e.SubElement(myroot,'auteur')
    e.SubElement(myroot[len(myroot)-1],'nom')
    e.SubElement(myroot[len(myroot)-1],'prenom')
    e.SubElement(myroot[len(myroot)-1],'age')
    e.SubElement(myroot[len(myroot)-1],'nomlivre')
    e.SubElement(myroot[len(myroot)-1],'genre')
    l=[nom_info,prenom_info,age_info,nomlivre_info,genre_info]
    i=0
    for x in myroot[len(myroot)-1]:
        b=l[i]
        x.text=str(b)
        i=i+1
    mytree.write('auteur.xml')
    nom_entry.delete(0,END)
    prenom_entry.delete(0,END)
    age_entry.delete(0,END)
    genre_entry.delete(0,END)
from sympy import expand
screen=Tk()
screen.geometry("500x500")
screen.minsize(500,500)
screen.maxsize(500,500)
screen.config(background='#A6D7CA')
screen.title("Ajout d'un auteur")
head=Label(screen,text="Saisir les éléments d'un auteur",bd=1,relief=SOLID,font=('Arial',15),bg="#6E7386",fg="black",width=0,height=0)
head.pack()
nom_text=Label(text="Nom:",)
prenom_text=Label(text="Prénom:",)
age_text=Label(text="age:",)
nomlivre_text=Label(text="Le nom du livre:",)
genre_text=Label(text="genre:",)
#
nom_text.place(x=25,y=40)
prenom_text.place(x=25,y=100)
age_text.place(x=25,y=160)
nomlivre_text.place(x=25,y=220)
genre_text.place(x=25,y=280)
#
nom=StringVar()
prenom=StringVar()
age=IntVar()
nomlivre=StringVar()
genre=StringVar()
#
nom_entry=Entry(textvariable=nom)
prenom_entry=Entry(textvariable=prenom)
age_entry=Entry(textvariable=age)
nomlivre_entry=Entry(textvariable=nomlivre)
genre_entry=Entry(textvariable=genre)
#
nom_entry.place(x=25,y=60)
prenom_entry.place(x=25,y=120)
age_entry.place(x=25,y=180)
nomlivre_entry.place(x=25,y=240)
genre_entry.place(x=25,y=300)
#creer un bouton
valide=Button(text="Enregistre les données",width="30",height="1",command=saisie_info)
valide.place(x=120,y=350)
#creation menu
menu_bar=Menu(screen)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="quiter",command=screen.quit)
menu_bar.add_cascade(label="fichier",menu=file_menu)
screen.config(menu=menu_bar)
head.mainloop()