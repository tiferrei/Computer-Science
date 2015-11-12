animals = []

num = 1 + int(input("How many animals do you want to add? "))

for n in range(1,num):
    animalToAdd = input("which animal do you want to add? ")
    animals.append(animalToAdd)


Reversed = input("Do you want your list reversed? (YES, NO): ")

if Reversed == "YES":

    animals.reverse()
    print(animals)
else:

    print(animals)

numberOnArray = int(input("Choose a number from 1 to " + str(num) + ". "))

print(animals[numberOnArray])
