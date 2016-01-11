NumberOfDays = int(input("How many days will you be walking for? "))
NumberOfDays = NumberOfDays + 1
Total = 0

for x in range(1, NumberOfDays):
    CurrentDay = input("Please enter the name of the day: ")
    StagesForDay = int(input("Please enter the number of stages for " + CurrentDay + ": "))
    StagesForDay = StagesForDay + 1

    for y in range(1, StagesForDay):
        StartStage = int(input("Please enter the start position of stage " + str(y) + ": "))
        EndStage = int(input("Please enter the end position of stage " + str(y) + ": "))

        Total = Total + (EndStage - StartStage)

print("Total distance walked: " + str(Total) + " kilometers.")
WalkingTime = Total / 3
print("Walking time: " + str(WalkingTime) + " hours.")
