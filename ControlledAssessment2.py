#  Controlled Assessment 2
#  Created by Tiago Ferreira on 15/09/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

custNumber = 0
dateOfEstimate = ""
numberOfRooms = 0
rooms = []
typeOfEmployee = ""

def menu():
    print("Welcome Caroline!")
    print()
    print("Available options:")
    print("A -> Register new order")
    choise = input("Please select an option (A): ")
    if choise == "A":
        registerNewOrder()

def registerNewOrder():
    print("Please enter some info:")
    global custNumber
    global dateOfEstimate
    global numberOfRooms
    global rooms
    global typeOfEmployee
    custNumber = int(input("Customer Number: "))
    dateOfEstimate = input("Date of estimate: ")
    numberOfRooms = int(input("Number of rooms that require painting: "))
    rooms = []
    for room in range(1, numberOfRooms+1):
        name = input("Room name: ")
        numberOfWalls = int(input("Number of walls in the " + str(name) + ": "))
        hasWallpaperStr = input("Is there wallpaper that needs to be removed (YES, NO)? ")
        if hasWallpaperStr == "YES":
            hasWallpaper = True
        else:
            hasWallpaper = False
        walls = []
        for wall in range(1, numberOfWalls+1):
            width = float(input("Width of wall #" + str(wall) + ": "))
            height = float(input("Height of wall #" + str(wall) + ": "))
            area = width * height
            walls.append(area)
        tempList = [name, numberOfWalls, hasWallpaper, walls]
        rooms.append(tempList)
    typeOfEmployee = input("Type of employee (AP, FQ): ")
    calculateOrder()

def calculateOrder():
    price = 0
    global numberOfRooms
    global rooms
    global typeOfEmployee
    print()
    for room in range(1, numberOfRooms+1):
        print(rooms[room-1][0] + ":")
        if rooms[room-1][2] == True:
            price += 70
            print("     Remove wallpaper –> £70")
        for wall in range(1, len(rooms[room-1][3])+1):
            print("     Wall #" + str(wall) + " –> £" + str(15 * rooms[room-1][3][wall-1]))
            price += 15 * rooms[room-1][3][wall-1]
    if typeOfEmployee == "AP":
        price += 100
        print("Apprentice painter –> £100")
    else:
        price += 250
        print("Fully-qualified painter –> £250")
    print()
    print("Order price: £" + str(price))
    totalPrice = (price * 120) / 100
    print("Order + VAT: £" + str(totalPrice))
    print()
    askRestart()

def askRestart():
    wantsTo = input("Would you like to generate another estimate (YES, NO)? ")
    if wantsTo == "YES":
        menu()
    else:
        print("Goodbye.")

menu()
