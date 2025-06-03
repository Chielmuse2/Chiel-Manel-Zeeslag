######################## global ###################################
import random 
AANTAL_BOTEN = 5
GROOTE_BORD = 10
######################## def's ####################################

def maakbord():
    bord = []
    e = 0
    while e < GROOTE_BORD:
        bord.insert(0,['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'])
        e += 1
    return bord

def al_geschoten():  #alGeschoten()
    al_geschoten = []
    e = 0
    while e < GROOTE_BORD:
        al_geschoten.insert(0,['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'])
        e += 1
    return al_geschoten


def printbord(a):
    for rij in a:
        print(rij)
        

def boten():
    i = 0
    print("yes")
    while i < AANTAL_BOTEN:
        loop1 = True
        while loop1 == True:
            Y = random.randint(0,(GROOTE_BORD-1))
            X = random.randint(0,(GROOTE_BORD-1))
            vak = bord[Y][X]
            print(vak)
            if vak == "~":
                loop1 = False
                print("yes3")
            else:
                loop1 = True
                print("no")
        bord[Y][X] = "b"
        print(bord[Y][X])
        print(Y)
        print(X)

        omringing_boten()
        print("yes4")
        i+= 1
    Verwijder_omringing()
    printbord(bord)

def TweeLangBoten():
    i = 0
    while i < 1: 
        loop1 = True
        loop2 = True
        while loop2 == True:
            while loop1 == True:
                Y = random.randint(0,(GROOTE_BORD-1))
                X = random.randint(0,(GROOTE_BORD-1))
                vak = bord[Y][X]
                print(vak)
                if vak == "~":
                    loop1 = False
                    print("yes3")
                else:
                    loop1 = True
                    print("no")
            orientatie = random.randint(0,1)
            if orientatie == 1:
                bord[Y][X] = "b"
                print(bord[Y][X])
                print(Y)
                print(X)
                if X < 5:
                    if bord[Y][X+1] == '~':
                        bord[Y][X+1] = "b"
                        loop2 = False 
                    elif bord[Y][X-1] == '~'and bord[Y][X] != 0:
                        bord[Y][X-1] = "b"
                        loop2 = False
                    else:
                        loop2 = True
                else:
                    if bord[Y][X-1] == '~':
                        bord[Y][X-1] = "b"
                        loop2 = False 
                    elif bord[Y][X+1] == '~'and bord[Y][X] != (GROOTE_BORD-1):
                        bord[Y][X+1] = "b"
                        loop2 = False
                    else:
                        loop2 = True
            if orientatie == 0:
                bord[Y][X] = "b"
                print(bord[Y][X])
                print(Y)
                print(X)
                if Y < 5:
                    if bord[Y+1][X] == '~':
                        bord[Y+1][X] = "b"
                        loop2 = False
                    elif bord[Y-1][X] == '~'and bord[Y][X-1] != 0:
                        bord[Y-1][X] = "b"
                        loop2 = False
                    else:
                        loop2 = True
                else:
                    if bord[Y-1][X] == '~':
                        bord[Y-1][X] = "b"
                        loop2 = False 
                    elif bord[Y+1][X] == '~'and bord[Y][X] != 0:
                        bord[Y+1][X] = "b"
                        loop2 = False
                    else:
                        loop2 = True 
            omringing_boten()
        i +=1
    Verwijder_omringing()

