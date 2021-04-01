# Jeremiah Soyebo - 1902930 #

myList = input()

posList = [int(num) for num in myList.split() if int(num) >= 0]

posList.sort()

for value in posList:
    print(value, end=' ')





