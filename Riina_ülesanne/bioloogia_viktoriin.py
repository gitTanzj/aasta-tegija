from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import sqlite3 as sql

conn = sql.connect("Vocostarter.db")
c = conn.cursor()




#____________________________________________

global SKOOR
global LOENDUR
SKOOR = 0
LOENDUR = 0

def Vastus():
    global SKOOR
    global LOENDUR
    selection = var.get()
    label1 = ttk.Label(text="")
    label2 = ttk.Label(text="")
    
   
    #skoorid[0]
    #print(skoorid[-1])
    if selection == 1:
        SKOOR += 5
        LOENDUR +=1
        KONTROLL.delete(0,END)
        ans = "Õige"
        KONTROLL.insert(0,ans)
        label1.pack(side=RIGHT)
        label1.configure(text="Sinu skoorile liideti 5 punkti!",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=130)
        
    elif selection == 2:
        SKOOR -= 1
        LOENDUR +=1
        KONTROLL.delete(0,END)
        ans = "Vale"
        KONTROLL.insert(0,ans)
        label1.configure(text="")
        label1.configure(text="Sinu skoorilt kaotati 1 punkt!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=310)
    
    elif selection == 3:
        
        SKOOR -= 1
        LOENDUR +=1        
        
        KONTROLL.delete(0,END)
        ans = "Vale"
        KONTROLL.insert(0,ans)
        label1.configure(text="Sinu skoorilt kaotati 1 punkt!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=460)
    
    elif selection == 4:
        
        SKOOR -= 1
        LOENDUR +=1
        KONTROLL.delete(0,END)
        ans = "Vale"
        KONTROLL.insert(0,ans)
        label1.configure(text="Sinu skoorilt kaotati 1 punkt!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=410,y=610)
        
    if LOENDUR == 4:
        RIINA_ENTRY.delete(0,END)
        
        uus_skoorid = int(SKOOR)
        RIINA_ENTRY.insert(0,uus_skoorid)
        JutuPilv = PhotoImage(file = "./assets/cloud.png")
        label2.configure(text="Võiksid liituda tasanduskursusega.",font=("Arial",12),background="white")
        label2.pack(side=RIGHT)
        label2.place(x=930,y=120)
    

#____________________________________________

def Riina_kommentaar():
    label2 = ttk.Label(text="")

    
    RIINA_ENTRY.delete(0,END)
    skoorid = []
    skoorid.append(SKOOR)
    uus_skoorid = int(skoorid[-1]) #uus_skoorid saada andmebaasi
    RIINA_ENTRY.insert(0, uus_skoorid)
    c.execute('INSERT INTO Riina (SKOOR) VALUES (?)', (uus_skoorid,))
    c.close()
    conn.commit()
    conn.close()
    
    if uus_skoorid <= 3:
        
        label2.configure(text="Võiksid liituda tasanduskursusega.",font=("Arial",12),background="white")
        label2.pack(side=RIGHT)
        label2.place(x=930,y=120)
    
    elif uus_skoorid > 3:
        label2.configure(text="Hästi tehtud!",font=("Arial",12),background="white")
        label2.pack(side=RIGHT)
        label2.place(x=960,y=120)
        




#____________________________________________

valikud = ["Kissell","Piim","Juust","Hapukoor"]

window = Tk()
window.geometry("1100x1000")
window.title("Bioloogia küsimus")


notebook = ttk.Notebook(window)
notebook.pack(fill="both")
#____________________________________________


label = ttk.Label(text="Milline neist ei sisalda laktoosi?",font=("Arial",25))
label.pack(side=LEFT)
label.place(x=110,y=70)


selected = tk.StringVar()
var = tk.IntVar()

KissellPhoto = PhotoImage(file=r"Riina_ülesanne\assets\Kissell3.png")
PiimPhoto = PhotoImage(file=r"Riina_ülesanne\assets\Piim2.png")
JuustPhoto = PhotoImage(file=r"Riina_ülesanne\assets\Juust2.png")
HapukoorPhoto = PhotoImage(file=r"Riina_ülesanne\assets\Hapukoor1.png")

r1 = ttk.Radiobutton(window,text="Kissell",value=1,variable=var,image= KissellPhoto)
r2 = ttk.Radiobutton(window,text="Piim",value=2,variable=var,image= PiimPhoto)
r3 = ttk.Radiobutton(window,text="Juust",value=3,variable=var, image = JuustPhoto)
r4 = ttk.Radiobutton(window,text="Hapukoor",value=4,variable=var,image = HapukoorPhoto)

r1.pack(side=LEFT)
r1.place(x=110,y=120)

r2.pack(side=LEFT)
r2.place(x=110,y=300)


r3.pack(side=LEFT)
r3.place(x=110,y=450)

r4.pack(side=LEFT)
r4.place(x=110,y=600)

JutuPilv = PhotoImage(file = r"Riina_ülesanne\assets\cloud.png")
JutuLabel = ttk.Label(window, image = JutuPilv,)
PhotoImage(file = r"Riina_ülesanne\assets\cloud.png")
JutuLabel.pack(side=RIGHT)
JutuLabel.place(x=900,y=1)


KONTROLL = Entry(window,font=("Arial",25))
KONTROLL.pack(side=LEFT)
KONTROLL.place(x=80,y=850)

SUBMIT = Button(window,text="Vastus",font=("Impact"), command=Vastus)
SUBMIT.pack(side=RIGHT)
SUBMIT.place(x=90, y=800)

RIINA_SUBMIT = Button(window,text= "Sinu punktid on",font=("Arial"),command = Riina_kommentaar)
RIINA_SUBMIT.pack(side= RIGHT)
RIINA_SUBMIT.place(x=800,y=450)
        
RIINA_ENTRY = Entry(window,font= ("Arial",25))
RIINA_ENTRY.pack(side=LEFT)
RIINA_ENTRY.place(x=800,y=500)

RiinaImage = PhotoImage(file =r"Riina_ülesanne\assets\Õp_Riina1.png")
RiinaLabel = ttk.Label(window, image = RiinaImage)
PhotoImage(file = r"Riina_ülesanne\assets\Õp_Riina1.png")
RiinaLabel.pack(side=RIGHT)
RiinaLabel.place(x=800,y=250)


#REF_BUTTON = Button(window,text="Värskenda lehte", font=("Arial", 13), command = Refresh_Button)
#REF_BUTTON.pack(side=LEFT)
#REF_BUTTON.place(x=10,y=10)


window.mainloop()