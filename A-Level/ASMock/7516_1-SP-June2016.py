#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random

def GetRowColumn():
    print()
    Column = int(input("Please enter column: ")) # Get coordinates from user.
    Row = -1
    while Row not in range(0,10):
        Row = int(input("Please enter row: ")) # Get coordinates from user.
        if Row not in range(0,10):
            print("Invalid value entered")
    print()
    return Row, Column

def MakePlayerTorpedoMove(Board, Ships):
    Row, Column = GetRowColumn() # Call func to get coordinates
    if Board[Row][Column] in ["A", "B", "S", "D", "P", "h"]:
        print("Hit at (" + str(Column) + "," + str(Row) + ").")
        CheckSunk(Row, Column, Board, Ships)
        Board[Row][Column] = "h"
    elif Board[Row][Column] in ["m", "-"]:
        Board[Row][Column] = "m"
        while Row != 0 and Board[Row][Column] != "h":
            Row -= 1
            if Board[Row][Column] in ["A", "B", "S", "D", "P", "h"]:
                print("Hit at (" + str(Column) + "," + str(Row) + ").")
                CheckSunk(Row, Column, Board, Ships)
                Board[Row][Column] = "h"
            else:
                Board[Row][Column] = "m"

def MakePlayerMove(Board, Ships):
    Row, Column = GetRowColumn() # Call func to get coordinates
    if Board[Row][Column] == "m" or Board[Row][Column] == "h": # Check for validity
        print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
    elif Board[Row][Column] == "-": # Check for misses
        print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
        Board[Row][Column] = "m"
    else: # Check for hits.
        print("Hit at (" + str(Column) + "," + str(Row) + ").")
        CheckSunk(Row, Column, Board, Ships)
        Board[Row][Column] = "h"

def CheckSunk(Row, Column, Board, Ships):
    for ship in Ships:
        if Board[Row][Column] == ship[0][:1]:
            ship[1] -= 1
        if ship[1] == 0:
            print(ship[0] + " is sunk!")

def SetUpBoard():
    Board = [] # define empty board
    for Row in range(10): # Make board a 2D list
        BoardRow = []
        for Column in range(10):
            BoardRow.append("-")
        Board.append(BoardRow) # Make board emmpty.
    return Board

def LoadGame(Filename, Board):
    BoardFile = open(Filename, "r") # Get the boardfile form FS.
    for Row in range(10):
        Line = BoardFile.readline() # Read each line
        for Column in range(10):
            Board[Row][Column] = Line[Column] # Fill in the board with the file content.
    BoardFile.close() # Close file after reading.

def PlaceRandomShips(Board, Ships):
    for Ship in Ships: # For every ship type available.
        Valid = False
        while not Valid:
            Row = random.randint(0, 9) # Define random position.
            Column = random.randint(0, 9)
            HorV = random.randint(0, 1) # Define orientation
            if HorV == 0:
                Orientation = "v" # Set orientation depending on random result.
            else:
                Orientation = "h"
            Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation) # Validate the ship positioning.
        print("Computer placing the " + Ship[0])
        PlaceShip(Board, Ship, Row, Column, Orientation) # Place it.

def PlaceShip(Board, Ship, Row, Column, Orientation):
    if Orientation == "v": # Depending on orientation, fill the board with the ship ID letter.
        for Scan in range(Ship[1]):
            Board[Row + Scan][Column] = Ship[0][0] # Fill vertically
    elif Orientation == "h":
        for Scan in range(Ship[1]):
            Board[Row][Column + Scan] = Ship[0][0] # Fill horizontally.

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
    if Orientation == "v" and Row + Ship[1] > 10: # Check if ship fits in the board.
        return False
    elif Orientation == "h" and Column + Ship[1] > 10: # Check if ship fits in the board.
        return False
    else:
        if Orientation == "v":
            for Scan in range(Ship[1]):
                if Board[Row + Scan][Column] != "-": # Make sure the space is not taken already.
                    return False
        elif Orientation == "h":
            for Scan in range(Ship[1]):
                if Board[Row][Column + Scan] != "-": # Make sure the space is not taken already.
                    return False
    return True

def CheckWin(Board):
    for Row in range(10):
        for Column in range(10):
            if Board[Row][Column] in ["A","B","S","D","P"]: # Check if the game is over by checking if there are any ships left.
                return False
    return True

def PrintBoard(Board):
    print()
    print("The board looks like this: ")
    print()
    print (" ", end="")
    for Column in range(10): # Print board space by space.
        print(" " + str(Column) + "    ", end="")
    print()
    for Row in range(10):
        print (str(Row) + " ", end="") # Print row header
        for Column in range(10): # Print grid with board content.
            if Board[Row][Column] == "-":
                print(" ", end="")
            elif Board[Row][Column] in ["A","B","S","D","P"]:
                print(" ", end="")
            else:
                print(Board[Row][Column], end="")
            if Column != 9: # Print seperators.
                print(" | ", end="")
        print()

def DisplayMenu():
    print("MAIN MENU") # Display the menu options.
    print()
    print("1. Start new game")
    print("2. Load training game")
    print("9. Quit")
    print()

def GetMainMenuChoice():
    print("Please enter your choice: ", end="") # Get user choice form menu options.
    Choice = int(input())
    print()
    return Choice

def PlayGame(Board, Ships):
    usedTorpedo = False
    GameWon = False # By default the game is not won.
    while not GameWon:
        PrintBoard(Board) # Print board

        if not usedTorpedo:
            wantsToUseTorpedo = input("Fire a torpedo (Y/N)? ")
            if wantsToUseTorpedo == "Y":
                MakePlayerTorpedoMove(Board, Ships)
                usedTorpedo = True
            else:
                MakePlayerMove(Board, Ships) # Ask the player for a move
        else:
            MakePlayerMove(Board, Ships) # Ask the player for a move
        GameWon = CheckWin(Board) # Check if the move altered the status of the game.
        if GameWon: # If it did:
            print("All ships sunk!") # End game.
            print()

if __name__ == "__main__":
    TRAININGGAME = "Training.txt" # Define board file to be used for training.
    MenuOption = 0 # Define the menu option selected.
    while not MenuOption == 9:
        Board = SetUpBoard() # Setup board.
        Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]] # Define ships option.
        DisplayMenu() # Display menu.
        MenuOption = GetMainMenuChoice() # Get choice from user.
        if MenuOption == 1: # If the menu choice is 1:
            PlaceRandomShips(Board, Ships) # Place random ships on the board
            PlayGame(Board,Ships) # Play game (i.e. evaluate game status and ask for move.)
        if MenuOption == 2: # If the menu choice is 2:
            LoadGame(TRAININGGAME, Board) # Load the game from the file.
            PlayGame(Board, Ships) # Play game (i.e. evaluate game status and ask for move.)