def DrieLangBoten():
    i = 0
    while i < 2: 
        loop1 = True
        loop2 = True
        while loop2 == True:
            while loop1 == True:
                Y = random.randint(0,(GROOTE_BORD-1))
                X = random.randint(0,(GROOTE_BORD-1))
                vak = bord[Y][X]
                print(vak)
                if vak == "~":
                    loop1 = False
                    print("yes3")
                else:
                    loop1 = True
                    print("no")
            orientatie = random.randint(0,1)
            if orientatie == 1:
                bord[Y][X] = "b"
                print(bord[Y][X])
                print(Y)
                print(X)
                if X < 5:
                    if bord[Y][X+1] == '~':
                        bord[Y][X+1] = "b" 
                        if bord[Y][X+2] == '~':
                            bord[Y][X+2] = "b"
                            loop2 = False
                        elif bord[Y][X-1] == '~'and bord[Y][X] != 0:
                            bord[Y][X-1] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    elif bord[Y][X-1] == '~'and bord[Y][X] != 0:
                        bord[Y][X-1] = "b"
                        if bord[Y][X-2] == '~'and bord[Y][X-1] != 0:
                            bord[Y][X-2] = "b"
                            loop2 = False
                        elif bord[Y][X+1] == '~':
                            bord[Y][X+1] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    else:
                            loop2 = True
                else:
                    if bord[Y][X-1] == '~':
                        bord[Y][X-1] = "b" 
                        if bord[Y][X-2] == '~':
                            bord[Y][X-2] = "b"
                            loop2 = False
                        elif bord[Y][X+1] == '~'and bord[Y][X] != (GROOTE_BORD-1):
                            bord[Y][X+1] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    elif bord[Y][X+1] == '~'and bord[Y][X] != (GROOTE_BORD-1):
                        bord[Y][X+1] = "b"
                        if bord[Y][X+2] == '~'and bord[Y][X+1] != 0:
                            bord[Y][X+2] = "b"
                            loop2 = False
                        elif bord[Y][X-1] == '~':
                            bord[Y][X-1] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    else:
                        loop2 = True
            if orientatie == 0:
                bord[Y][X] = "b"
                print(bord[Y][X])
                print(Y)
                print(X)
                if Y < 5:
                    if bord[Y+1][X] == '~':
                        bord[Y+1][X] = "b" 
                        if bord[Y+2][X] == '~':
                            bord[Y+2][X] = "b"
                            loop2 = False
                        elif bord[Y-1][X] == '~'and bord[Y][X-1] != 0:
                            bord[Y-1][X] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    elif bord[Y-1][X] == '~'and bord[Y][X-1] != 0:
                        bord[Y-1][X] = "b"
                        if bord[Y-2][X] == '~'and bord[Y][X-1] != 1:
                            bord[Y-2][X] = "b"
                            loop2 = False
                        elif bord[Y+1][X] == '~':
                            bord[Y+1][X] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    else:
                        loop2 = True
                else:
                    if bord[Y-1][X] == '~':
                            bord[Y-1][X] = "b" 
                            if bord[Y-2][X] == '~':
                                bord[Y-2][X] = "b"
                                loop2 = False
                            elif bord[Y+1][X] == '~'and bord[Y][X] != 0:
                                bord[Y+1][X] = "b"
                                loop2 = False
                            else:
                                loop2 = True
                    elif bord[Y+1][X] == '~'and bord[Y][X] != 0:
                        bord[Y+1][X] = "b"
                        if bord[Y+2][X] == '~'and bord[Y][X+1] != 1:
                            bord[Y+2][X] = "b"
                            loop2 = False
                        elif bord[Y-1][X] == '~':
                            bord[Y-1][X] = "b"
                            loop2 = False
                        else:
                            loop2 = True
                    else:
                        loop2 = True 
            omringing_boten()
        i +=1
    Verwijder_omringing()


