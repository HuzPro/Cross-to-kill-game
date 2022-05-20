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
        while flag != 1:
            if flag == 2:
                print("Incorrect coordinate entered.")
            coordinate = input('\nEnter your Coordinates for your coin:')
            for posY in range(len((gamemap))):
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
        while flag != 1:
            if flag == 2:
                print("Incorrect coordinate entered.")
            coordinate = input('\nEnter your Coordinates for your coin:')
            for posY in range(len((gamemap))):
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


    



while turnCount != 8:
    if turnCount == 0:
        turn = CoinToss()
        
    
    Player1,Player2 = ExecuteTurn(Player1, Player2, turn)
    turn = NextTurn(turn)
    turnCount += 1

