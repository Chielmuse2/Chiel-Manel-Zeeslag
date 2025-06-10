import tkinter as tk
selection_color = "#4dd0e1"
mis_color = "#b3e5fc"
hit_color = "#e53935"

geklikt_vakje = ""
oud_geklikt = ""

# Functie die wordt aangeroepen wanneer een knop wordt geklikt
def fire():
    global oud_geklikt
    global geklikt_vakje
    oud_geklikt.config(bg=hit_color)
    oud_geklikt = ""
    geklikt_vakje = ""

def on_button_click(row, col, button):
    global geklikt_vakje
    global oud_geklikt
    if geklikt_vakje is "":
        button.config(bg=selection_color)
        oud_geklikt = button
        geklikt_vakje = (row, col)
    if geklikt_vakje is not (row, col):
        oud_geklikt.config(bg="lightgrey")
        oud_geklikt = button
        button.config(bg=selection_color)
        geklikt_vakje = (row, col)
    print(geklikt_vakje)
    print(oud_geklikt)

# Functie die het raster maakt
def create_grid(parent_window):
    grid_frame = tk.Frame(parent_window, bg="white")
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    for row in range(10):
        for col in range(10):
            # Maak een knop en geef row en col door via lambda
            btn = tk.Button(grid_frame, width=6, height=3, bg="lightgray")
            btn.config(command=lambda r=row, c=col, b=btn: on_button_click(r, c, b))
            btn.grid(row=row, column=col, padx=2, pady=2)

# Hoofdvenster maken
root = tk.Tk()
root.title("10x10 Grid")
root.geometry("700x700")  # Pas de grootte aan indien nodig

fire_btn = tk.Button(root, text="Fire", command=fire, bg="#f44336", fg="white")
fire_btn.grid(row =0, column= 0)

# Raster aanmaken in het venster
create_grid(root)

# Start de Tkinter event loop
root.mainloop()