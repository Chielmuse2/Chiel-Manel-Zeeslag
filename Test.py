import random
from tkinter import *
from tkinter import font
#from PIL import Image, ImageTk

# Scale factor for all UI elements (1.0 is normal size)
scale = 0.75 # Change this value to adjust the scale of all UI elements

# Apply scaling to dimensions
def scale_dim(value):
    return int(value * scale)

backgroundColor       = "#e0f7fa"
titleBackgroundColor  = "#00bcd4"   
fillColor             = "#81d4fa"   
hoverColor            = "#ffd54f"   
hoverTextColor        = "black"     
textColor             = "black"
hoverColorFire = "#ff9a00"
selection_color = "#BFE5FF"
mis_color = "#83aec2"
hit_color = "#e53935"
grey_out_color = "#A5A5A5"

########## Globale variabelen ##########
aangeklikt_vakje = None
oud_aangeklikt_vakje = None
grootte_bord = 10
aangeklikte_vakjes = []
hitOrMiss = ""
overview_labels_p1 = []
overview_labels_p2 = []
turn = "P1"
########## Defs ##########
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

def on_leave_disableable_p2 (e):
    if turn == "P2":
        e.widget.config(bg=fillColor, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_leave_fire_p1(e):
    if turn == "P1":
        e.widget.config(bg=hit_color, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def on_leave_fire_p2 (e):
    if turn == "P2":
        e.widget.config(bg=hit_color, fg=textColor)
    else:
        e.widget.config(bg=grey_out_color, fg=textColor)

def create_grid(parent_window):
    grootte_bord = 10
    bord = maak_bord(grootte_bord)
    grid_frame = Frame(parent_window, bg=backgroundColor)
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    # Column labels (1-10)
    for col in range(10):
        label = Label(grid_frame, text=str(col+1),bg=titleBackgroundColor, width=scale_dim(2), height= scale_dim(1),bd=scale_dim(3), relief="solid", font=font.Font(family="Arial", size=scale_dim(28), weight="bold"))
        label.grid(row=0, column=col+1, ipady=scale_dim(3))

    # Row labels (A-J)
    for row in range(10):
        label = Label(grid_frame, text=chr(65+row), bg=titleBackgroundColor, width=scale_dim(2), height= scale_dim(1),bd=scale_dim(3), relief="solid", font=font.Font(family="Arial", size=scale_dim(28), weight="bold"))
        label.grid(row=row+1, column=0, ipady=scale_dim(3))

    # Create grid buttons with colors based on game_bord
    for row in range(10):
        for col in range(10):
            btn = Button(grid_frame, width=scale_dim(6), height=scale_dim(3), bg=backgroundColor, bd=scale_dim(3), relief="solid")
            btn.config(command=lambda r=row, c=col, b=btn: on_button_select(r, c, b))
            btn.grid(row=row+1, column=col+1)
    
    # Store grid frame reference
    parent_window.grid_frame = grid_frame

def on_button_select(row, col, button):
    global aangeklikt_vakje
    global oud_aangeklikt_vakje
    # Check if button is already hit (red) or miss (blue)
    if button.cget('bg') in [hit_color, mis_color]:
        print("You've already fired at this location!")
        return
    
    # If no cell is currently selected
    if aangeklikt_vakje is None:
        button.config(bg=selection_color)
        oud_aangeklikt_vakje = button
        aangeklikt_vakje = [row, col]
    # If selecting a different cell
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
    
    # Bepaal de ruimte die de boot inneemt + een buffer van 1 vakje rondom
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
    
    # Controleer of alle vakjes in dit gebied vrij zijn (~)
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if bord[i][j] != '~':
                return False
    return True

def plaats_boten(bord, grootte_boot, aantal_boten):
    grootte_bord = len(bord)
    attempts = 0
    max_attempts = 100  # Prevent infinite loops
    
    while attempts < max_attempts:
        attempts += 1
        success = True
        
        # Try to place all boats of this size
        for _ in range(aantal_boten):
            boot_geplaatst = False
            pogingen = 0
            max_pogingen = 100
            
            while not boot_geplaatst and pogingen < max_pogingen:
                pogingen += 1
                # Kies willekeurige startpositie en richting
                x = random.randint(0, grootte_bord - 1)
                y = random.randint(0, grootte_bord - 1)
                richting = random.choice(['horizontaal', 'verticaal'])
                
                # Controleer of de boot binnen het bord past
                if richting == 'horizontaal':
                    if y + grootte_boot > grootte_bord:
                        continue
                else:  # verticaal
                    if x + grootte_boot > grootte_bord:
                        continue
                
                # Controleer of de boot veilig geplaatst kan worden
                if is_veilig(bord, x, y, grootte_boot, richting):
                    # Plaats de boot
                    if richting == 'horizontaal':
                        for i in range(grootte_boot):
                            bord[x][y + i] = 'b'
                    else:  # verticaal
                        for i in range(grootte_boot):
                            bord[x + i][y] = 'b'
                    boot_geplaatst = True
            
            if not boot_geplaatst:
                success = False
                break
        
        if success:
            return bord  # Return if all boats placed successfully
        
        # Reset the board if placement failed
        bord = maak_bord(grootte_bord)
    
    print(f"Kon {aantal_boten} boten van grootte {grootte_boot} niet plaatsen na {max_attempts} pogingen.")
    return bord  # Return the board even if not all boats were placed

def disable_all_buttons(grid_frame):
    for row in range(1, 11):  # Rows 1-10
        for col in range(1, 11):  # Columns 1-10
            button = grid_frame.grid_slaves(row=row, column=col)
            if button:  # If button exists
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
        overview_labels_p1[row][col].config(bg=hit_color)  # Update overview
        
        if is_ship_sunk(bordP1, row, col):
            hitOrMiss = "Ship sunk!"
        else:
            hitOrMiss = "Hit!"
            
        # Check if all ships are sunk
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
        overview_labels_p2[row][col].config(bg=hit_color)  # Update overview
        
        if is_ship_sunk(bordP2, row, col):
            hitOrMiss = "Ship sunk!"
        else:
            hitOrMiss = "Hit!"
            
        # Check if all ships are sunk
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
    #Check links
    i = col - 1
    while i >= 0 and bord[row][i] in ['b', 'h']:
        if bord[row][i] == 'b':
            return False  #Er is nog een deel van de boot
        i -= 1
    
    #Check rechts
    i = col + 1
    while i < len(bord) and bord[row][i] in ['b', 'h']:
        if bord[row][i] == 'b':
            return False
        i += 1
    
    #Check omhoog
    i = row - 1
    while i >= 0 and bord[i][col] in ['b', 'h']:
        if bord[i][col] == 'b':
            return False
        i -= 1
    
    #Check beneden
    i = row + 1
    while i < len(bord) and bord[i][col] in ['b', 'h']:
        if bord[i][col] == 'b':
            return False
        i += 1
    
    #Alles geraakt
    return True

def create_ship_overview(parent_window, bord, title, player):
    global overview_labels_p1, overview_labels_p2
    
    overview_frame = Frame(parent_window, bg=backgroundColor)
    overview_frame.place(x=scale_dim(1569), y=scale_dim(222), width=scale_dim(500), height=scale_dim(350))
    
    title_label = Label(overview_frame, text=title, font=font.Font(family="Arial", size=scale_dim(14), weight="bold"), bg=titleBackgroundColor, fg="black", bd= scale_dim(5), relief='solid')
    title_label.grid(row=0, column=0, columnspan=10, sticky="ew")
    
    board_frame = Frame(overview_frame, bg="black")
    board_frame.grid(row=1, column=0)
    
    labels = []
    for row in range(10):
        row_labels = []
        for col in range(10):
            cell_value = bord[row][col]
            
            bg_color = "#4CAF50" if cell_value == 'b' else backgroundColor
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
    print("JAJAJA P!TURN")
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
    print("was:", turn)
    if turn == "P1":
        turn = "P2"
        p2Turn()
    else:
        turn = "P1"
        p1Tturn()
    print("is nu:", turn)

######## Voor het spel begint ##########
print(turn)
bordP1 = maak_bord(grootte_bord)
bordP1 = plaats_boten(bordP1, grootte_boot=2, aantal_boten=1)
bordP1 = plaats_boten(bordP1, grootte_boot=3, aantal_boten=2)
bordP1 = plaats_boten(bordP1, grootte_boot=4, aantal_boten=1)
bordP1 = plaats_boten(bordP1, grootte_boot=5, aantal_boten=1)

bordP2 = maak_bord(grootte_bord)
bordP2 = plaats_boten(bordP2, grootte_boot=2, aantal_boten=1)
bordP2 = plaats_boten(bordP2, grootte_boot=3, aantal_boten=2)
bordP2 = plaats_boten(bordP2, grootte_boot=4, aantal_boten=1)
bordP2 = plaats_boten(bordP2, grootte_boot=5, aantal_boten=1)
########## Home window ##########
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

# image_path = r"images/boot enzo.jpg"
# image = Image.open(image_path)
# image = image.resize((scale_dim(935), scale_dim(455)))  
# #photo = ImageTk.PhotoImage(image)

#photoLabel = Label(home_window, image=photo, bd=scale_dim(6), relief="solid")
#photoLabel.place(x=scale_dim(820), y=scale_dim(198))

########## Game window ##########
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

########## Game window multiplayer player 1##########
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

fireButtonP1 = Button(game_window_multiplayer_p1, text="FIRE", font=kopjesFont, bd=scale_dim(6), relief="solid", bg=hit_color, width=scale_dim(25), height=scale_dim(2),command=fireP1)
fireButtonP1.place(relx=0.5, y=scale_dim(966), anchor='center')

create_grid(game_window_multiplayer_p1)
create_ship_overview(game_window_multiplayer_p1, bordP2, "Jouw boten", 2)

########## Game window multiplayer player 2##########
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

create_grid(game_window_multiplayer_p2)
create_ship_overview(game_window_multiplayer_p2, bordP1, "Jouw boten", 1)
########## Hover effecten ##########
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
    
home_window.mainloop()