#Tic tac toe
import random
import time
import math

def drawBoard(board):
    print(board[7] + "|" + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == "X")or (letter == "O"):
        letter = input("Do you want to be X or O? ").upper()
    if letter == "O":
        return ["O", "X"]
    else:
        return ["X", "O"]
    
def whoGoesFirst():
    if random.randint(0,1) == 1:
        return "player"
    else:
        return "computer"
def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
            (bo[4]==le and bo[5]==le and bo[6]==le) or
            (bo[1]==le and bo[2]==le and bo[3]==le) or
            (bo[1]==le and bo[5]==le and bo[9]==le) or
            (bo[7]==le and bo[5]==le and bo[3]==le) or
            (bo[1]==le and bo[4]==le and bo[7]==le) or
            (bo[2]==le and bo[5]==le and bo[8]==le) or
            (bo[3]==le and bo[6]==le and bo[9]==le))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == " "

def getPlayerMove(board):
    move = " "
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input("Enter a number to place your move (1-9): ")
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputermove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(board, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return int(i)
    for i in range(1, 10):
      boardCopy = getBoardCopy(board)
      if isSpaceFree(boardCopy, i):
        makeMove(boardCopy, playerLetter, i)
        if isWinner(boardCopy, playerLetter):
            return int(i)
    move = chooseRandomMoveFromList(boardCopy, [1,3,7,9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(2,4,6,8)

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to my tic tac toe game.")

while True:
    theBoard = [" "] *10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The "+turn+ " will go first.")
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == "player":
            drawBoard(theBoard)
            playerMove = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, playerMove)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Congratulations! You won.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It was a draw.")
                    gameIsPlaying = False
                else:
                    drawBoard(theBoard)
                    time.sleep(1)
                    turn = "computer"
        else:
            computerMove = getComputermove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, computerMove)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("Unlucky! The computer won.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It was a draw.")
                    break
                else:
                    turn = "player"

    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break
