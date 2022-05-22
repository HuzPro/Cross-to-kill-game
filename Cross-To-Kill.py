Player1 = {'coin':'x','numofcoins':4}
Player2 = {'coin':'o','numofcoins':4}

turnCount = 0
gamemap = [['x','o','x'],
           ['x','x','o'],
           ['o',' ','o']]
#gamemap = [[' ',' ',' '],
#           [' ',' ',' '],
#           [' ',' ',' ']]
coordinatesmap = [[7,8,9],
                  [4,5,6],
                  [1,2,3]]
coordinate = 0


def DisplayMap(gamemap):
    for posY in range(len((gamemap))):
        print(end="|")
        for posX in range(len(gamemap[posY])):
            print(gamemap[posY][posX], end="|")
        print()


def CoinToss():
    import random
    toss = random.randint(1,2)
    if toss == 1:
        print("Player 1 Won the Toss!!!")
        print("------------------------------------------------")
    elif toss == 2:
        print("Player 2 Won the Toss!!!")
        print("------------------------------------------------")
    return toss, toss


def NextTurn(turn):
    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1
    return turn


def ExecuteTurn(P1, P2, turn):
    flag = 0
    if turn == 1:
        print(end="It's Player1's Turn!")
        print("(Refer to the Coordinate map)")
        DisplayMap(coordinatesmap)
        print("\n")
        while flag != 1:
            if flag == 2:
                print("Incorrect coordinate entered.")
            coordinate = input('\nEnter your Coordinates for your coin: ')
            for posY in range(len(gamemap)):
                for posX in range(len(gamemap[posY])):
                    if coordinate == coordinatesmap[posY][posX] and gamemap[posY][posX] == ' ':
                        gamemap[posY][posX] = P1['coin']
                        coordinatesmap[posY][posX] = 'x'
                        flag = 1
                    elif flag != 1:
                        flag = 2
                        
        DisplayMap(gamemap)
        print("------------------------------------------------")
        P1['numofcoins'] -=1
    if turn == 2:
        print(end="It's Player2's Turn!")
        print("(Please refer to the Coordinate map)")
        DisplayMap(coordinatesmap)
        print("\n")
        while flag != 1:
            if flag == 2:
                print("Incorrect coordinate entered.")
            coordinate = input('\nEnter your Coordinates for your coin: ')
            for posY in range(len(gamemap)):
                for posX in range(len(gamemap[posY])):
                    if coordinate == coordinatesmap[posY][posX] and gamemap[posY][posX] == ' ':
                        gamemap[posY][posX] = P2['coin']
                        coordinatesmap[posY][posX] = 'x'
                        flag = 1
                    elif flag != 1:
                        flag = 2
        DisplayMap(gamemap)
        print("------------------------------------------------")
        P2['numofcoins'] -=1
    return P1, P2



#------------------------------------MOVEMENT PART------------------------------------#
def movementInput():
    while True:
        pieceNum = 0
        try:
            pieceNum = int(input("\nPlease enter which Queen you'd like to move: "))
        except:
            print("That is a letter...")
        if pieceNum > 0 and pieceNum < 10:
            break
        else:
            print("Incorrect number entered. Enter a valid number.")
    while True:
        placeLetter = str(input("\nPlease enter which direction you'd like to move that Queen. Pick from the following directions: W=Up, S=Down, A=Left, D=Right\nEnter the Direction letter(W,S,A,D): "))
        if placeLetter == 'w' or placeLetter == 'a' or placeLetter == 's' or placeLetter == 'd':
            break
        else:
            print("Incorrect letter entered. Enter a valid letter")
    return pieceNum, placeLetter

