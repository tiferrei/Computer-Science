import csv

with open("dictionary.csv") as csvfile:
    dictionaryCSV = csv.reader(csvfile, delimiter="\n")

    words = []

    for row in dictionaryCSV:
        word = row[0]

        words.append(word)

if decryptedMessage in(words):
    print("This is the real word")
