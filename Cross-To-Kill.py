Player1 = {'coin':'x','numofcoins':4}
Player2 = {'coin':'o','numofcoins':4}

turnCount = 0
gamemap = [[' ',' ',' '],
          [' ',' ',' '],
          [' ',' ',' ']]
coordinatesmap = [['7','8','9'],
                 ['4','5','6'],
                 ['1','2','3']]
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
    return toss


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

def pieceToPlaceCondition(piecex, piecey, placex, placey):
    canMove = 0
    if (piecex-placex) == 1 or (piecex-placex) == -1:
        if (piecey-placey) == 0:
            canMove = 1
    if (piecey-placey) == 3 or (piecey-placey) == -3:
        if (piecex-placex) == 0:
            canMove = 1
    return canMove

def movementCondition(place, piece, coin):
    pieceX, pieceY, placeX, placeY = 0, 0, 0, 0
    placeCondition, pieceCondition = 0, 0
    for PosY in range(len(gamemap)):
        for PosX in range(len(gamemap[PosY])):
            if place == coordinatesmap[PosY][PosX]:
                placeCondition += 1
                if coordinatesmap[PosY][PosX] == ' ':
                    placeCondition += 1
                    placeY, placeX = PosY, PosX
            if piece == coordinatesmap[PosY][PosX]:
                pieceCondition += 1
                if coordinatesmap[PosY][PosX] == coin:
                    pieceCondition += 1
                    pieceY, pieceX = PosY, PosX
                
    if pieceCondition == 0 or placeCondition == 0:
        place, piece = movementInput()
    
    
    
    
    # THE ELSE TO ALL THESE IF CONDITIONS WILL HAVE AN ERROR MESSAGE AND THE movementInput FUNCTION AFTER IT
    doesItWork = pieceToPlaceCondition(pieceX,pieceY,placeX,placeY)

    if doesItWork == 1:
        return pieceX, pieceY, placeX, placeY

def movementInput():
    pieceNum = input("Please enter which Queen you'd like to move: ")
    placeNum = input("Please enter the valid square you'd like to move that Queen: ")
    return pieceNum, placeNum

def movement(Pcoin):
    whichPiece, whichPlace = movementInput()
    PieceX, PieceY, PlaceX, PlaceY = movementCondition(whichPlace, whichPiece, Pcoin)
    
    gamemap[PlaceX][PlaceY] == Pcoin
    gamemap[PieceX][PieceY] == ' '
#NEED TO ADD CHECKS FOR CAPTURING QUEENS
#NEED TO CHANGE INPUT METHOD TO TELL WHERE TO MOVE THE PIECE TO A DIRECTIONAL ONE
#NEED TO CHANGE MOVEMENT FUNCTION BECAUSE IT'S LITERALLY USELESS(#makethemovementfunctiongreatagain)





while turnCount != 8:
    if turnCount == 0:
        turn = CoinToss()
        
    
    Player1,Player2 = ExecuteTurn(Player1, Player2, turn)
    turn = NextTurn(turn)
    turnCount += 1

