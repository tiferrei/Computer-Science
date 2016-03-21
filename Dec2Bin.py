decNum = int(input("Number: "))
binNum = ""

while decNum != 0:
    if decNum % 2 == 1:
        binNum = "1" + binNum
    else:
        binNum = "0" + binNum
    decNum = decNum / 2

print("Number: "+ binNum)
