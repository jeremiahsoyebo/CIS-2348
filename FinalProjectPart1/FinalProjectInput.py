# Jeremiah Soyebo - 1902930 #

import csv
from datetime import datetime

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

inventory = []
for i in range(0, len(manuList)):
    inventory.append(manuList[i][2])

# Convert list to dictionary
inventory = list(dict.fromkeys(inventory))

# Create empty lists for inventory files
inventoryItem = []
inventoryItem = manuList
categoryInventory = []
for jj in range(0, len(inventory)):
    for ii in range(0, len(inventoryItem)):
        # Get item type and add csv extension to make the file name
        itemType = inventory[jj] + "Inventory.csv"
        if inventory[jj] == inventoryItem[ii][2]:
            categoryInventory.append(inventoryItem[ii])

    # Remove the item from the file
    for x in range(0, len(categoryInventory)):
        del (categoryInventory[x][2])
    # Sort by inventory by ID
    categoryInventory.sort(key=lambda id_sort: (id_sort[0]))
    
    # Open files using itemType and write through them
    file = open(itemType, 'w')
    for i in range(0, len(categoryInventory)):
        for j in range(0, 5):
            if j != 4:
                line = categoryInventory[i][j] + ','
            else:
                line = categoryInventory[i][j]
            file.write(line)
        file.write('\n')
    file.close()
    categoryInventory = []


# Open Full Inventory and add data to it
with open('FullInventory.csv') as myFile:
    reader = csv.reader(myFile, delimiter=',')

    for row in reader:
        manuList.append(row)

pastService = manuList
serviceDate = []

# Iterate through dates
for i in range(0, len(pastService)):
        currentDate = datetime.now()
        a = pastService[i][4]
        dates = datetime.strptime(a, '%m/%d/%Y')
        # Compare dates
        if dates <= currentDate:
            serviceDate.append(pastService[i])

# Sort by service date
serviceDate.sort(reverse=True)

# Open Past Service Date file and write to it
file = open('PastServiceDateInventory.csv', 'w')
for i in range(0, len(serviceDate)):
    for j in range(0, 6):
        if j != 5:
            line = serviceDate[i][j] + ','
        else:
            line = serviceDate[i][j]
        file.write(line)
    file.write('\n')
file.close()

# Transfer items from the Manufacturing list
damagedItems = manuList
# Create empty list for items that are actually damaged
damagedInventory = []

# Add the damaged items
for i in range(0, len(damagedItems)):
    if damagedItems[i][5] == 'damaged':
        damagedInventory.append(damagedItems[i])

# Sort the damaged inventory prices
damagedInventory.sort(reverse=True)

# Open the Damaged Inventory file and write to it
file = open('DamagedInventory.csv', 'w')
for i in range(0, len(damagedInventory)):
    for j in range(0, 5):
        if j != 4:
            line = damagedInventory[i][j] + ','
        else:
            line = damagedInventory[i][j]
        file.write(a)
    file.write('\n')
file.close()


