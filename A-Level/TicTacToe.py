import sys
import time

board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
isComputerTurn = False
computerUsesX = False


def printBoard():
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")

printBoard()
