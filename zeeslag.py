######################## global ###################################
import random 

######################## def's ####################################

def maakbord():
    bord = [["~","~","~","~"],["~","~","~","~"],["~","~","~","~"]]
    return bord

def printbord():
    for rij in bord:
        print(rij)
        

def boten():
    i = 0
    yes = True
    print("yes")
    while i < 3:
        while yes == True:
            Y = random.randint(0,2)
            X = random.randint(0,3)
            vak = bord[Y][X]
            print("yes2")
            if vak == "~":
                yes = False
                print("yes3")
            else:
                yes = True
        bord[Y][X] = "b"
        print(Y)
        print(X)
        if Y != 2:
            bord[Y+1][X] = "o"
            bord[Y+1][X-1] = "o"
            
        bord[Y-1][X] = "o"
        bord[Y+1][X+1] = "o"
        bord[Y-1][X+1] = "o"
        bord[Y+1][X-1] = "o"
        bord[Y-1][X-1] = "o"
        bord[Y][X+1] = "o"
        bord[Y][X-1] = "o"
        print("yes4")
        i+= 3

######################## Mainscript ###############################

bord = maakbord()
vakje = bord[2][1]
printbord()
boten()
printbord()

#thats crazy dawg