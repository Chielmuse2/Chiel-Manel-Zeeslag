from tkinter import *

# Kleuren
fillColor = "lightgray"
textColor = "black"
hoverColor = "blue"
hoverTextColor = "white"

# Hover-functies
def on_enter(e): #e betekend in deze context any
    e.widget.config(bg=hoverColor, fg=hoverTextColor) #kleur veranderen wanneer je boven de knop hangt

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor) #kleur terugveranderen als je weer van de knop af gaat

# Hoofdvenster
root = Tk()
root.title("Hover Button Demo")
root.geometry("300x150")

# Knoppen aanmaken
openMultiplayer = Button(root, text="Multiplayer", bg=fillColor, fg=textColor)
openSingleplayer = Button(root, text="Singleplayer", bg=fillColor, fg=textColor)

# Buttons in lijst
buttons = [openMultiplayer, openSingleplayer]

# Event-binding voor hover
for btn in buttons:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=10)

# Start de GUI
root.mainloop()