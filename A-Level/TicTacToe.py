#  Tic Tac Toe

#  Created by Tiago Ferreira on 11/09/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys
import time
from random import randint

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
possibleLines = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"],
                 ["00", "10", "20"], ["01", "11", "21"], ["02", "12", "22"],
                 ["00", "11", "22"], ["20", "11", "02"]]
isComputerTurn = False
userUses = ""
computerUses = ""

def printBoard():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")

def isEmpty(row, column):
    if board[row][column] == " ":
        return True
    else:
        return False

def putPiece(piece, row, column):
    global isComputerTurn
    if isEmpty(row, column):
        board[row][column] = piece
    if isComputerTurn:
        isComputerTurn = False
    else:
        isComputerTurn = True

def preventOpponentLine():
    global isComputerTurn
    if isComputerTurn:
        for line in range(0, len(possibleLines) - 1):
            opponentCounter = 0
            for place in range(0, len(possibleLines[line]) - 1):
                print("line: " + str(line))
                print("place: " + str(place))
                if board[int(possibleLines[line][place][0])][int(possibleLines[line][place][1])] == "X" and computerUses == "X":
                    break
                elif board[int(possibleLines[line][place][0])][int(possibleLines[line][place][1])] == "O" and computerUses == "O":
                    break
                elif isEmpty(int(possibleLines[line][place][0]), int(possibleLines[line][place][1])):
                    pass
                else:
                    opponentCounter += 1
        if opponentCounter == 2:
            putPiece(computerUses, line, place)
            isComputerTurn = False
        else:
            isComputerTurn = True

def AISelectPlace():
    preventOpponentLine()
    global isComputerTurn
    if isComputerTurn:
        for line in range(0, len(possibleLines) - 1):
            playCounter = 0
            opponentCounter = 0
            for place in range(0, len(possibleLines[line]) - 1):
                if (board[int(possibleLines[line][place][0])][int(possibleLines[line][place][1])] == "X" and computerUses == "X") or (board[int(possibleLines[line][place][0])][int(possibleLines[line][place][1])] == "O" and computerUses == "O"):
                   playCounter += 1
                if (board[int(possibleLines[line][place][0])][int(possibleLines[line][place][1])] == "X" and computerUses == "O") or (board[int(possibleLines[line][place][0])][int(possibleLines[line][place][1])] == "O" and computerUses == "X"):
                    opponentCounter += 1
            if playCounter == 2:
                for place in range(0, len(possibleLines[line]) - 1):
                    if isEmpty(int(possibleLines[line][place][0]), int(possibleLines[line][place][1])):
                        putPiece(computerUses, int(possibleLines[line][place][0]), int(possibleLines[line][place][1]))
                        # Call end of game
            if opponentCounter == 1:
                break
            if playCounter == 0 and opponentCounter == 0:
                putPiece(computerUses, int(possibleLines[line][place][0]), randint(0, 2))

def askForPlay():
    inputIsInvalid = True
    while inputIsInvalid:
        printBoard()
        row = int(input("On what line would you like to place the piece? (1, 2, 3): "))
        row -= 1
        column = int(input("On what place would you like to place the piece? (1, 2, 3): "))
        column -= 1
        if isEmpty(row, column):
            inputIsInvalid = False
            putPiece(userUses, row, column)
        else:
            print("This location is already taken.")

def selectUsage():
    global isComputerTurn
    print("In this game, X goes first.")
    userUses = input("Which piece would you like to use? (X, O): ")
    if userUses == "X":
        computerUses = "O"
        isComputerTurn = False
    else:
        computerUses = "X"
        isComputerTurn = True

def main():
    selectUsage()
    for x in range(0, 2):
        if isComputerTurn:
            AISelectPlace()
            printBoard()
        else:
            askForPlay()
            printBoard()

main()
