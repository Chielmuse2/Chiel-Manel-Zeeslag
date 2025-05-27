from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

backgroundColor       = "#e0f7fa"
titleBackgroundColor  = "#00bcd4"   
fillColor             = "#81d4fa"   
hoverColor            = "#ffd54f"   
textColor             = "#004d40"   
hoverTextColor        = "black"     

########## Defs ##########
def open_game_window():
    game_window.deiconify()

def open_game_window_multiplayer():
    game_window_multiplayer.deiconify()

def on_enter(e): #e betekend in deze context any
    e.widget.config(bg=hoverColor, fg=hoverTextColor) #kleur veranderen wanneer je boven de knop hangt

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor) #kleur terugveranderen als je weer van de knop af gaat

########## Welcome window ##########
welcome_window = Tk()
welcome_window.attributes("-fullscreen", True)

kopjesFont = font.Font(family="Arial", size= 24, weight="bold") #Best wel vet, ben erachter gekomen hoe ik text dik kan drukken.
titelFont = font.Font(family="Times New Roman", size= 100, weight="bold")
normalFont = font.Font(family="Arial", size= 24)

welcome_window.configure(bg=backgroundColor)
welcome_window.wm_title("Welkom bij zeeslag!")

naastTitel = Label(welcome_window, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(welcome_window, width= 20, bg=titleBackgroundColor, text="Z e e s l a g", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0)

openSingleplayer = Button(welcome_window, text="Singleplayer", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_game_window, width= 15, height= 5)
openSingleplayer.place(x=1467, y=800)

openMultiplayer = Button(welcome_window, text="Multiplayer", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_game_window, width= 15, height= 5)
openMultiplayer.place(x=1100, y=800)

welcomeText = Label(welcome_window, font=kopjesFont, text="Welkom bij zeeslag!", bg=backgroundColor)
welcomeText.place(x=186,y=205)

description = Label(welcome_window, font=normalFont, text="Klik op 'singleplayer' om het spel te starten tegen een computer. Klik op 'multiplayer' om het spel met een vriend te spelen", bg=backgroundColor, wraplength= 500, justify='left')
description.place(x=186,y=255)

borderVert = Label(welcome_window, width=0, height=30, bg="black")
borderVert.place(x=158, y=205)

borderVert1 = Label(welcome_window, width=0, height=30, bg="black")
borderVert1.place(x=772, y=205)

image_path = r"images/boot enzo.jpg"  
image = Image.open(image_path)
image = image.resize((935, 455))  
photo = ImageTk.PhotoImage(image)

photoLabel = Label(welcome_window, image=photo, bd=6, relief="solid") #plaatje staat in een label
photoLabel.place(x=820, y=198)

########## Game window ############
game_window = Toplevel()
game_window.attributes("-fullscreen", True)
game_window.configure(bg=backgroundColor)
game_window.wm_title("Singleplayer")

naastTitel = Label(game_window, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window, width= 20, bg=titleBackgroundColor, text="S I N G L E P L A Y E R", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0) #Ik gebruik place in plaats van grid. Ik heb namelijk een specefiek design gemaakt die ik wilde volgen en dit ging erg moeilijk met grid. Place vind ik dus veel fijner om mee te werken.

########## Game window multiplayer ##########
game_window_multiplayer = Toplevel()
game_window_multiplayer.attributes("-fullscreen", True)
game_window_multiplayer.configure(bg=backgroundColor)
game_window_multiplayer.wm_title("Multiplayer")

naastTitel = Label(game_window_multiplayer, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window_multiplayer, width= 20, bg=titleBackgroundColor, text="M U L T I P L A Y E R", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0)
welcome_window.mainloop()

##########  ##########

buttons = [openMultiplayer, openSingleplayer]

for Button in buttons: #dit zorgt ervoor dat voor elke knop in de lijst buttons[] de knop aan on_enter() en on_leave() wordt gekoppeld
    Button.bind("<Enter>", on_enter) #run on_enter() als je over de knop hovert
    Button.bind("<Leave>", on_leave) #run on_leave() als je weer van de knop af gaat