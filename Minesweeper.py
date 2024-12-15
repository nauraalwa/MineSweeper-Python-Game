import random 

#board user cannot see (the solution)
board = [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]

#board user can see (-1 means unknown location of mines)
boardDisplay = [[-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1]]

#add the mines
numMines = int(input('How many mines?'))
if numMines > 25:
    print('Impossible. Setting to 5 default.')
    numMines = 5
num = 0
while num < numMines:
    row = random.randint(0,4) #5 rows, but indexing start from 0. 
    col = random.randint(0,4)
    if board[row][col] == 0:
        board[row][col] = 1
        num = num+1

#trickiest part thas why did last, need to display the number of mines around in the board.
def checkMinesAround(row, col):
    t = 0 #total mines around the guessed spot
    for r in range(max(0, row - 1), min(4, row + 1) + 1):  # Ensure index stays within bounds, the +1 includes 4 cuz if doesn't use, won't include
        for c in range(max(0, col - 1), min(4, col + 1) + 1):  # Ensure index stays within bounds
            t += board[r][c]
    return t

def displaySol():
    for row in range(0,5):
        for col in range(0,5):
            print(board[row][col], end=" ")
        print("") #if we don't use this it will just print the board disctionary horizontally

def displayBoard():
    print("-"*22)
    for row in range(0,5):
        print("|", end=" ")
        for col in range(0,5):
            if boardDisplay[row][col] == -1:
                print(" ", end=" | ")
            else:
                print(boardDisplay[row][col], end= " | ")
        print("")
        print("-"*22)

displaySol()
displayBoard()

#now make for the guesses
guess = 0
while guess < (25 - numMines):
    row = int(input('Guess a row (1-5): '))-1
    col = int(input('Guess a column (1-5): '))-1
    if board[row][col] == 1:
        print('Boom! You hit a mine.')
        displaySol()
    else:
        boardDisplay[row][col] = checkMinesAround(row, col)
        displayBoard()



