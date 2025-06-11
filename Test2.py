import random
from tkinter import *
from tkinter import font

# Scale factor for all UI elements (1.0 is normal size)
scale = 0.75  # Change this value to adjust the scale of all UI elements

# Apply scaling to dimensions
def scale_dim(value):
    return int(value * scale)

# Colors
backgroundColor = "#e0f7fa"
titleBackgroundColor = "#00bcd4"
fillColor = "#81d4fa"
hoverColor = "#ffd54f"
hoverTextColor = "black"
textColor = "black"
hoverColorFire = "#ff9a00"
selection_color = "#BFEFF"
mis_color = "#83aec2"
hit_color = "#e53935"
grey_out_color = "#A5A5A5"
BOOT_KLEUR = "#4CAF50"
PREVIEW_KLEUR = "#FFC107"

# Global variables
aangeklikt_vakje = None
oud_aangeklikt_vakje = None
grootte_bord = 10
aangeklikte_vakjes = []
hitOrMiss = ""
overview_labels_p1 = []
overview_labels_p2 = []
turn = "P1"

# Boat placement variables
huidige_boot_grootte = None
boot_index = 0
boten_te_plaatsen = []
selectie_pos = None
selectie_richting = 'horizontaal'
preview_posities = []
boot_config = {
    5: 1,  # 1 boot van grootte 5
    4: 1,  # 1 boot van grootte 4
    3: 2,  # 2 boten van grootte 3
    2: 1   # 1 boot van grootte 2
}

def open_game_window():
    game_window.deiconify()

def open_game_window_multiplayer():
    game_window_multiplayer_p1.deiconify()

def open_home_window_from_singleplayer():
    game_window.withdraw()
    home_window.deiconify()

def open_home_window_from_multiplayer():
    game_window_multiplayer_p1.withdraw()
    home_window.deiconify()

def close_all():
    home_window.destroy()

def on_enter(e):
    e.widget.config(bg=hoverColor, fg=hoverTextColor)

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor)

