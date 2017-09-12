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

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
possibleLines = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"],
                 ["00", "10", "20"], ["01", "11", "21"], ["02", "12", "22"],
                 ["00", "11", "22"], ["20", "11", "02"]]
isComputerTurn = False
computerUsesX = False

def printBoard():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")

def isEMpty(row, column):
    if board[row][column] == " ":
        return True
    else:
        return False

def putPiece(piece, row, column):
    if isEmpty(row, column):
        board[row][column] = piece

def preventOpponentLine():
  if isComputerTurn:
    for line in len(possibleLines):
      opponentCounter = 0
      for place in possibleLines[line]:
        if board[line][place] == "X" and computerUses == "X":
          break
      else:
        opponentCounter = opponentCounter+1
    if opponentCounter == 2:
      putPiece(line,place)
      isComputerTurn = False
    else:
      isComputerTurn = True

def AISelectPlace():
