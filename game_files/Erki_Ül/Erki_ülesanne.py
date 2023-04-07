from tkinter import *
from tkinter import ttk
from tkinter import Tk
import sqlite3 as sql

conn = sql.connect("Vocostarter.db")
c = conn.cursor()

#____________________________________________


#____________________________________________

window = Tk()
window.geometry("1300x650")
window.title("Matemaatika ülesanne")

notebook = ttk.Notebook(window)
notebook.pack(fill="both")

#____________________________________________
SKOOR = 0
def Kontroll():
    global SKOOR
    label1 = ttk.Label(text="")

    

    if int(entry1.get()) == -2 and int(entry2.get()) == -4 and int(entry3.get()) == -2 and int(entry4.get()) == -4:
        label1.configure(text="Õigesti lahendasid! Nüüd teenisid välja 200 punkti",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR += 200
        
    
    elif int(entry1.get()) == -4 and int(entry2.get()) == -2 and int(entry3.get()) == -4 and int(entry4.get()) == -2:
        label1.configure(text="Õigesti lahendasid! Nüüd teenisid välja 200 punkti",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR += 200
        
    
    elif int(entry1.get()) == -2 and int(entry2.get()) == -4 and int(entry3.get()) == -2 and int(entry4.get()) == -4:
        label1.configure(text="Õigesti lahendasid! Nüüd teenisid välja 200 punkti",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR += 200
        
    elif int(entry1.get()) == -4 and int(entry2.get()) == -2 and int(entry3.get()) == -4 and int(entry4.get()) == -2:
        label1.configure(text="Õigesti lahendasid! Nüüd teenisid välja 200 punkti",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR += 200
        
    elif int(entry1.get()) == -4 and int(entry2.get()) == -2 and int(entry3.get()) == -2 and int(entry4.get()) == -4:
        label1.configure(text="Õigesti lahendasid! Nüüd teenisid välja 200 punkti",
                         font=("Arial",15),
                         foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR += 200
        
    elif int(entry1.get()) == -2 and int(entry2.get()) == -4 and int(entry3.get()) == -4 and int(entry4.get()) == -2:
        label1.configure(text="Õigesti lahendasid! Nüüd teenisid välja 200 punkti",font=("Arial",15),foreground="green")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR += 200
        
    else:
        label1.configure(text="Nii ikka ei saa. Kaotasid 25 punkti. Proovi uuesti!",
                         font=("Arial",15),
                         foreground="red")
        label1.pack(side=RIGHT)
        label1.place(x=810,y=425)
        SKOOR -=1
        
        
    c.execute('INSERT INTO Erki (SKOOR) VALUES (?)', (SKOOR,))
    c.close()
    conn.commit()
    conn.close()

    
#____________________________________________


label = ttk.Label(text="Aita õpetaja Erkil lahendada Viete'i teoreemi ülesanne",
font=("Arial",18))
label.pack(side="right")
label.place(x=300,y=70)

Label1 = ttk.Label(text="Teoreemi valem",
font=("Arial",13))
Label1.pack(side="left")
Label1.place(x=120,y=500)

ErkiImage = PhotoImage(file=r"Erki_Ül\erki.png")
ErkiLabel = ttk.Label(window, image = ErkiImage)
PhotoImage(file=r"Erki_Ül\erki.png")
ErkiLabel.pack(side="left")
ErkiLabel.place(x=70,y=50)

VieteImage = PhotoImage(file=r"Erki_Ül\Viete.png")
VieteLabel = ttk.Label(window,image=VieteImage)
PhotoImage(file=r"Erki_Ül\Viete.png")
VieteLabel.pack(side="left")
VieteLabel.place(x=70,y=300)

PlussLabel = ttk.Label(text= "+",font=("Impact",25))
PlussLabel.pack(side="right")
PlussLabel.place(x=500,y=425)

KorruLabel = ttk.Label(text= "x",font=("Arial",25))
KorruLabel.pack(side="right")
KorruLabel.place(x=500,y=320)

VõrdusLabel = ttk.Label(text="=",font=("Arial",25))
VõrdusLabel.pack(side="right")
VõrdusLabel.place(x= 700, y = 325)

VõrdusLabel2 = ttk.Label(text="=",font=("Arial",25))
VõrdusLabel2.pack(side="right")
VõrdusLabel2.place(x= 700, y = 425)

entry1 = Entry(window,font=("Arial",18),width=7)
entry2 = Entry(window,font=("Arial",18),width=7)
entry3 = Entry(window,font=("Arial",18),width=7)
entry4 = Entry(window,font=("Arial",18),width=7)


entry1.pack(side="right")
entry2.pack(side="left")
entry3.pack(side="right")
entry4.pack(side="left")


entry1.place(x=350, y=330)
entry2.place(x=550, y=330)
entry3.place(x=350, y=430)
entry4.place(x=550, y=430)

KuusLabel = ttk.Label(text=-6,font=("arial",30))
KuusLabel.pack(side="right")
KuusLabel.place(x= 750, y=425)

KaheksaLabel = ttk.Label(text=8,font=("arial",30))
KaheksaLabel.pack(side="right")
KaheksaLabel.place(x=750,y=325)

Label2 = ttk.Label(text="Leida on vaja puuduvad x-id. Iga õige x annab 2 ja vale kaotab 1 punkti",
font=("Arial",15))
Label2.pack(side="left")
Label2.place(x=300,y=130)


#ControlEntry1 = Entry(window,font=("Arial",18),width=14)
#ControlEntry2 = Entry(window,font=("Arial",18),width=14)

#ControlEntry1.pack(side="right")
#ControlEntry2.pack(side="right")

#ControlEntry1.place(x=800,y=325)
#ControlEntry2.place(x=800,y=425)

Button1 = Button(window,text="Kontrolli",font=("Arial",15),command=Kontroll)

Button1.pack(side="right")

Button1.place(x=1000,y=370)



window.mainloop()