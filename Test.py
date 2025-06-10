import tkinter as tk
selection_color = "#4dd0e1"
mis_color = "#b3e5fc"
hit_color = "#e53935"

geklikt_vakje = []

# Functie die wordt aangeroepen wanneer een knop wordt geklikt


def on_button_click(row, col, button):
    button.config(bg=selection_color)
    selected_row = row
    selected_col = col
    return selected_row, selected_col


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

# Raster aanmaken in het venster
create_grid(root)

# Start de Tkinter event loop
root.mainloop()