import time

fileRead = open("whatever.txt", "r")
fileWrite = open("whatever.txt", "a")
dataToEnter = str(input("Enter data: "))
fileWrite.write(dataToEnter)
fileWrite.close()
time.sleep(1)
data = fileRead.read()
print(data)
fileRead.close()
