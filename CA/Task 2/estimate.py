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

custNumber = 0 # Declaration and initialization of main variables.
dateOfEstimate = ""
numberOfRooms = 0
rooms = []
typeOfEmployee = ""

def menu(): # Menu declaration
    print("Welcome Caroline!")
    print()
    print("Available options:")
    print("A -> Register new order")
    choise = input("Please select an option (A): ")
    if choise == "A":
        registerNewOrder() # Call to registerNewOrder function.

def registerNewOrder(): # register function declaration.
    print("Please enter some info:")
    global custNumber # Global declarations
    global dateOfEstimate
    global numberOfRooms
    global rooms
    global typeOfEmployee
    custNumber = int(input("Customer Number: "))
    dateOfEstimate = input("Date of estimate: ")
    numberOfRooms = int(input("Number of rooms that require painting: "))
    rooms = [] #Empty rooms list
    for room in range(1, numberOfRooms+1): # For each room
        name = input("Room name: ") # Get info
        numberOfWalls = int(input("Number of walls in the " + str(name) + ": "))
        hasWallpaperStr = input("Is there wallpaper that needs to be removed (YES, NO)? ")
        if hasWallpaperStr == "YES":
            hasWallpaper = True
        else:
            hasWallpaper = False
        walls = [] #empty wall list
        for wall in range(1, numberOfWalls+1):
            width = float(input("Width of wall #" + str(wall) + ": ")) # get data
            height = float(input("Height of wall #" + str(wall) + ": "))
            area = width * height
            walls.append(area) # append each wall
        tempList = [name, numberOfWalls, hasWallpaper, walls] #create tempList
        rooms.append(tempList) # Cahce data
    typeOfEmployee = input("Type of employee (AP, FQ): ")
    calculateOrder() # Call to calculateOrder

def calculateOrder():
    price = 0
    global numberOfRooms # Global declarations
    global rooms
    global typeOfEmployee
    print()
    for room in range(1, numberOfRooms+1): # For each room...
        print(rooms[room-1][0] + ":")
        if rooms[room-1][2] == True:
            price += 70
            print("     Remove wallpaper –> £70")
        for wall in range(1, len(rooms[room-1][3])+1): #For each wall print the price
            print("     Wall #" + str(wall) + " –> £" + str(15 * rooms[room-1][3][wall-1]))
            price += 15 * rooms[room-1][3][wall-1] # Print the total for the room.
    if typeOfEmployee == "AP": #Add price of employee.
        price += 100
        print("Apprentice painter –> £100")
    else:
        price += 250
        print("Fully-qualified painter –> £250")
    print()
    print("Order price: £" + str(price)) # Print total
    totalPrice = (price * 120) / 100
    print("Order + VAT: £" + str(totalPrice)) # Print total with vat
    print()
    askRestart() # Call to restart.

def askRestart(): # Declaration fo restart function.
    wantsTo = input("Would you like to generate another estimate (YES, NO)? ")
    if wantsTo == "YES":
        menu() #Call to menu
    else:
        print("Goodbye.") # See ya, exit program.

menu() # Start program.
