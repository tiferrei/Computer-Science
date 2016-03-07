with open("shopping.txt", mode="r", encoding="utf-8") as readFile: ##initialize file in read mode
    for line in readFile: #for every line
        print(line.rstrip("\n")) #Print it without extra line
