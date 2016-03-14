import sys, time, os

animals = []

print("Welcome!")

def menu():
    time.sleep(0.3)
    print()
    print("What do you want to do?")
    print()
    time.sleep(0.3)
    print("1 - Add animals to the list")
    print("2 - Show list of animals")
    print("3 - Remove animals from list")
    print("4 - Show position of animal in the list")
    print("5 - Exit")
    time.sleep(0.5)
    print()

    userNumber = int(input("-> "))

    if userNumber == 5:
        sys.exit()
    elif userNumber == 4:
        detectAnimal()
    elif userNumber == 3:
        remove()
    elif userNumber == 2:
        printList()
    elif userNumber == 1:
        add()

def remove():
    if len(animals) == 0:
        os.system('clear')
        print("The list is empty, you can't remove anything.")
        time.sleep(1)
        os.system('clear')
        menu()
    else:
        os.system('clear')
        print(animals)
        removeAnimal = input("Which animal do you want to remove? (zebra): ")
        animals.remove(removeAnimal)
        print('Done. The animal "' + removeAnimal + '" has been removed.')
        os.system('clear')
    menu()

def printList():
    os.system('clear')
    print(animals)
    os.system('clear')
    menu()

def add():
    os.system('clear')
    addAnimal = input("What animal do you want to add? (zebra): ")
    animals.append(addAnimal)
    print('Done, added the animal "' + addAnimal + '" to the list.')
    os.system('clear')
    menu()

def detectAnimal():
    os.system('clear')
    nameAnimal = input("What animal do you want to know the position? (zebra): ")
    indexAnimal = animals.index(nameAnimal)
    print('"' + nameAnimal + '" is on index ' + str(indexAnimal))
    os.system('clear')
    menu()

menu()
