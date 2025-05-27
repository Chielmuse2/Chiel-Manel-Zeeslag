from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import FestivalSQL

backgroundColor       = "#e0f7fa"   # Lichtblauw (achtergrond oceaanachtig)
titleBackgroundColor  = "#00bcd4"   # Fel turquoise (koptekst, accentkleur)
fillColor             = "#81d4fa"   # Zacht waterblauw (voor watercellen)
hoverColor            = "#ffd54f"   # Vrolijk geel (hover-effect)
textColor             = "#004d40"   # Donkergroenblauw (goede leesbaarheid)
hoverTextColor        = "black"     # Zwarte tekst bij hover (duidelijk)

################## def's ##################
def on_enter(e): #e betekend in deze context any
    e.widget.config(bg=hoverColor, fg=hoverTextColor) #kleur veranderen wanneer je boven de knop hangt

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor) #kleur terugveranderen als je weer van de knop af gaat

def open_main_window():
    window.deiconify()  #toont het hoofdscherm

def close_all():
   welcome_window.destroy()

def NAW_tabel():
 ingevoerde_voornaam = invoerveldVoornaam.get()
 print("ingevulde naam:", invoerveldVoornaam.get() )

 ingevoerd_tussenvoegsel = invoerveldTussenvoegsel.get()
 ingevoerde_achternaam = invoerveldAchternaam.get()
 ingevoerde_postcode = invoerveldPostcode.get()
 ingevoerd_adres = invoerveldAdres.get()
 ingevoerde_email = invoerveldemail.get()
 ingevoerde_telefoon = invoerveldtelefoon.get()
 FestivalSQL.voegNAWToe(ingevoerde_voornaam,ingevoerd_tussenvoegsel,ingevoerde_achternaam,ingevoerde_postcode,ingevoerd_adres,ingevoerde_email,ingevoerde_telefoon)
 print("mr/miss",ingevoerde_achternaam, "toegevoegd aan tabelNAW")

def knopvrijdag():
   NAW_tabel()
   ingevoerde_voornaam = invoerveldVoornaam.get()
   print("ingevulde naam:", invoerveldVoornaam.get() )
   FestivalSQL.knopvrijdag(ingevoerde_voornaam)

def knopzaterdag():
   NAW_tabel()
   ingevoerde_voornaam = invoerveldVoornaam.get()
   print("ingevulde naam:", invoerveldVoornaam.get() )
   FestivalSQL.knopzaterdag(ingevoerde_voornaam)

def knopzondag():
   NAW_tabel()
   ingevoerde_voornaam = invoerveldVoornaam.get()
   print("ingevulde naam:", invoerveldVoornaam.get() )
   FestivalSQL.knopzondag(ingevoerde_voornaam)

def knopweekend():
   NAW_tabel()
   ingevoerde_voornaam = invoerveldVoornaam.get()
   print("ingevulde naam:", invoerveldVoornaam.get() )
   FestivalSQL.knopweekend(ingevoerde_voornaam)

def knopcampeerplek():
   NAW_tabel()
   ingevoerde_voornaam = invoerveldVoornaam.get()
   print("ingevulde naam:", invoerveldVoornaam.get() )
   FestivalSQL.knopcampingplek(ingevoerde_voornaam)

def knopparkeerplek():
   NAW_tabel()
   ingevoerde_voornaam = invoerveldVoornaam.get()
   print("ingevulde naam:", invoerveldVoornaam.get() )
   FestivalSQL.knopparkeerplek(ingevoerde_voornaam)

def listboxdoen():
 ingevoerde_voornaam = invoerveldVoornaam.get()
 NAW_tabel()
 listboxSelected.delete(1, END) #maak de listbox leeg
 tbl_klanten = FestivalSQL.tabel_klanten(ingevoerde_voornaam)
 for regel in tbl_klanten:
  listboxSelected.insert(END, regel) #voeg elke regel uit resultaat in
### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
################## Hoofdprogramma ##################

##### Welcome Window #####
welcome_window = Tk()
welcome_window.attributes("-fullscreen", True)

