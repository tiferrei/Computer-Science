#ShoppingList

#  Created by Tiago Ferreira on 01/03/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import os, time, sys

def menu():
    time.sleep(0.3)
    print()
    print("What do you want to do?")
    print()
    time.sleep(0.3)
    print("1 - Add items to the list")
    print("2 - Show shopping list")
    print("3 - Remove items from list")
    print("4 - Exit")
    time.sleep(0.5)
    print()
    userNumber = int(input("-> "))
    if userNumber == 4:
        os.system('clear')
        print("See you!")
        sys.exit()
    elif userNumber == 3:
        os.system('clear')
        removeItems()
    elif userNumber == 2:
        os.system('clear')
        listItems()
    elif userNumber == 1:
        os.system('clear')
        addItems()
    else:
        os.system('clear')
        print("Please selecet a vaild number: ")
        menu()

def addItems():
    if os.path.isfile("shopping.txt") == False:
        with open("shopping.txt", mode="w", encoding="utf-8") as newFile:
            newFile.write()

    addData = input("Items to add: ")
    with open("shopping.txt", mode="a", encoding="utf-8") as writeFile: ##initialize file in write mode
        writeFile.write(addData + "\n")

def listItems():
    if os.path.isfile("shopping.txt") == False:
        print("List non-existant, creating blank shopping list.")
        with open("shopping.txt", mode="w", encoding="utf-8") as newFile:
            newFile.write()

    with open("shopping.txt", mode="r", encoding="utf-8") as readFile: ##initialize file in read mode
        for line in readFile: #for every line
            print(line.rstrip("\n")) #Print it without extra line

def removeItems():
    itemToRemove = input("Which item would you like to remove? ")
    with open("shopping.txt", mode="r", encoding="utf-8") as readFile: ##initialize file in read mode
        lines = readFile.readline()
        with open("shopping.txt", mode="w", encoding="utf-8") as removeFromFile:
            for line in lines:
                 if line != itemToRemove + "\n":
                     removeFromFile.write(line)

def priorityItems():
    itemToGet = input("Item to check priority: ")

menu()
