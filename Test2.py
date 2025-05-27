import tkinter as tk

# Kleuren
fillColor = "lightgray"
textColor = "black"
hoverColor = "blue"
hoverTextColor = "white"

# Hover-functies
def on_enter(e):
    e.widget.config(bg=hoverColor, fg=hoverTextColor)

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor)

# Hoofdvenster
root = tk.Tk()
root.title("Hover Button Demo")
root.geometry("300x150")

# Knoppen aanmaken
openMultiplayer = tk.Button(root, text="Multiplayer", bg=fillColor, fg=textColor)
openSingleplayer = tk.Button(root, text="Singleplayer", bg=fillColor, fg=textColor)

# Buttons in lijst
buttons = [openMultiplayer, openSingleplayer]

# Event-binding voor hover
for btn in buttons:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=10)

# Start de GUI
root.mainloop()