def on_enter_fire_p1(e):
    global turn
    if turn == "P1":
        e.widget.config(bg=hoverColorFire, fg=hoverTextColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_enter_fire_p2(e):
    global turn
    if turn == "P2":
        e.widget.config(bg=hoverColorFire, fg=hoverTextColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_enter_disableable_p1(e):
    global turn
    if turn == "P1":
        e.widget.config(bg=hoverColor, fg=hoverTextColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_enter_disableable_p2(e):
    global turn
    if turn == "P2":
        e.widget.config(bg=hoverColor, fg=hoverTextColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_leave_disableable_p1(e):
    if turn == "P1":
        e.widget.config(bg=fillColor, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_leave_disableable_p2(e):
    if turn == "P2":
        e.widget.config(bg=fillColor, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_leave_fire_p1(e):
    if turn == "P1":
        e.widget.config(bg=hit_color, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_leave_fire_p2(e):
    if turn == "P2":
        e.widget.config(bg=hit_color, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def create_grid(parent_window, for_placement=False):
    grootte_bord = 10
    grid_frame = Frame(parent_window, bg=backgroundColor)
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Column labels (1-10)
    for col in range(10):
        label = Label(grid_frame, text=str(col+1), bg=titleBackgroundColor, width=scale_dim(2), height=scale_dim(1),
                     bd=scale_dim(3), relief="solid", font=font.Font(family="Arial", size=scale_dim(28), weight="bold"))
        label.grid(row=0, column=col+1, ipady=scale_dim(3))

    # Row labels (A-J)
    for row in range(10):
        label = Label(grid_frame, text=chr(65+row), bg=titleBackgroundColor, width=scale_dim(2), height=scale_dim(1),
                     bd=scale_dim(3), relief="solid", font=font.Font(family="Arial", size=scale_dim(28), weight="bold"))
        label.grid(row=row+1, column=0, ipady=scale_dim(3))

    # Create grid buttons
    for row in range(10):
        for col in range(10):
            btn = Button(grid_frame, width=scale_dim(6), height=scale_dim(3),
                        bg=backgroundColor, bd=scale_dim(3), relief="solid")
            if for_placement:
                btn.config(command=lambda r=row, c=col: plaats_boot_klik(r, c))
            else:
                btn.config(command=lambda r=row, c=col, b=btn: on_button_select(r, c, b))
            btn.grid(row=row+1, column=col+1)
    
    parent_window.grid_frame = grid_frame
    return grid_frame

def on_button_select(row, col, button):
    global aangeklikt_vakje
    global oud_aangeklikt_vakje
    
    # Check if button is already hit or missed
    if button.cget('bg') in [hit_color, mis_color]:
        print("You've already fired at this location!")
        return
    
    # Check if it's the player's turn
    if (turn == "P1" and button.master == game_window_multiplayer_p2.grid_frame) or \
       (turn == "P2" and button.master == game_window_multiplayer_p1.grid_frame):
        print("Not your turn to select on this board!")
        return
    
    if aangeklikt_vakje is None:
        button.config(bg=selection_color)
        oud_aangeklikt_vakje = button
        aangeklikt_vakje = [row, col]
    elif aangeklikt_vakje != [row, col]:
        oud_aangeklikt_vakje.config(bg=backgroundColor)
        oud_aangeklikt_vakje = button
        button.config(bg=selection_color)
        aangeklikt_vakje = [row, col]

def to_player_two():
    game_window_multiplayer_p1.withdraw()
    game_window_multiplayer_p2.deiconify()

def to_player_one():
    game_window_multiplayer_p1.deiconify()
    game_window_multiplayer_p2.withdraw()

def maak_bord(grootte_bord):
    return [['~' for _ in range(grootte_bord)] for _ in range(grootte_bord)]

def print_bord(bord):
    for rij in bord:
        print(' '.join(rij))

def is_veilig(bord, x, y, grootte_boot, richting):
    grootte_bord = len(bord)
    
    if richting == 'horizontaal':
        min_x = max(0, x - 1)
        max_x = min(grootte_bord - 1, x + 1)
        min_y = max(0, y - 1)
        max_y = min(grootte_bord - 1, y + grootte_boot)
    else:  # verticaal
        min_x = max(0, x - 1)
        max_x = min(grootte_bord - 1, x + grootte_boot)
        min_y = max(0, y - 1)
        max_y = min(grootte_bord - 1, y + 1)
    
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if bord[i][j] != '~':
                return False
    return True

def disable_all_buttons(grid_frame):
    for row in range(1, 11):
        for col in range(1, 11):
            button = grid_frame.grid_slaves(row=row, column=col)
            if button:
                button[0].config(state=DISABLED, bg=grey_out_color)

def fireP1():
    global hitOrMiss, aangeklikt_vakje, bordP1
    if aangeklikt_vakje is None:
        return
    
    row, col = aangeklikt_vakje
    button = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+1, column=col+1)[0]
    
    if bordP1[row][col] == "b":
        bordP1[row][col] = "h"
        button.config(bg=hit_color, state=DISABLED)
        overview_labels_p1[row][col].config(bg=hit_color)
        
        if is_ship_sunk(bordP1, row, col):
            hitOrMiss = "Ship sunk!"
        else:
            hitOrMiss = "Hit!"
            
        if all_ships_sunk(bordP1):
            hitOrMiss = "Player 1 wins! All ships sunk!"
            disable_all_buttons(game_window_multiplayer_p1.grid_frame)
    else:
        hitOrMiss = "Miss!"
        button.config(bg=mis_color, state=DISABLED)
        switchTurn()
    
    hitOrMisLabel.config(text=hitOrMiss)
    aangeklikt_vakje = None

def fireP2():
    global hitOrMiss, aangeklikt_vakje, bordP2
    if aangeklikt_vakje is None:
        return
    
    row, col = aangeklikt_vakje
    button = game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+1, column=col+1)[0]
    
    if bordP2[row][col] == "b":
        bordP2[row][col] = "h"
        button.config(bg=hit_color, state=DISABLED)
        overview_labels_p2[row][col].config(bg=hit_color)
        
        if is_ship_sunk(bordP2, row, col):
            hitOrMiss = "Ship sunk!"
        else:
            hitOrMiss = "Hit!"
            
        if all_ships_sunk(bordP2):
            hitOrMiss = "Player 2 wins! All ships sunk!"
            disable_all_buttons(game_window_multiplayer_p2.grid_frame)
    else:
        hitOrMiss = "Miss!"
        button.config(bg=mis_color, state=DISABLED)
        switchTurn()
    
    hitOrMisLabelP2.config(text=hitOrMiss)
    aangeklikt_vakje = None

def is_ship_sunk(bord, row, col):
    i = col - 1
    while i >= 0 and bord[row][i] in ['b', 'h']:
        if bord[row][i] == 'b':
            return False
        i -= 1
    
    i = col + 1
    while i < len(bord) and bord[row][i] in ['b', 'h']:
        if bord[row][i] == 'b':
            return False
        i += 1
    
    i = row - 1
    while i >= 0 and bord[i][col] in ['b', 'h']:
        if bord[i][col] == 'b':
            return False
        i -= 1
    
    i = row + 1
    while i < len(bord) and bord[i][col] in ['b', 'h']:
        if bord[i][col] == 'b':
            return False
        i += 1
    
    return True

def create_ship_overview(parent_window, bord, title, player):
    global overview_labels_p1, overview_labels_p2
    
    overview_frame = Frame(parent_window, bg=backgroundColor)
    overview_frame.place(x=scale_dim(1569), y=scale_dim(222), width=scale_dim(500), height=scale_dim(350))
    
    title_label = Label(overview_frame, text=title, font=font.Font(family="Arial", size=scale_dim(14), weight="bold"),
                       bg=titleBackgroundColor, fg="black", bd=scale_dim(5), relief='solid')
    title_label.grid(row=0, column=0, columnspan=10, sticky="ew")
    
    board_frame = Frame(overview_frame, bg="black")
    board_frame.grid(row=1, column=0)
    
    labels = []
    for row in range(10):
        row_labels = []
        for col in range(10):
            cell_value = bord[row][col]
            
            bg_color = BOOT_KLEUR if cell_value == 'b' else backgroundColor
            label = Label(board_frame, width=scale_dim(4), height=scale_dim(2), bg=bg_color,
                         bd=scale_dim(2), relief="solid", font=font.Font(size=scale_dim(6)))
            label.grid(row=row, column=col, padx=scale_dim(1), pady=scale_dim(1))
            row_labels.append(label)
        labels.append(row_labels)
    
    if player == 1:
        overview_labels_p1 = labels
    else:
        overview_labels_p2 = labels
    
    for i in range(10):
        board_frame.grid_rowconfigure(i, weight=1, uniform="cells")
        board_frame.grid_columnconfigure(i, weight=1, uniform="cells")
    return labels

def all_ships_sunk(bord):
    for row in bord:
        if 'b' in row:
            return False
    return True

def p1Tturn():
    fireButtonP1.config(state=NORMAL, bg=hit_color)
    toPlayer2Button.config(state=DISABLED, bg=grey_out_color)
    fireButtonP2.config(state=DISABLED, bg=grey_out_color)
    toPlayer1Button.config(state=NORMAL, bg=fillColor)

def p2Turn():
    fireButtonP2.config(state=NORMAL, bg=hit_color)
    toPlayer1Button.config(state=DISABLED, bg=grey_out_color)
    fireButtonP1.config(state=DISABLED, bg=grey_out_color)
    toPlayer2Button.config(state=NORMAL, bg=fillColor)

def switchTurn():
    global turn
    if turn == "P1":
        turn = "P2"
        p2Turn()
    else:
        turn = "P1"
        p1Tturn()

# Boot placement functions
def start_boot_plaatsing():
    global boten_te_plaatsen, boot_index, bordP1, bordP2
    
    bordP1 = maak_bord(grootte_bord)
    bordP2 = maak_bord(grootte_bord)
    
    boten_te_plaatsen = []
    for grootte, aantal in boot_config.items():
        for _ in range(aantal):
            boten_te_plaatsen.append(grootte)
    
    boot_index = 0
    volgende_boot()

def volgende_boot():
    global boot_index, huidige_boot_grootte
    
    if boot_index < len(boten_te_plaatsen):
        huidige_boot_grootte = boten_te_plaatsen[boot_index]
        status_label.config(text=f"Plaats een boot van {huidige_boot_grootte} lang. Klik op een startpositie.")
    else:
        status_label.config(text="Alle boten zijn geplaatst!")
        create_ship_overview(game_window_multiplayer_p1, bordP1, "Jouw boten", 1)
        create_ship_overview(game_window_multiplayer_p2, bordP2, "Jouw boten", 2)
        switch_to_shooting_mode()

def plaats_boot_klik(row, col):
    global selectie_pos, selectie_richting
    
    if selectie_pos and selectie_pos == (row, col):
        selectie_richting = 'verticaal' if selectie_richting == 'horizontaal' else 'horizontaal'
    
    selectie_pos = (row, col)
    toon_preview(row, col)

def toon_preview(row, col):
    global preview_posities
    
    reset_preview()
    
    if selectie_richting == 'horizontaal':
        if col + huidige_boot_grootte > grootte_bord:
            return False
        
        if is_veilig(bordP1 if turn == "P1" else bordP2, row, col, huidige_boot_grootte, selectie_richting):
            for i in range(huidige_boot_grootte):
                btn = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+1, column=col+i+1)[0] if turn == "P1" else game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+1, column=col+i+1)[0]
                btn.config(bg=PREVIEW_KLEUR)
                preview_posities.append((row, col+i))
            return True
    else:
        if row + huidige_boot_grootte > grootte_bord:
            return False
        
        if is_veilig(bordP1 if turn == "P1" else bordP2, row, col, huidige_boot_grootte, selectie_richting):
            for i in range(huidige_boot_grootte):
                btn = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+i+1, column=col+1)[0] if turn == "P1" else game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+i+1, column=col+1)[0]
                btn.config(bg=PREVIEW_KLEUR)
                preview_posities.append((row+i, col))
            return True
    return False

def bevestig_plaatsing():
    global boot_index
    
    if selectie_pos:
        row, col = selectie_pos
        if plaats_boot(row, col):
            volgende_boot()

def plaats_boot(row, col):
    global boot_index
    
    bord = bordP1 if turn == "P1" else bordP2
    
    if selectie_richting == 'horizontaal':
        for i in range(huidige_boot_grootte):
            bord[row][col + i] = 'b'
            btn = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+1, column=col+i+1)[0] if turn == "P1" else game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+1, column=col+i+1)[0]
            btn.config(bg=BOOT_KLEUR)
    else:
        for i in range(huidige_boot_grootte):
            bord[row + i][col] = 'b'
            btn = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+i+1, column=col+1)[0] if turn == "P1" else game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+i+1, column=col+1)[0]
            btn.config(bg=BOOT_KLEUR)
    
    boot_index += 1
    return True

