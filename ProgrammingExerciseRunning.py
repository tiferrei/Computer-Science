#Programming Exercise Runnung

#  Created by Tiago Ferreira on 13/01/2016.
#  Copyright (c) 2016 Tiago Ferreira. All rights reserved.

Total = 0 #Set default value for distance
NumberOfDays = int(input("How many days will you be walking for? ")) #Get number of days.
for x in range(NumberOfDays): #Loop for number of days.
    CurrentDay = input("Please enter the name of the day: ") #Get current day name.
    StagesForDay = int(input("Please enter the number of stages for " + CurrentDay + ": ")) #How many stages in this day
    for y in range(StagesForDay):#loopfor stages in a day
        StartStage = int(input("Please enter the start position of stage " + str(y + 1) + ": "))#get start position
        EndStage = int(input("Please enter the end position of stage " + str(y + 1) + ": "))#get end position
        Total = Total + (EndStage - StartStage)#overall km calculation
print("Total distance walked: " + str(Total) + " kilometers.")#print total distance
WalkingTime = Total / 3 #Get walking time.
print("Walking time: " + str(WalkingTime) + " hours.") #print walking time.
