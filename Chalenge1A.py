animals = []
num = input("How many animals do you want to add? ")
for n in range(1,(num + 1)):
    animalToAdd = input("which animal do you want to add? ")
    animals.append(animalToAdd)

Reversed = input("Do you want your list reversed? (YES, NO): ")

if Reversed == "YES":
    animalsReversed = [animals.sort()]
    print(animalsReversed)
else:
    print(animals)