def reset_preview():
    global preview_posities
    
    for row, col in preview_posities:
        btn = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+1, column=col+1)[0] if turn == "P1" else game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+1, column=col+1)[0]
        if (bordP1 if turn == "P1" else bordP2)[row][col] == '~':
            btn.config(bg=backgroundColor)
    
    preview_posities = []

def switch_to_shooting_mode():
    # Reset alle knoppen in beide grids
    for row in range(10):
        for col in range(10):
            # Reset voor player 1 grid
            btn_p1 = game_window_multiplayer_p1.grid_frame.grid_slaves(row=row+1, column=col+1)[0]
            btn_p1.config(
                bg=backgroundColor, 
                command=lambda r=row, c=col, b=btn_p1: on_button_select(r, c, b),
                state=NORMAL
            )
            
            # Reset voor player 2 grid
            btn_p2 = game_window_multiplayer_p2.grid_frame.grid_slaves(row=row+1, column=col+1)[0]
            btn_p2.config(
                bg=backgroundColor, 
                command=lambda r=row, c=col, b=btn_p2: on_button_select(r, c, b),
                state=NORMAL
            )
    
    # Enable fire buttons
    fireButtonP1.config(state=NORMAL, bg=hit_color)
    fireButtonP2.config(state=DISABLED, bg=grey_out_color)
    
    # Update turn
    global turn
    turn = "P1"
    p1Tturn()

