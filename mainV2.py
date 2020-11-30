from clips import Environment, Symbol
CLOSED = '-'
OPENED = ' '
FLAGGED = 'P'
BOMB = '*'

BOMBVAL = -99

env = None
boardSize = 4
bombNumber = 0
flagNumber = 0
bombPosition = []

boardFinal = []
boardState = []

#Coordinates Methods
def translate(x,y):
    y1=x
    x1=boardSize-y-1
    return x1, y1

#Board Methods
def generateBoard():
    global boardSize, bombNumber, bombPosition, boardFinal, boardState
    
    fileName = input('Enter .txt file name: ')
    lines = []
    with open('testcase/'+fileName+'.txt') as f:
        lines = f.readlines()
    
    boardSize = int(lines[0])
    bombNumber = int(lines[1])
    
    for i in range(boardSize):
        boardFinal.append([])
        boardState.append([])
        for _ in range(boardSize):
            boardFinal[i].append(0)
            boardState[i].append(CLOSED)
    
    for i in range(bombNumber):
        temp = [int(x) for x in lines[i+2].split(',')]
        bombPosition.append(temp)
        x, y = translate(temp[0], temp[1])
        boardFinal[x][y]=BOMBVAL
        boardFinal[x][y-1]+=1
        boardFinal[x][y+1]+=1
        boardFinal[x+1][y]+=1
        boardFinal[x+1][y-1]+=1
        boardFinal[x+1][y+1]+=1
        boardFinal[x-1][y]+=1
        boardFinal[x-1][y-1]+=1
        boardFinal[x-1][y+1]+=1
        
def printBoard(board):
    x=boardSize-1
    for i in range(boardSize):
        if (x>9):
            print(x, end='')
        else:
            print(x, end=' ')
        for j in range(boardSize):
            print(board[i][j], end = ' ')
        print()
        x-=1
    print(" ", end = ' ')
    for i in range(boardSize):
        print(i, end = ' ')
    print()

def checkWin():
    return flagNumber==bombNumber

#Probe Functions
def probeCheckBorderAndFlag(x,y):
    global env, boardState
    boardState[x][y]==OPENED
    env.assert_string('(false 0 '+str(x)+' '+str(y)+')')
    for i in range(x-1,3):
        for j in range(y-1,3):
            if not(i==x and j==y):
                try:
                    if (boardState[i][j]==CLOSED):
                        probe(i,j)
                except IndexError:
                    None

def countClosedAdjacent(x,y):
    count=0
    for i in range(x-1,3):
        for j in range(y-1,3):
            if not(i==x and j==y):
                try:
                    if (boardState[i][j]==CLOSED):
                        count+=1
                except IndexError:
                    None
    return count
    
def countFlaggedAdjacent(x,y):
    count=0
    for i in range(x-1,3):
        for j in range(y-1,3):
            if not(i==x and j==y):
                try:
                    if (boardState[i][j]==FLAGGED):
                        count+=1
                except IndexError:
                    None
    return count
    
def flagMatchClosedNumber(x,y):
    global boardState, env, flagNumber
    for i in range(x-1,3):
        for j in range(y-1,3):
            if not(i==x and j==y):
                try:
                    if (boardState[i][j]==CLOSED):
                        boardState[i][j]==FLAGGED
                        env.assert_string('true '+i+' '+j+')')
                        flagNumber+=1
                except IndexError:
                    None

def probe(x,y):
    global env, boardFinal, boardState
    if (boardFinal[x][y]==0):
        probeCheckBorderAndFlag(x,y)
    elif (boardFinal[x][y]==countClosedAdjacent(x,y)):
        flagMatchClosedNumber(x,y)
    elif (boardFinal[x][y]==countFlaggedAdjacent(x,y) and countClosedAdjacent>0):
        probeCheckBorderAndFlag(x,y)
    else:
        boardState[x][y]=boardFinal[x][y]
        env.assert_string('(false '+boardFinal[x][y]+' '+x+' '+y+')')
    printBoard(boardState)

def main():
    global env
    generateBoard()
    env = Environment()
    env.load('mine2.clp')
    x, y = translate(0,0)
    probe(x,y)
    while not(checkWin()):
        None
    printBoard(boardFinal)
    printBoard(boardState)
    
    
    
if __name__ == '__main__':
    main()