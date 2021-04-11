# Jeremiah Soyebo - 1902930 #

import csv

# Open ManufacturerList and read from it
InventoryList = []
with open('ManufacturerList.csv', 'r') as myFile:
    reader = csv.reader(myFile, delimiter=',')
    for row in reader:
        InventoryList.append(row[0])
        InventoryList.append(row[1])
        InventoryList.append(row[2])
        InventoryList.append(row[3])


# Create empty list to add file input to
priceList = []
with open('PriceList.csv', 'r') as myFile:
    reader = csv.reader(myFile, delimiter=',')
    for row in reader:
        # Get the Prices row from the file and add it to empty list
        priceList.append(row[1])

# Add prices information to main inventory list
InventoryList.extend(priceList)

# Create empty list to add file input to
serviceDatesList = []
# Open ServiceDatesList and read from it
with open('ServiceDatesList.csv', 'r') as myFile:
    reader = csv.reader(myFile, delimiter=',')
    for row in reader:
        # Get date row from the file and append it to empty list created
        serviceDatesList.append(row[1])

# Add service dates to main inventory list
InventoryList.extend(serviceDatesList)

with open('FullInventory.csv', 'w') as myFile:
    writer = csv.writer(myFile)

    writer.writerow(InventoryList)





