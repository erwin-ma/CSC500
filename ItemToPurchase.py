'''
This defines the ItemToPurchase class, which represents items available to purchase.
Attributes:
 - item_name (str): Name of the item
 - item_price (float): price of the item
 - item_quantity(int): Number of items
 
Methods:
 - print_item_cost(): Prints the item name, quantity, price, and total
 
Note: This was originally from week 4, but modified further to add description and defaults
In addition, commented out __main__ since ShoppingCart has the main script now.
'''
 
# defining the class first
class ItemToPurchase:
    def __init__(self, name='none', price=0.0, quantity=0, description='none'):
    # setting initial attributes here
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
 
    # print method
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${self.item_quantity * self.item_price:.0f}')
 
'''# putting the script under main
if __name__ == '__main__':
    # the instructions don't seem like they need a list,
    # but the rubric says to demonstrate dictionary, vector, or list
    # so, creating a list of items
    item_list = []
    
    # instead of prompting for item 1 and item 2 explicitly, 
    # will loop and add to list
    # this makes it easy to increase # of items later too
    for i in range(1, 3):
        print(f"Item {i}")
        
        # instantiate the item
        item = ItemToPurchase()
 
        # get the item name
        item.item_name = input("Enter the item name: ")
 
        # using loop to validate data with try/except
        while True:
            try:
                item.item_price = float(input('Enter the item price: $'))
                break # exit loop if it *doesn't* get excepted 
            except ValueError:
                print("Invalid input. Please enter a valid price (e.g. 1.99)")
        
        while True:
            try:
                item.item_quantity = int(input('Enter the item quantity: '))
                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity (e.g. 2)")
        
        print()
        item_list.append(item)
 
    # calculate the total. 
    grand_total = 0
    for item in item_list:
        grand_total += item.item_quantity * item.item_price
 
 
    # print subtotals and totals
    print('\nTOTAL COST')
    
    # call print method for each item in list
    for item in item_list:
        item.print_item_cost()
    
    # print grand total
    print(f'Total: ${grand_total:.2f}')



'''