def directionCheck(Direction, piecey, piecex, ocoin):
    dX, dY = 0, 0

    if Direction == 'w':
        if piecey-1 >= 0 and piecey-1 <= 1:
            if gamemap[piecey-1][piecex] == ' ':
                dX, dY = piecex, piecey-1        #For one step in either direction
            elif gamemap[piecey-1][piecex] == ocoin:
                if gamemap[piecey-2][piecex] == ' ':
                    dX, dY = piecex, piecey-2   #For two steps in either direction
                    gamemap[piecey-1][piecex] = ' '
    if Direction == 's':
        if (piecey+1) >= 1 and (piecey+1) <= 2:
            if gamemap[piecey+1][piecex] == ' ':
                print("1 space coordinates being empty check successful")
                dX, dY = piecex, piecey+1        #For one step in either direction
            elif gamemap[piecey+1][piecex] == ocoin:
                if gamemap[piecey+2][piecex] == ' ':
                    dX, dY = piecex, piecey+2   #For two steps in either direction
                    gamemap[piecey+1][piecex] = ' '
    if Direction == 'a':
        if piecex-1 >= 0 and piecex-1 <= 1:
            if gamemap[piecey][piecex-1] == ' ':
                dX, dY = piecex-1, piecey        #For one step in either direction
            elif gamemap[piecey][piecex-1] == ocoin:
                if gamemap[piecey][piecex-2] == ' ':
                    dX, dY = piecex-2, piecey   #For two steps in either direction
                    gamemap[piecey][piecex-1] = ' '
    if Direction == 'd':
        if piecex+1 >= 1 and piecex+1 <= 2:
            if gamemap[piecey][piecex+1] == ' ':
                dX, dY = piecex+1, piecey        #For one step in either direction
            elif gamemap[piecey][piecex+1] == ocoin:
                if gamemap[piecey][piecex+2] == ' ':
                    dX, dY = piecex+2, piecey   #For two steps in either direction
                    gamemap[piecey][piecex+1] = ' '
    return dY, dX


def movement(Pcoin):
    coordinateCheck = [[7,8,9],
                       [4,5,6],
                       [1,2,3]]
    pieceY, pieceX, placeY, placeX = 0, 0, 0, 0
    if Pcoin == 'x':
        opCoin = 'o'
    if Pcoin == 'o':
        opCoin = 'x'

    piece, direction = movementInput() #Taking input
    print("\n\nPiece: "+str(piece)+", Direction: "+direction)
    for PosY in range(len(gamemap)):
        for PosX in range(len(gamemap[PosY])):
            if coordinateCheck[PosY][PosX] == piece:
                if gamemap[PosY][PosX] == Pcoin:
                    pieceY, pieceX = PosY, PosX
    placeY, placeX = directionCheck(direction, pieceY, pieceX, opCoin)
    print("PlaceX = "+str(placeX)+" PlaceY = "+str(placeY)+"\nPieceX = "+str(pieceX)+" PieceY = "+str(pieceY)) #WORKING
    
    gamemap[placeY][placeX] = Pcoin
    gamemap[pieceY][pieceX] = ' '

    for x in gamemap:
        print(x)









#Placement
#while turnCount != 8:
#    if turnCount == 0:
#        turn, movementTurn = CoinToss()
#        
#    
#    Player1,Player2 = ExecuteTurn(Player1, Player2, turn)
#    turn = NextTurn(turn)
#    turnCount += 1

#Movement

turn = 2

endGame = 0
while endGame == 0:
    for x in gamemap:
        print(x)

    if turn == 1:
        pCoin = Player1['coin']
    elif turn == 2:
        pCoin = Player2['coin']

    movement(pCoin)
    if turn == 1:
        turn += 1
    elif turn == 2:
        turn -= 1



#NEED TO ADD CHECKS FOR CAPTURING QUEENS
#NEED TO CHANGE INPUT METHOD TO TELL WHERE TO MOVE THE PIECE TO A DIRECTIONAL ONE
#NEED TO CHANGE MOVEMENT FUNCTION BECAUSE IT'S LITERALLY USELESS(#makethemovementfunctiongreatagain)

