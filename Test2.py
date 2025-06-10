import tkinter as tk

selection_color = "#4dd0e1"
mis_color = "#b3e5fc"
hit_color = "#e53935"
default_color = "lightgray"

def create_grid(parent_window):
    selected_button = []      # currently selected button widget
    selected_position = []    # (row, col) of selected button

    def on_button_click(row, col, button):
        # Reset previous selection
        if selected_button[0] is not "":
            selected_button[0].config(bg=default_color)

        # Update current selection
        button.config(bg=selection_color)
        selected_button[0] = button
        selected_position[0] = (row, col)

    def fire():
        if selected_position[0] is not None:
            row, col = selected_position[0]
            print(f"Fired at position: row={row}, col={col}")
        else:
            print("No position selected to fire at.")

    grid_frame = tk.Frame(parent_window, bg="white")
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    for row in range(10):
        for col in range(10):
            btn = tk.Button(grid_frame, width=6, height=3, bg=default_color)
            btn.config(command=lambda r=row, c=col, b=btn: on_button_click(r, c, b))
            btn.grid(row=row, column=col, padx=2, pady=2)

    # Fire button below the grid
    fire_btn = tk.Button(parent_window, text="Fire", command=fire, bg="#f44336", fg="white")
    fire_btn.place(relx=0.5, rely=0.9, anchor='center', width=100, height=40)

root = tk.Tk()
root.title("10x10 Grid with Fire Button")
root.geometry("700x700")

create_grid(root)
root.mainloop()