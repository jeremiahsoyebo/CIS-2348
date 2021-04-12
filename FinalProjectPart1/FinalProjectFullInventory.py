# Jeremiah Soyebo - 1902930 #

import csv

# Create empty list for manufacturing, date, and price data
manuList = []
priceList = []
dateList = []

# Open Manufacturing list and add to string
with open('ManufacturerList.csv', 'r') as myFile:
    reader = csv.reader(myFile, delimiter=',')

    for row in reader:
        manuList.append(row)

# Open PriceList and add to empty string
with open('PriceList.csv') as myFile:
    reader = csv.reader(myFile, delimiter=',')

    for row in reader:
        priceList.append(row)

# Open ServiceDatesList and add to empty string
with open('ServiceDatesList.csv') as myFile:
    reader = csv.reader(myFile, delimiter=',')

    for row in reader:
        dateList.append(row)

# Sort the list by Company Name
manuList.sort(key=lambda name_sort: (name_sort[1])) # Wasn't sure how else to sort so I used Lambda, hopefully that's fine

# Merge all three lists to make a final list for FullInventory
for name in range(0, len(manuList)):
    for date in range(0, len(dateList)):
        if manuList[name][0] == dateList[date][0]:
            comb = manuList[name]
            # Add combination to spot in the list
            comb.insert(4, dateList[date][1])

for name in range(0, len(manuList)):
    for price in range(0, len(priceList)):
        if manuList[name][0] == priceList[price][0]:
            comb2 = manuList[name]
            # Add combination to spot in the list
            comb2.insert(3, priceList[price][1])


# Open FullInventory and add write the list to it
file = open('FullInventory.csv', 'w')
for i in range(0, len(manuList)):
    for j in range(0, 6):
        if j != 5:
            line = manuList[i][j] + ','
        else:
            line = manuList[i][j]
        # Write to file output and start newline
        file.write(line)
    file.write('\n')
file.close()
