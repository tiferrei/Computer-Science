#  Board
#  Tic Tac Toe

#  Created by Tiago Ferreira on 17/09/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

class Board(object):
    possibleLines = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"],
                     ["00", "10", "20"], ["01", "11", "21"], ["02", "12", "22"],
                     ["00", "11", "22"], ["20", "11", "02"]]

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def validatePiece(piece):
        pieceIsInvalid = True
        while pieceIsInvalid():
            if piece == "X" or piece == "O":
                pieceIsInvalid = False
            else:
                print("This piece is invalid.")
                piece = input("Please enter X or O: ")

    def printBoard(self):
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " ")
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " ")
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " ")

    def blockIsEmpty(self, row, column):
        if self.board[row][column] == " ":
            return True
        else:
            return False
