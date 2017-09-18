#  Game
#  Tic Tac Toe

#  Created by Tiago Ferreira on 14/09/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from Board import Board

class Game(object):
    gameCount = 0
    def __init__(self):
        Game.gameCount += 1
        self.board = Board()
        self.computerUses = ""
        self.playerUses = ""
        self.isComputerTurn = True

    def start(self):
        print("In this game the X goes first.")
        inputIsInvalid = True
        while inputIsInvalid:
            playerWantsToUse = input("Which piece would you like to be? (X, O): ")
            if playerWantsToUse == "X":
                self.playerUses = "X"
                self.computerUses = "O"
                inputIsInvalid = False
            elif playerWantsToUse == "O":
                self.playerUses = "O"
                self.computerUses = "X"
                inputIsInvalid = False
