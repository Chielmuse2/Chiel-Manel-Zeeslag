import tkinter as tk

# Parameters
ROWS = 10
COLS = 10
CELL_SIZE = 40  # grootte van elke cel (in pixels)

def create_board(root):
    board = []
    for row in range(ROWS):
        row_buttons = []
        for col in range(COLS):
            btn = tk.Button(root, width=4, height=2, command=lambda r=row, c=col: on_click(r, c))
            btn.grid(row=row, column=col)
            row_buttons.append(btn)
        board.append(row_buttons)
    return board

def on_click(row, col):
    print("Klik op cel: ("+str(row)+","+str(col)+")")
    board[row][col].configure(bg='blue')  # voorbeeld: cel wordt blauw bij klik

# Hoofdvenster
root = tk.Tk()
root.title("Zeeslag")

board = create_board(root)

root.mainloop()