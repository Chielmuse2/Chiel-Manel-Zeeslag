from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

backgroundColor       = "#e0f7fa"
titleBackgroundColor  = "#00bcd4"   
fillColor             = "#81d4fa"   
hoverColor            = "#ffd54f"   
hoverTextColor        = "black"     
textColor             = "black"

selection_color = "#4dd0e1"
mis_color = "#b3e5fc"
hit_color = "#e53935"

########## Globale variabelen ##########
aangeklikt_vakje = None
oud_aangeklikt_vakje = None

########## Defs ##########
def open_game_window():
    game_window.deiconify()

def open_game_window_multiplayer():
    game_window_multiplayer.deiconify()

def open_home_window_from_singleplayer():
    home_window.deiconify()
    game_window.withdraw()

def open_home_window_from_multiplayer():
    home_window.deiconify()
    game_window_multiplayer.withdraw()

def close_all():
    home_window.destroy()

def on_enter(e):
    e.widget.config(bg=hoverColor, fg=hoverTextColor)

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor)

def create_grid(parent_window):
    grid_frame = Frame(parent_window, bg=backgroundColor)
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    for row in range(10):
        for col in range(10):
            btn = Button(grid_frame, width=6, height=3, bg="lightgray")
            btn.config(command=lambda r=row, c=col, b=btn: on_button_select(r, c, b))
            btn.grid(row=row, column=col, padx=2, pady=2)

def on_button_select(row, col, button):
    global aangeklikt_vakje
    global oud_aangeklikt_vakje
    if aangeklikt_vakje is None:
        button.config(bg=selection_color)
        oud_aangeklikt_vakje = button
        aangeklikt_vakje = (row, col)
    if aangeklikt_vakje is not (row, col):
        oud_aangeklikt_vakje.config(bg="lightgrey")
        oud_aangeklikt_vakje = button
        button.config(bg=selection_color)
        aangeklikt_vakje = (row, col)

########## Home window ##########
home_window = Tk()
home_window.attributes("-fullscreen", True)

kopjesFont = font.Font(family="Arial", size=24, weight="bold")
titelFont = font.Font(family="Times New Roman", size=100, weight="bold")
normalFont = font.Font(family="Arial", size=24)

home_window.configure(bg=backgroundColor)
home_window.wm_title("Welkom bij zeeslag!")

naastTitel = Label(home_window, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(home_window, width=20, bg=titleBackgroundColor, text="Z e e s l a g", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0)

openSingleplayer = Button(home_window, text="Singleplayer", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_game_window, width=15, height=5)
openSingleplayer.place(x=1467, y=800)

openMultiplayer = Button(home_window, text="Multiplayer", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_game_window_multiplayer, width=15, height=5)
openMultiplayer.place(x=1100, y=800)

closeGame = Button(home_window, text="Close", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=close_all, width=15, height=5)
closeGame.place(x=100, y=800)

welcomeText = Label(home_window, font=kopjesFont, text="Welkom bij zeeslag!", bg=backgroundColor)
welcomeText.place(x=186, y=205)

description = Label(home_window, font=normalFont, text="Klik op 'singleplayer' om het spel te starten tegen een computer. Klik op 'multiplayer' om het spel met een vriend te spelen", bg=backgroundColor, wraplength=500, justify='left')
description.place(x=186, y=255)

borderVert = Label(home_window, width=0, height=30, bg="black")
borderVert.place(x=158, y=205)

borderVert1 = Label(home_window, width=0, height=30, bg="black")
borderVert1.place(x=772, y=205)

image_path = r"images/boot enzo.jpg"
image = Image.open(image_path)
image = image.resize((935, 455))  
photo = ImageTk.PhotoImage(image)

photoLabel = Label(home_window, image=photo, bd=6, relief="solid")
photoLabel.place(x=820, y=198)

########## Game window ##########
game_window = Toplevel()
game_window.attributes("-fullscreen", True)
game_window.configure(bg=backgroundColor)
game_window.wm_title("Singleplayer")
game_window.withdraw()

closeSingleplayer = Button(game_window, text="Home", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_home_window_from_singleplayer, width=15, height=5)
closeSingleplayer.place(x=1467, y=800)

naastTitel = Label(game_window, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window, width=20, bg=titleBackgroundColor, text="S I N G L E P L A Y E R", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0)

create_grid(game_window)

########## Game window multiplayer ##########
game_window_multiplayer = Toplevel()
game_window_multiplayer.attributes("-fullscreen", True)
game_window_multiplayer.configure(bg=backgroundColor)
game_window_multiplayer.wm_title("Multiplayer")
game_window_multiplayer.withdraw()

closeMultiplayer = Button(game_window_multiplayer, text="Home", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=open_home_window_from_multiplayer, width=15, height=5)
closeMultiplayer.place(x=1467, y=800)

naastTitel = Label(game_window_multiplayer, bg=titleBackgroundColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window_multiplayer, width=20, bg=titleBackgroundColor, text="M U L T I P L A Y E R", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0)

create_grid(game_window_multiplayer)

########## Hover effecten ##########
buttons = [openMultiplayer, openSingleplayer, closeMultiplayer, closeSingleplayer, closeGame]

for btn in buttons:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

home_window.mainloop()
