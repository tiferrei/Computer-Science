import csv
capitalQuestions = []
points = 0
with open ("Capitals.txt") as csvfile:
    capitalsCsv = csv.reader(csvfile, delimiter = ",")
    for row in capitalsCsv:
        capitalQuestions.append(row)
numberOfQuestions = len(capitalQuestions)
for x in range(numberOfQuestions):
    print(capitalQuestions[x][1])
    print()
    print("A -> " + capitalQuestions[x][3])
    print("B -> " + capitalQuestions[x][4])
    print("C -> " + capitalQuestions[x][5])
    print("D -> " + capitalQuestions[x][6])
    userChoice = input("Answer (A, B, C, D): ")
    userChoice = userChoice.upper()
    if userChoice == capitalQuestions[x][2]:
        print("Correct!")
        points = points + 1
    else:
        print("Wrong!")
print("You scored " + str(points) + " points!")