# Initialize game boards
bordP1 = maak_bord(grootte_bord)
bordP2 = maak_bord(grootte_bord)

# Home window
home_window = Tk()
home_window.attributes("-fullscreen", True)

kopjesFont = font.Font(family="Arial", size=scale_dim(24), weight="bold")
titelFont = font.Font(family="Times New Roman", size=scale_dim(100), weight="bold")
normalFont = font.Font(family="Arial", size=scale_dim(24))

home_window.configure(bg=backgroundColor)
home_window.wm_title("Welkom bij zeeslag!")

naastTitel = Label(home_window, bg=titleBackgroundColor, bd=scale_dim(6), relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(home_window, width=scale_dim(22), bg=titleBackgroundColor, text="Z e e s l a g", bd=scale_dim(6), relief="solid", font=titelFont)
titel.place(x=scale_dim(75), y=0)

openSingleplayer = Button(home_window, text="Singleplayer", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, command=open_game_window, width=scale_dim(15), height=scale_dim(5))
openSingleplayer.place(x=scale_dim(1467), y=scale_dim(800))

openMultiplayer = Button(home_window, text="Multiplayer", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, command=open_game_window_multiplayer, width=scale_dim(15), height=scale_dim(5))
openMultiplayer.place(x=scale_dim(1100), y=scale_dim(800))

closeGame = Button(home_window, text="Close", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, command=close_all, width=scale_dim(15), height=scale_dim(5))
closeGame.place(x=scale_dim(100), y=scale_dim(800))

welcomeText = Label(home_window, font=kopjesFont, text="Welkom bij zeeslag!", bg=backgroundColor)
welcomeText.place(x=scale_dim(186), y=scale_dim(205))

description = Label(home_window, font=normalFont, text="Klik op 'singleplayer' om het spel te starten tegen een computer. Klik op 'multiplayer' om het spel met een vriend te spelen", bg=backgroundColor, wraplength=scale_dim(500), justify='left')
description.place(x=scale_dim(186), y=scale_dim(255))

borderVert = Label(home_window, width=0, height=scale_dim(30), bg="black")
borderVert.place(x=scale_dim(158), y=scale_dim(205))

borderVert1 = Label(home_window, width=0, height=scale_dim(30), bg="black")
borderVert1.place(x=scale_dim(772), y=scale_dim(205))

# Game window
game_window = Toplevel()
game_window.attributes("-fullscreen", True)
game_window.configure(bg=backgroundColor)
game_window.wm_title("Singleplayer")
game_window.withdraw()

closeSingleplayer = Button(game_window, text="Home", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, command=open_home_window_from_singleplayer, width=scale_dim(15), height=scale_dim(5))
closeSingleplayer.place(x=scale_dim(1467), y=scale_dim(800))

naastTitel = Label(game_window, bg=titleBackgroundColor, bd=scale_dim(6), relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window, width=scale_dim(22), bg=titleBackgroundColor, text="S I N G L E P L A Y E R", bd=scale_dim(6), relief="solid", font=titelFont)
titel.place(x=scale_dim(75), y=0)

create_grid(game_window)

# Multiplayer windows
game_window_multiplayer_p1 = Toplevel()
game_window_multiplayer_p1.attributes("-fullscreen", True)
game_window_multiplayer_p1.configure(bg=backgroundColor)
game_window_multiplayer_p1.wm_title("Multiplayer - Player 1")
game_window_multiplayer_p1.withdraw()

homeButton = Button(game_window_multiplayer_p1, text="Home", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, command=open_home_window_from_multiplayer, width=scale_dim(15), height=scale_dim(5))
homeButton.place(x=scale_dim(100), y=scale_dim(800))

hitOrMisLabel = Label(game_window_multiplayer_p1, text="", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, width=scale_dim(15), height=scale_dim(5), wraplength=scale_dim(250))
hitOrMisLabel.place(x=scale_dim(100), y=scale_dim(300))

toPlayer2Button = Button(game_window_multiplayer_p1, text="Player 2", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=grey_out_color, state=DISABLED, command=to_player_two, width=scale_dim(15), height=scale_dim(5))
toPlayer2Button.place(x=scale_dim(1546), y=scale_dim(800))

naastTitel = Label(game_window_multiplayer_p1, bg=titleBackgroundColor, bd=scale_dim(6), relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window_multiplayer_p1, width=scale_dim(22), bg=titleBackgroundColor, text="MULTIPLAYER-PLAYER 1", bd=scale_dim(6), relief="solid", font=titelFont)
titel.place(x=scale_dim(75), y=0)

fireButtonP1 = Button(game_window_multiplayer_p1, text="FIRE", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=hit_color, width=scale_dim(25), height=scale_dim(2), command=fireP1)
fireButtonP1.place(relx=0.5, y=scale_dim(966), anchor='center')

bevestig_knop_p1 = Button(game_window_multiplayer_p1, text="Bevestig plaatsing", font=kopjesFont, command=bevestig_plaatsing)
bevestig_knop_p1.place(x=scale_dim(700), y=scale_dim(800))

status_label = Label(game_window_multiplayer_p1, text="", font=kopjesFont)
status_label.place(x=scale_dim(100), y=scale_dim(100))

create_grid(game_window_multiplayer_p1, for_placement=True)

game_window_multiplayer_p2 = Toplevel()
game_window_multiplayer_p2.attributes("-fullscreen", True)
game_window_multiplayer_p2.configure(bg=backgroundColor)
game_window_multiplayer_p2.wm_title("Multiplayer - Player 2")
game_window_multiplayer_p2.withdraw()

naastTitel = Label(game_window_multiplayer_p2, bg=titleBackgroundColor, bd=scale_dim(6), relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(game_window_multiplayer_p2, width=scale_dim(22), bg=titleBackgroundColor, text="MULTIPLAYER-PLAYER 2", bd=scale_dim(6), relief="solid", font=titelFont)
titel.place(x=scale_dim(75), y=0)

toPlayer1Button = Button(game_window_multiplayer_p2, text="Player 1", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, command=to_player_one, width=scale_dim(15), height=scale_dim(5))
toPlayer1Button.place(x=scale_dim(1467), y=scale_dim(800))

fireButtonP2 = Button(game_window_multiplayer_p2, text="FIRE", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=hit_color, width=scale_dim(25), height=scale_dim(2), command=fireP2)
fireButtonP2.place(relx=0.5, y=scale_dim(966), anchor='center')

hitOrMisLabelP2 = Label(game_window_multiplayer_p2, text="", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=fillColor, width=scale_dim(15), height=scale_dim(5), wraplength=scale_dim(250))
hitOrMisLabelP2.place(x=scale_dim(100), y=scale_dim(300))

bevestig_knop_p2 = Button(game_window_multiplayer_p2, text="Bevestig plaatsing", font=kopjesFont, command=bevestig_plaatsing)
bevestig_knop_p2.place(x=scale_dim(700), y=scale_dim(800))

status_label_p2 = Label(game_window_multiplayer_p2, text="", font=kopjesFont)
status_label_p2.place(x=scale_dim(100), y=scale_dim(100))

create_grid(game_window_multiplayer_p2, for_placement=True)

# Hover effects
buttons = [openMultiplayer, openSingleplayer, homeButton, closeSingleplayer, closeGame]

for btn in buttons:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

toPlayer1Button.bind("<Enter>", on_enter_disableable_p1)
toPlayer1Button.bind("<Leave>", on_leave_disableable_p1)

toPlayer2Button.bind("<Enter>", on_enter_disableable_p2)
toPlayer2Button.bind("<Leave>", on_leave_disableable_p2)

fireButtonP1.bind("<Enter>", on_enter_fire_p1)
fireButtonP1.bind("<Leave>", on_leave_fire_p1)

fireButtonP2.bind("<Enter>", on_enter_fire_p2)
fireButtonP2.bind("<Leave>", on_leave_fire_p2)

# Start the game
start_boot_plaatsing()
home_window.mainloop()