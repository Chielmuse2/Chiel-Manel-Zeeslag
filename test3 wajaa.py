import random

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
    for _ in range(aantal_boten):
        boot_geplaatst = False
        pogingen = 0
        max_pogingen = 100  # Voorkom oneindige loops bij te weinig ruimte
        
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
            print(f"Kon boot {_ + 1} niet plaatsen na {max_pogingen} pogingen.")

# Voorbeeldgebruik
grootte_bord = 10
bord = maak_bord(grootte_bord)

plaats_boten(bord, grootte_boot = 3, aantal_boten = 2)
plaats_boten(bord, grootte_boot = 4, aantal_boten = 2)
plaats_boten(bord, grootte_boot = 5, aantal_boten = 1)
print_bord(bord)