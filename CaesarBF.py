import time
import sys
import csv

with open("dictionary.csv") as csvfile:
    dictionaryCSV = csv.reader(csvfile, delimiter="\n")

    words = []

    for row in dictionaryCSV:
        word = row[0]

        words.append(word)

message = input("Message to brute force: ")
message = message.upper()

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

decryptedMessage = ""

for i in range(1,26):
    looper = i
    for x in range(len(message)):
        letter = message[x]
        letter = letter.upper()
        currentLetter = Letters.index(letter)
        newLetter = currentLetter + (looper - 1)
        if newLetter > 25:
            newLetter = newLetter - 26
        decryptedLetter = Letters[newLetter]
        decryptedMessage = decryptedMessage + decryptedLetter
    print("ROT" + str(i-1) + " -> " + decryptedMessage)
    if decryptedMessage in(words):
        print("This is the real word")
    decryptedMessage = ""


# from nltk.corpus import words
# word_list = words.words()
