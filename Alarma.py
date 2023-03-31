#Maria jennifer carbajal marinez 
from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import pygame, sys
from pygame.locals import *
root = Tk()
pygame.init()

hour=StringVar()
min=StringVar()
Vent = Frame(root, bg="#CCCCFF")
Vent.pack(fill='both', expand=1)
root.geometry("600x550")


Tit = Label(Vent, text="ALARM", font=("Aurora",20, "bold"), bg="#CCCCFF")
Tit.place(relx=0.35,rely=0.05)

Eti = Label(Vent, text="Hora", font=("Aurora",20), bg="#CCCCFF")
Eti.place(relx=0.15, rely=0.15)
Ehour = Entry(Vent, textvariable=hour).place(relx=0.35, rely=0.15)

Etimin = Label(Vent, text="Min", font=("Aurora",20),bg="#CCCCFF")
Etimin.place(relx=0.15, rely=0.21)
entradaminutos = Entry(Vent, textvariable=min).place(relx=0.35, rely=0.21)

bottonAlarm = Button(Vent, text="Alarma", font=("Aurora",20)).place(relx=0.30, rely=0.55)

def det():
     pygame.mixer.music.stop()
     Vent.config(bg="#CCCCFF")
     Eti.config(bg="#CCCCFF")
     Etimin.config(bg="#CCCCFF")
     Tit.config(bg="#CCCCFF")
     Etiquetas.config(bg="#CCCCFF")

bottonStop = Button(Vent, text="Detiene la alarma", font=("Aurora",20), command=det).place(relx=0.30, rely=0.7)

def tiempo():
    horas = time.strftime("%H")
    minutos = time.strftime("%M")
    segundos = time.strftime("%S")

    horaLocal = horas + ":" + minutos + ":" + segundos
    Etiquetas.config(text=horaLocal)
    Etiquetas.after(2000, tiempo)

    alarmHour = hour.get()
    alarmMin = min.get()

    if horas == alarmHour and minutos == alarmMin and segundos == "00":
        Vent.config(bg="#FF6666")
        Eti.config(bg="#FF6666")
        Etimin.config(bg="#FF6666")
        Tit.config(bg="#FF6666")
        Etiquetas.config(bg="#FF6666")

Etiquetas = Label(root, text="", font=("Aurora", 20, "bold"),bg="#CCCCFF")
Etiquetas.place(relx=0.30, rely=0.35)

tiempo()
root.mainloop()