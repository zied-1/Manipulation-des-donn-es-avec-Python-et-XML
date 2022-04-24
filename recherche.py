from cProfile import label
from distutils.filelist import findall
from struct import pack
from tkinter import *
import xml.etree.ElementTree as e
from tkinter import messagebox
mytree=e.parse('auteur.xml')
myroot=mytree.getroot()
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
nom_text=Label(text="Nom de l'auteur",)
nom_text.place(x=25,y=40)
nom=StringVar()
nom_entry=Entry(textvariable=nom)
nom_entry.place(x=25,y=60)
valide=Button(text="Lancer recherche",width="20",height="1",command=recherche)
valide.place(x=25,y=85)
head.mainloop()