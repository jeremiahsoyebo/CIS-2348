# Jeremiah Soyebo - 1902930 #

# Declare the class ItemToPurchase
class ItemToPurchase:

    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # print the output in a specifed format
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
                                            (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    # Implement the method print_item_description

    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)
        print(string, end='\n')
        return string


# Declare the class ShoppingCart

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, string):
        print('\nADD ITEM TO CART', end='\n')
        item_name = str(input('Enter the item name: '))
        item_description = str(input('\nEnter the item description: '))
        item_price = int(input('\nEnter the item price: '))
        item_quantity = int(input('\nEnter the item quantity: '))

        # Append the above values in to the list
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))
