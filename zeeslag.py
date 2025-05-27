######################## global ###################################
import random 
AANTAL_BOTEN = 3
GROTE_BORD = 4
["~","~","~","~"]
######################## def's ####################################

def maakbord():
    bord = []
    e = 0
    while e < GROTE_BORD:
        bord.insert(0,["~","~","~","~"])
        e += 1
    return bord

def al_geschoten():
    al_geschoten = []
    e = 0
    while e < GROTE_BORD:
        al_geschoten.insert(0,["","","",""])
        e += 1
    return al_geschoten


def printbord():
    for rij in bord:
        print(rij)
        

def boten():
    i = 0
    print("yes")
    while i < AANTAL_BOTEN:
        yes = True
        while yes == True:
            Y = random.randint(0,len(bord)-1)
            X = random.randint(0,len(bord)-1)
            vak = bord[Y][X]
            print("yes2")
            if vak == "~":
                yes = False
                print("yes3")
            else:
                yes = True
                print("no")
        bord[Y][X] = "b"
        print(Y)
        print(X)
        if Y != len(bord)-1:
            bord[Y+1][X] = "o"
            if X != 0:
                bord[Y+1][X-1] = "o"
            if X != 3:
                bord[Y+1][X+1] = "o"
        if Y != 0:
            bord[Y-1][X] = "o"
            if X != 0:
                bord[Y-1][X-1] = "o"
            if X != 3:
                bord[Y-1][X+1] = "o"
        if X != 0:
            bord[Y][X-1] = "o"
        if X != len(bord)-1:
            bord[Y][X+1] = "o" 
        print("yes4")
        i+= 1
    for rij in range(len(bord)):
        for column in range(len(bord)):
            if bord[rij][column] == "o":
                bord[rij][column] = "~"

def schieten(xcoord, ycoord):
    won = False
    if bord[ycoord-1][xcoord-1] == "~":
        if miss[ycoord-1][xcoord-1] != "m":
            print("Helaas, dat is miss!")
            miss[ycoord-1][xcoord-1] = "m"
        else:
            print("hier heb je al geschoten")
    elif bord[ycoord-1][xcoord-1] == "b":
        bord[ycoord-1][xcoord-1] = "X" 
        boten_over = 0
        for rij in range(len(bord)):
            for column in range(len(bord)):
                if bord[rij][column] == "b":
                    boten_over += 1
        if boten_over < 1:
            won = True
        else:
            print("goed gedaan je hebt een boot geraakt, er zijn nu nog",boten_over, "boten over!")
    return won



######################## Mainscript ###############################
won = False
bord = maakbord()
miss = al_geschoten()
print(bord)
printbord()
boten()
while won == False:
    printbord()
    print("je speelt met een bord van", GROTE_BORD, "bij", GROTE_BORD)
    opbord = False
    while opbord == False:
        xcoord = int(input("geef een X-coördinaat voor je schot : "))
        ycoord = int(input("geef een Y-coördinaat voor je schot : "))
        if ycoord > GROTE_BORD and xcoord > GROTE_BORD:
            print("dat is niet binnen het speelveld geef nieuwe coördinaten")
        else:
            won = schieten(xcoord, ycoord)
            opbord = True
print("Gefelicteerd! ")


#thats crazy dawg
