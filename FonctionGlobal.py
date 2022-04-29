import tkinter
from turtle import heading, left, right
import xml.etree.ElementTree as e
from tkinter import *
from more_itertools import padded
#fonction de saisie:
mytree=e.parse('auteur.xml')
myroot=mytree.getroot()
def saisie():
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
    screen1=Tk()
    screen1.geometry("500x500")
    screen1.minsize(500,500)
    screen1.maxsize(500,500)
    screen1.config(background='#A6D7CA')
    screen1.title("Ajout d'un auteur")
    head=Label(screen1,text="Saisir les éléments d'un auteur",bd=1,relief=SOLID,font=('Arial',15),bg="#6E7386",fg="black",width=0,height=0)
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
    valide=Button(text="Enregistrer les données",width="30",height="1",command=saisie_info)
    valide.place(x=120,y=350)
    #creation menu
    menu_bar=Menu(screen1)
    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="chercher",command=screen1.destroy)
    menu_bar.add_cascade(label="fichier",menu=file_menu)
    screen1.config(menu=menu_bar)
    screen1.mainloop()
##
def chercher():
    from tkinter import messagebox
    def recherche():
     nom_info=nom.get()
     l=[]
     for x in myroot.findall("auteur"):
         item=x.find('nom').text
         l.append(item)
         if item==nom_info:
             Label(text="les infos de l'auteur:",font=30,bd=1,relief=SOLID).place(x=25,y=120)
             Label(text="Nom:",).place(x=25,y=150)
             Label(text=nom_info).place(x=60,y=150)
             Label(text="Prénom:").place(x=25,y=170)
             Label(text=x.find('prenom').text).place(x=75,y=170)
             Label(text="age:").place(x=25,y=190)
             Label(text=x.find('age').text).place(x=50,y=190)
             Label(text="Publication:").place(x=25,y=210)
             Label(text=x.find('nomlivre').text).place(x=90,y=210)
             Label(text="Genre:").place(x=25,y=230)
             Label(text=x.find('genre').text).place(x=65,y=230)
             #Label(text=nom_info,font=20).pack()
             #messagebox.showinfo("prenom:",x.find('prenom').text)
             #messagebox.showinfo("age:",x.find('age').text)
             #messagebox.showinfo("publication:",x.find('nomlivre').text)
             #messagebox.showinfo("genre:",x.find('genre').text)
     if nom_info not in l:
             messagebox.showinfo("auteur inexsistant")
     nom_entry.delete(0,END)
    screen=Tk()
    screen.geometry("500x500")
    screen.minsize(500,500)
    screen.maxsize(500,500)
    screen.config(background='#A6D7CA')
    screen.title("Rechereche d'un auteur")
    head=Label(screen,text="Saisir le nom de l'auteur à chercher:",bd=1,relief=SOLID,font=('Arial',15),bg="#6E7386",fg="black",width=0,height=0)
    head.pack()
    nom_text=Label(screen,text="Nom de l'auteur",)
    nom_text.place(x=25,y=40)
    nom=StringVar()
    nom_entry=Entry(textvariable=nom)   
    nom_entry.place(x=25,y=60)
    valide=Button(screen ,text="Lancer recherche",width="20",height="1",command=recherche)
    valide.place(x=25,y=85)
    menu_bar=Menu(screen)
    #
    file_menu=Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="quiter",command=screen.quit)
    menu_bar.add_cascade(label="fichier",menu=file_menu)
    screen.config(menu=menu_bar)
    screen.mainloop()
    
saisie()

chercher()