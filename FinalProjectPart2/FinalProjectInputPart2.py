# Jeremiah Soyebo - 1902930 #

# System kept throwing me errors for datetime.strptime function, so I threw out my old code and decided to use classes for part 2
import csv
import datetime


class InventoryItem:
    # Initialize class for inventory and items and their details
    def __init__(self, itemID='none', itemManufacturer='none', itemType='none', itemPrice=0, itemServiceDate='',
                 itemCondition=False, itemDamagedInd=''):
        self.itemID = itemID
        self.itemManufacturer = itemManufacturer
        self.itemType = itemType
        self.itemPrice = itemPrice
        self.itemServiceDate = itemServiceDate
        self.itemCondition = itemCondition
        self.itemDamagedInd = itemDamagedInd


class InventoryList:
    listItem = InventoryItem()

    # Create an empty list for the inventory
    def __init__(self, inventoryName='Inventory_initial'):
        self.inventoryName = inventoryName
        self.inventoryList = []

    # Create method to add items to the list
    def addItem(self, listItem):  # adds each inventory item to the list
        self.inventoryList.append(listItem)

    # Create method to update service dates of the item using their ID
    def updateDate(self, idNumber, itemDateUp):
        userItemID = idNumber
        userDateUp = itemDateUp
        # Use for loop to compare IDs and update price
        for listItem in self.inventoryList:
            if listItem.itemID == userItemID:
                listItem.itemServiceDate = userDateUp

    # Create method to update the item prices using their ID
    def updatePrice(self, idNumber, itemPriceUp):
        userItemID = idNumber
        userPriceUp = itemPriceUp
        # Use for loop to compare IDs and update price
        for listItem in self.inventoryList:
            if listItem.itemID == userItemID:
                listItem.itemPrice = userPriceUp

    # Create method to search through inventory
    def inventorySearch(self):

        # Create method to print suggested items
        def printItem(listedItemName):
            print('You might also consider: {}, {} {}, ${}\n'.format(listedItemName[0], listedItemName[1], listedItemName[2],
                                                                     listedItemName[3]))

        # Create method to sort items by price from highest to lowest
        def highestPrice(nameOfList):
            itemCost = nameOfList[3]
            return itemCost

        # Get current date for later comparisons
        currentDate = datetime.date.today()
        print("Hello, welcome to Jeremiah's Jumble! - A store with a 'jumble' of random electronics!\n")
        # Query user for input on their desired items
        userSearch = input("Search for an item by its Manufacturer name and item type: (Enter 'q' at any time to quit.)\n")
        # If the user the user wants to quit before searching anything
        if userSearch == 'q' or userSearch == 'Q':
            print("You have exited. Thanks for trying Jeremiah's Jumble!")
        # Start while loop
        while userSearch != 'q' or userSearch != 'Q':
            # Get user input in split it into a list
            userSearchList = userSearch.split(' ')
            # Create list to store the items the user is searching for
            itemSearchList = []
            # Create list to store similar items in for suggestions
            suggestedList = []

            # Use for loop to iterate through the inventory and compare to the user input
            for listItem in self.inventoryList:
                validList = [listItem.itemID, listItem.itemManufacturer, listItem.itemType, listItem.itemPrice,
                              listItem.itemServiceDate, listItem.itemDamagedInd]
                # Get the items service date and split it
                checkDate = listItem.itemServiceDate.split('/')
                compareDate = datetime.date(int(checkDate[2]), int(checkDate[0]), int(checkDate[1]))
                # Create a list of manufacturers and the item types
                typeManuList = [listItem.itemManufacturer, listItem.itemType]
                checkProduct = all(product in userSearchList for product in typeManuList)
                # Check if items that match aren't past the service date or damaged
                if checkProduct is True and listItem.itemDamagedInd == '' and currentDate < compareDate:
                    # Then add them to the valid list
                    itemSearchList.append(validList)
                # It also takes any matching item names and appends them to the suggestedList.
                if listItem.itemType in userSearchList and (listItem.itemDamagedInd == '') and \
                        (currentDate < compareDate) and listItem.itemManufacturer not in userSearchList:
                    suggestedList.append(validList)
            # If user input does not match any items
            if len(itemSearchList) < 1:
                print('No such item in inventory.\n')

            # Check if items are in the searched list or suggested
            if len(itemSearchList) >= 1 and len(suggestedList) >= 1:
                # Call highestPrice as a key to sort the item search list
                sortedItemList = sorted(itemSearchList, key=highestPrice, reverse=True)
                userSelection = sortedItemList[0]
                # Create an empty list for the suggested item
                userSuggestion = []
                print("Your item is: {}, {} {}, ${}\n".format(userSelection[0], userSelection[1],
                                                              userSelection[2], userSelection[3]))
                closestPrice = 1000000
                for alternateItem in suggestedList:
                    # Use a for loop to iterate through the suggested list and replace item with the closest price
                    itemPriceDiff = abs(alternateItem[3] - userSelection[3])
                    if itemPriceDiff < closestPrice:
                        closestPrice = itemPriceDiff
                        userSuggestion = alternateItem
                # Call printItem to format userSuggestion correctly
                printItem(userSuggestion)

            # If nothing comes up from the userSearchList
            if len(suggestedList) >= 1 and len(userSearchList) > 1:
                if len(itemSearchList) < 1:
                    # Call highestPrice as a key to sort suggestedList by highest price
                    suggestedSortedList = sorted(suggestedList, key=highestPrice, reverse=True)
                    suggestedSortedItem = suggestedSortedList[0]
                    # Call printItem to format the most expensive item correctly
                    printItem(suggestedSortedItem)

            # Prompt the user for their next input
            userSearch = input('Search for an item by its manufacturer name and its type:\n (Note - Please do not use adjectives)\n')
            #  When user quits exit the loop
            if userSearch == 'q' or userSearch == 'Q':
                print("You have exited. Thanks for trying Jeremiah's Jumble!")
                break


# Main section of code
if __name__ == "__main__":

    validItemInventory = InventoryList()
    # Open manufacturer list and read from it
    with open('ManufacturerList.csv', 'r') as myFile:
        manuList = csv.reader(myFile)

        # Iterate through the manufacturer list and assign items to the class
        for item in manuList:
            currentItem = InventoryItem()
            itemValues = []
            # Assign each value to the class variable
            for value in item:
                itemValues.append(value)
            currentItem.itemID = itemValues[0]
            currentItem.itemManufacturer = itemValues[1].strip()
            currentItem.itemType = itemValues[2]
            if len(itemValues[3]) >= 1:
                currentItem.itemCondition = True
                currentItem.itemDamagedInd = itemValues[3] 
            validItemInventory.addItem(currentItem)
    # Open price list and read from it
    with open('PriceList.csv', 'r') as myFile:
        priceList = csv.reader(myFile)  
        # Iterate through price list and add prices to valid inventory
        for idNumPrice in priceList:
            validItemInventory.updatePrice(idNumPrice[0], int(idNumPrice[1]))
    # Open service dates list and read from it
    with open('ServiceDatesList.csv', 'r') as myFile: 
        datesList = csv.reader(myFile)
        # Iterate through service dates list and add dates to valid inventory
        for idNumDate in datesList:
            validItemInventory.updateDate(idNumDate[0], idNumDate[1])

    # Call the search to have the user search from the valid inventory
    validItemInventory.inventorySearch()  
