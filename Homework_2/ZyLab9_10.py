# Jeremiah Soyebo - 1902930 #

import csv
fileInput = input()
with open(fileInput, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        wordList = set(row)
    for word in wordList:
        count = row.count(word)
        print(word, count)  # cant figure out what I'm doing wrong in zyLabs #
