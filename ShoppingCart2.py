'''
This defines the ShoppingCart class, which has methods to manipulate a list
of items. Imports ItemsToPurchase.py from week 4
Attributes:
 - customer_name (str): Name of customer
 - current_date (str): date as a string
 - cart_items (list): List to hold ItemsToPurchase
 
Methods:
 - add_item(): appends item to cart_items list
 - remove_item(): removes item from cart_items list
 - modify_item(): changes name, price or quantity of item in list
 - get_num_items_in_cart(): sum of all item quantities
 - get_cost_of_cart(): sum of all item price*quantity
 - print_total(): calculates then prints the total cost
 - print_descriptions(): prints description of every item
 
Main prompts for user name and date, instantiates a ShoppingCart
and then prints a menu until the user is done.
'''

# mostly re-used from week 4
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

# defining ShoppingCart class
class ShoppingCart:
    # initialization, with defaults per instructions.
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # setting basic attributes
        self.customer_name = customer_name
        # note that this is a string, not DateTime
        self.current_date = current_date  
        self.cart_items = []  # this is a list of items

    def add_item(self, item):
        # list append
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # loop through all items
        for i, item in enumerate(self.cart_items):
            # check if the name matches
            if item.item_name == item_name:
                # use list remove
                del self.cart_items[i]
                # need an empty return, otherwise the below will print.
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        # loop through number of items in cart
        for i, item in enumerate(self.cart_items):
            # check if name matches (exists)
            if item.item_name == modified_item.item_name:
                # go through each description , price, and quantity.
                # for each, check if it's none or 0.
                # if not, then update the *cart_items* to the *parameter*
                if modified_item.item_description != "none":
                    self.cart_items[i].item_description = modified_item.item_description
                if modified_item.item_price != 0.0:
                    self.cart_items[i].item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    self.cart_items[i].item_quantity = modified_item.item_quantity
                # again, preventing print using return
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # easy to call from module 4 ItemToPurchase
        # we should sum in case multiple items
        # use list comprehension to loop
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        # easy to call from module 4 ItemToPurchase
        # need to sum through each item
        # use list comprehension to loop.
        return sum(item.item_quantity * item.item_price for item in self.cart_items)

    def print_total(self):
        # follow instruction format
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        
        # check if cart is empty. interrupt with return if so
        num_items = self.get_num_items_in_cart()
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
            return
 
        # use get_num_items defined above, instead
        print("Number of Items:", self.get_num_items_in_cart())
 
        # loop through each item
        for item in self.cart_items:
            # print the cost
            item.print_item_cost()
 
        # print the total
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.0f}")
 
    def print_descriptions(self):
        # use format from instructions
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        # loop through each item and print description
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    # loop until we quit.
    while True:
        # this menu is from instruction example
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity, price, or description")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        # need to store user option
        choice = input("Choose an option: ").lower()

        # if-else nest for all the options
        if choice == 'a':
            # creates the item
            item = ItemToPurchase()  

            # prompt for name, description, price, and quantity
            item.item_name = input("Give the item a name: ")
            item.item_description = input("Describe the item: ")

            # adding some validation for price and quantity
            try:
                item.item_price = float(input("What does the item cost? $"))
                item.item_quantity = int(input("How many do you want? "))

                # have to add it to the shopping cart class
                cart.add_item(item)
            except ValueError:
                print("Invalid input for price or quantity")

        elif choice == 'r':
            item_name = input("Which item do you want to remove? ")
            # we can call the cart's remove_item, which takes care of
            # item not existing
            cart.remove_item(item_name)

        elif choice == 'c':
            # this is a bit odd. We have to create the item first, 
            # and then pass it to the cart to modify
            # first, get all the inputs. Defaults/blanks are fine.
            item_name = input("Which item do you want to modify?: ")
            new_description = input("What is the new description? (Press Enter for default): ")
            new_price_input = input("What is the new price? (Press Enter for default): ")
            new_quantity_input = input("What is the new quantity? (Press Enter for default): ")
 
            try:
                # if we have no input from user, use the default
                new_description = new_description if new_description else "none"
                new_price = float(new_price_input) if new_price_input else 0.0
                new_quantity = int(new_quantity_input) if new_quantity_input else 0
                
                # this creates the item
                modified_item = ItemToPurchase(item_name, new_price, new_quantity, new_description)
    
                # pass to cart and call modify
                cart.modify_item(modified_item)
            except ValueError:
                print("Invalid input for price or quantity.")
            
        elif choice == 'i':
            # calls function from above
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            # calls function from above
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            # this breaks the while loop.
            break

        else:
            # note that this implies that it starts at the top of the 
            # while loop again.
            print("Bad option! Please try again.")

if __name__ == "__main__":
    # get name and date
    customer_name = input("What is your name? ")
    current_date = input("What is the date? (For example, 'January 1, 2020' is the default.) ")
    # instantiate the shopping cart
    shopping_cart = ShoppingCart(customer_name, current_date)
    # print the menu
    print_menu(shopping_cart)