kopjesFont = font.Font(family="Arial", size= 24, weight="bold") #Best wel vet, ben erachter gekomen hoe ik text dik kan drukken.
titelFont = font.Font(family="Times New Roman", size= 100, weight="bold")
normalFont = font.Font(family="Arial", size= 24)
listboxfont = font.Font(family="Helvetica", size= 20, weight="bold")

welcome_window.configure(bg=backgroundColor)
welcome_window.wm_title("Welcome to PoePaaPop!")

naastTitel = Label(welcome_window, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(welcome_window, width= 20, bg=titleBackgroundColor, text="P O E P A A P O P", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0)

openMain = Button(welcome_window, text="Buy Tickets", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_main_window, width= 15, height= 5)
openMain.place(x=1467, y=198)

welcomeText = Label(welcome_window, font=kopjesFont, text="Welcome to poepaapop!", bg=backgroundColor)
welcomeText.place(x=186,y=205)

description = Label(welcome_window, font=normalFont, text="Welcome to poepaapop!", bg=backgroundColor)
description.place(x=186,y=255)

borderVert = Label(welcome_window, width=0, height=30, bg="black")
borderVert.place(x=158, y=205)

borderVert1 = Label(welcome_window, width=0, height=30, bg="black")
borderVert1.place(x=772, y=205)

# borderHor1 = Label(welcome_window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
# borderHor1.place(x=176, y=450)

# borderHor2 = Label(welcome_window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
# borderHor2.place(x=176, y=600)

# borderHor3 = Label(welcome_window, height= 0, bg=backgroundColor, text= "_______________________", font=("Arial", 50))
# borderHor3.place(x=875, y=450)

# borderHor4 = Label(welcome_window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
# borderHor4.place(x=875, y=750)

# borderHor5 = Label(welcome_window, height= 0, bg=backgroundColor, text= "-------------", font=("Arial", 50))
# borderHor5.place(x=1473, y=400)

# borderHor6 = Label(welcome_window, height= 0, bg=backgroundColor, text= "-------------", font=("Arial", 50))
# borderHor6.place(x=1473, y=1000)

##### Main Window #####
window = Toplevel()
window.withdraw()
#kopjesFont = font.Font(family="Arial", size= 24, weight="bold") #Best wel vet, ben erachter gekomen hoe ik text dik kan drukken.
#titelFont = font.Font(family="Times New Roman", size= 100, weight="bold")
window.attributes("-fullscreen", True)
window.configure(bg=backgroundColor)
window.wm_title("PoePaaPop")

naastTitel = Label(window, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(window, width= 20, bg=titleBackgroundColor, text="P O E P A A P O P", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0) #Ik gebruik place in plaats van grid. Ik heb namelijk een specefiek design gemaakt die ik wilde volgen en dit ging erg moeilijk met grid. Place vind ik dus veel fijner om mee te werken.



borderVert = Label(window, width=0, height=30, bg="black")
borderVert.place(x=158, y=205)

borderHor = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50)) #alle borders zijn puur omdat ze er leuk uit zien
borderHor.place(x=186, y=250)

borderVert1 = Label(window, width=0, height=30, bg="black")
borderVert1.place(x=772, y=205)

borderHor1 = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
borderHor1.place(x=176, y=450)

borderHor2 = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
borderHor2.place(x=176, y=600)

borderHor3 = Label(window, height= 0, bg=backgroundColor, text= "_______________________", font=("Arial", 50))
borderHor3.place(x=875, y=450)

borderHor4 = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
borderHor4.place(x=875, y=750)

borderHor5 = Label(window, height= 0, bg=backgroundColor, text= "-------------", font=("Arial", 50))
borderHor5.place(x=1473, y=400)

borderHor6 = Label(window, height= 0, bg=backgroundColor, text= "-------------", font=("Arial", 50))
borderHor6.place(x=1473, y=1000)

