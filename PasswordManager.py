import sys

username = input("Add username: ")
password = input("Add password: ")

with open("Username.txt", mode="a", encoding="utf-8") as writeUsernameFile: ##initialize file in append mode
    writeUsernameFile.write(username + "\n")

with open("Password.txt", mode="a", encoding="utf-8") as writePasswordFile: ##initialize file in append mode
    writePasswordFile.write(password + "\n")

username = input("Username: ")
password = input("Password: ")

with open("Username.txt", mode="r", encoding="utf-8") as readUsernameFile: ##initialize file in append mode
    for line in readUsernameFile:
        line = line.rstrip("\n")
        if line == username:
            with open("Password.txt", mode="r", encoding="utf-8") as readPasswordFile: ##initialize file in append mode
                line = line.rstrip("\n")
                if line == password:
                    print("User logged in")
                    sys.exit()
    print("Login incorrect")