def VijfLangBoten():
    i = 0
    while i < 1: 
        loop1 = True
        loop2 = True
        while loop2 == True:
            while loop1 == True:
                Y = random.randint(0,(GROOTE_BORD-1))
                X = random.randint(0,(GROOTE_BORD-1))
                vak = bord[Y][X]
                print(vak)
                if vak == "~":
                    loop1 = False
                    print("yes3")
                else:
                    loop1 = True
                    print("no")
            orientatie = random.randint(0,1)
            if orientatie == 1:
                bord[Y][X] = "b"
                print(bord[Y][X])
                print(Y)
                print(X)
                lengte = 1
                if X < 5:
                    x2 = [1,2,3,4]
                    x3 = [-1,-2,-3,-4]
                    for x in x2:
                        if bord[Y][X+x] == '~' and lengte < 5:
                           bord[Y][X+x] = "b"
                           lengte += 1
                        else:   
                            break
                    for x in x3:
                        if bord[Y][X+x] == '~' and lengte < 5:
                           bord[Y][X+x] = "b"
                           lengte += 1
                        elif lengte == 5:
                            break
                        else:
                            loop2 = True  
                else:
                    x2 = [1,2,3,4]
                    x3 = [-1,-2,-3,-4]
                    for x in x3:
                        if bord[Y][X+x] == '~' and lengte < 5:
                           bord[Y][X+x] = "b"
                           lengte += 1
                        else:   
                            break
                    for x in x2:
                        if bord[Y][X+x] == '~' and lengte < 5:
                           bord[Y][X+x] = "b"
                           lengte += 1
                        elif lengte == 5:
                            break
                        else:
                            loop2 = True  
            if orientatie == 0:
                bord[Y][X] = "b"
                print(bord[Y][X])
                print(Y)
                print(X)
                if Y < 5:
                    y2 = [1,2,3,4]
                    y3 = [-1,-2,-3,-4]
                    for y in y2:
                        if bord[Y+y][X] == '~' and lengte < 5:
                           bord[Y+y][X] = "b"
                           lengte += 1
                        else:   
                            break
                    for y in y3:
                        if bord[Y+y][X] == '~' and lengte < 5:
                           bord[Y+y][X] = "b"
                           lengte += 1
                        elif lengte == 5:
                            break
                        else:
                            loop2 = True 
            omringing_boten()
        i +=1
    Verwijder_omringing()

def omringing_boten(): #deze def omringt alle "b" met "o" zodat er geen boten naast elkaar kunnen geplaatst worden
    for rij in range(len(bord)):
                for colomn in range(len(bord)):
                    if bord[rij][colomn] == "b":
                        if rij != len(bord)-1 and bord[rij+1][colomn] != "b":
                            bord[rij+1][colomn] = "o"
                            if colomn != 0:
                                bord[rij+1][colomn-1] = "o"
                            if colomn != len(bord)-1:
                                bord[rij+1][colomn+1] = "o"
                        elif rij != len(bord)-1:
                            if colomn != 0:
                                bord[rij+1][colomn-1] = "o"
                            if colomn != len(bord)-1:
                                bord[rij+1][colomn+1] = "o"
                        if rij != 0 and bord[rij-1][colomn] != "b":
                            bord[rij-1][colomn] = "o"
                            if colomn != 0:
                                bord[rij-1][colomn-1] = "o"
                            if colomn != len(bord)-1:
                                bord[rij-1][colomn+1] = "o"
                        elif rij != 0:
                            if colomn != 0:
                                bord[rij-1][colomn-1] = "o"
                            if colomn != len(bord)-1:
                                bord[rij-1][colomn+1] = "o"
                        if colomn != 0 and bord[rij][colomn-1] != "b":
                            bord[rij][colomn-1] = "o"
                        if colomn != len(bord)-1 and bord[rij][colomn+1] != "b":
                            bord[rij][colomn+1] = "o" 

def Verwijder_omringing():
    for rij in range(GROOTE_BORD):
        for column in range(GROOTE_BORD):
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
        miss[ycoord-1][xcoord-1] = "X"
        boten_over = 0
        for rij in range(GROOTE_BORD):
            for column in range(GROOTE_BORD):
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
printbord(bord)
TweeLangBoten()
DrieLangBoten()
while won == False:
    printbord(miss)
    print()
    printbord(bord)
    print("je speelt met een bord van", GROOTE_BORD, "bij", GROOTE_BORD)
    opbord = False
    while opbord == False:
        xcoord = int(input("geef een X-coördinaat voor je schot : "))
        ycoord = int(input("geef een Y-coördinaat voor je schot : "))
        if ycoord > GROOTE_BORD or xcoord > GROOTE_BORD or ycoord <= 0 or xcoord <= 0:
            print("dat is niet binnen het speelveld geef nieuwe coördinaten")
        else:
            won = schieten(xcoord, ycoord)
            opbord = True
print("Gefelicteerd! Je hebt gewonnen, alle boten zijn gezonken!")


#thats crazy dawg