email = Label(window, text="Email:",bg=backgroundColor, font=kopjesFont)
email.place(x=186, y=200)
ingevoerde_email = StringVar()
invoerveldemail = Entry(window, textvariable=ingevoerde_email, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldemail.place(x=486-50, y=200)

phone = Label(window, text="Phone Number:",bg=backgroundColor, font=kopjesFont)
phone.place(x=186, y=250)
ingevoerde_telefoon = StringVar()
invoerveldtelefoon = Entry(window, textvariable=ingevoerde_telefoon, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldtelefoon.place(x=436, y=250)

name = Label(window, text="First Name:",bg=backgroundColor, font=kopjesFont)
name.place(x=186, y=350)
ingevoerde_voornaam = StringVar()
invoerveldVoornaam = Entry(window, textvariable=ingevoerde_voornaam, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldVoornaam.place(x=436, y=350)

prefix = Label(window, text="Prefix:",bg=backgroundColor, font=kopjesFont)
prefix.place(x=186, y=400)
ingevoerd_tussenvoegsel = StringVar()
invoerveldTussenvoegsel = Entry(window, textvariable=ingevoerd_tussenvoegsel, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldTussenvoegsel.place(x=436, y=400)

surname = Label(window, text="Surname:",bg=backgroundColor, font=kopjesFont)
surname.place(x=186, y=450)
ingevoerde_achternaam = StringVar()
invoerveldAchternaam = Entry(window, textvariable=ingevoerde_achternaam, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldAchternaam.place(x=436, y=450)

ZIPcode = Label(window, text="ZIP code:",bg=backgroundColor, font=kopjesFont)
ZIPcode.place(x=186, y=550)
ingevoerde_postcode = StringVar()
invoerveldPostcode = Entry(window, textvariable=ingevoerde_postcode, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldPostcode.place(x=436, y=550)

address = Label(window, text="Address:",bg=backgroundColor, font=kopjesFont)
address.place(x=186, y=600)
ingevoerd_adres = StringVar()
invoerveldAdres = Entry(window, textvariable=ingevoerd_adres, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldAdres.place(x=436, y=600)

selected = Label(window, text="Selected:",bg=backgroundColor, font=kopjesFont)
selected.place(x=1464, y=474)
listboxSelected = Listbox(window, height=5, width= 65, bd= 6, relief="solid", bg=fillColor, font=listboxfont)
listboxSelected.insert(0, "Naam     dag hoofdartiest begintijd campingplaats parkeerplek")
listboxSelected.place(x=821, y=538)

confirm = Button(window, text="Confirm Selection", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 15, height= 6, command=listboxdoen)
confirm.place(x=1516-50, y=726)

campingSpot = Button(window, text="Camping Spot", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 15, command=knopcampeerplek)
campingSpot.place(x=1144, y=726)

parkingSpot = Button(window, text="Parking Spot", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 15, command=knopparkeerplek)
parkingSpot.place(x=821, y=726)

closeWindow = Button(window, text="Close", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=close_all, width= 15, height= 5)
closeWindow.place(x=1467, y=198)

weekend = Button(window, text="Weekend", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 7, height= 5, command=knopweekend)
weekend.place(x=821, y=846)

friday = Button(window, text="Friday", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 7, height= 5, command=knopvrijdag)
friday.place(x=980, y=846)

saturday = Button(window, text="Saturday", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 7, height= 5, command=knopzaterdag)
saturday.place(x=1139, y=846)

sunday = Button(window, text="Sunday", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width=7, height= 5, command=knopzondag)
sunday.place(x=1294, y=846)

image1_path = r"images/Felix.png" #dit was me toch een gedoe om uit te vogelen haha
image1 = Image.open(image1_path)
image1 = image1.resize((610,355))
photo1 = ImageTk.PhotoImage(image1)

image_path = r"images/Aapop.png"  
image = Image.open(image_path)
image = image.resize((614, 300))  
photo = ImageTk.PhotoImage(image)

photoLabel = Label(window, image=photo, bd=6, relief="solid") #plaatje staat in een label
photoLabel.place(x=870-50, y=198)

photoLabel1 = Label(window, image=photo1, bd=6, relief="solid")
photoLabel1.place(x=206-50, y=700)

buttons = [
    confirm, closeWindow, weekend, friday, saturday, sunday, parkingSpot, campingSpot, openMain
]

for Button in buttons: #dit zorgt ervoor dat voor elke knop in de lijst buttons[] de knop aan on_enter() en on_leave() wordt gekoppeld
    Button.bind("<Enter>", on_enter) #run on_enter() als je over de knop hovert
    Button.bind("<Leave>", on_leave) #run on_leave() als je weer van de knop af gaat

welcome_window.mainloop()
