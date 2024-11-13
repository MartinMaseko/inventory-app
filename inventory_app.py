#========The beginning of the class==========

class Shoe:
    
    """Shoe class is used to define objects and print the 
    objects attributes"""

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        
    def get_cost(self):
        
        """Prints the cost of the defined object"""

        print(f"The cost of the shoes: {self.cost}")


    def get_quantity(self):
        
        """Prints the quantity of the defined object"""

        print(f"Quantity of shoes: {self.quantity}")


    def __str__(self):
        
        """Prints the attributes of the defined object"""

        return (
            "        [Product Data]        \n"
            f"Country: {self.country}\n"
            f"Code: {self.code}\n"
            f"Product: {self.product}\n"
            f"Cost: {self.cost}\n"
            f"Quantity: {self.quantity}\n"
        )                                                                


#=============Shoe list===========
# Empty list shoe_list will be used to append objects.

shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with  
    this data and append this object into the shoes list. 
    One line in this file represents data to create one object 
    of shoes.skip the first line using code.
    '''
    
    # A with open() function is used to read the inventory text file 
    # function. 
    # The next() function is used to skip the first line of headings.
    # A for loop is called to strip() and split() to 
    # initialise variables that will be used as parameters to 
    # instantiate a Shoe class object.
    # The object is then appended into the shoe_list.

    with open('inventory.txt', 'r+') as inventory_txt:
        next(inventory_txt)
        for line in inventory_txt:
            inv_data = line.strip()
            inv_data = inv_data.split(",")
            country, code, product, cost, quantity = inv_data
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)




def capture_shoes():

    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    
    # Create Variables that take user inputs.
    # The variables are passed as parameters for instatiating 
    # an object.
    # The new object is appended into the shoe_list.
    
    country = input("Enter the Country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")
    with open('inventory.txt',"a+", encoding="utf-8" ) as inventorytxt_file:
        inventorytxt_file.write(
            f"\n{country},{code},{product},{cost},{quantity}"
        )
    captured_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(captured_shoe)


def view_all():

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    
    # A for loop is used to print each object as a string using the 
    # str() function within the shoe_list.
	
    [print(str(obj)) for obj in shoe_list]



# Empty list to store int elements from the shoe_list object values.

attr_list  = []


def restock():
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. 
    Ask the user if they want to add this quantity of shoes 
    and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    
    # For loop is used to append each objects quantity into attr_list.
    # The min() function is used to find the smallest value.(min_qty)
    
    for obj in shoe_list:
        attr_list.append(int(obj.quantity))
    
    min_qty = str(min(attr_list))
    
    # Another for loop is used to find the object that has a matching 
    # value in the object list. 
    # The object is then diplayed with a user prompt to restock item.
    # A if statement together with a try-except block is used to handle 
    # user input errors.
    # The object value is then changed into an addition of the previous 
    # stock quantity and the restock quantity.
    # The changes are then written back into the text file.

    for obj in shoe_list:
        
        if obj.quantity == min_qty:
            print("Stock with the lowest quantity:\n",obj)
            
            add_stock = input("Would you like to add stock (Yes/No): ").lower() 
            
            if add_stock == "yes":
                
                try:
                    restock_quantity = int(input(
                        "Enter the quantity you would like to add: "
                        ))
                    current_total = int(obj.quantity)
                    restock_value = current_total + restock_quantity
                    obj.quantity = str(restock_value)
                    print(obj)
                    
                    with open('inventory.txt', 'w+') as file:
                        file.write("Country,Code,Product,Cost,Quantity")
                        for obj in shoe_list:
                            file.write(
								f"\n{obj.country},{obj.code},{obj.product}"
        f",{obj.cost},{obj.quantity}"
							)
                            
                except ValueError:
                    
                    print("Invalid input!, Enter a number.")
                    restock()
                    
            elif add_stock == "No":
                exit()
                
            else:
            	print("Invalid Input")
                
                  
def search_shoe():

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so 
     that it will be printed.
    '''
    
    # Ask user for product code in product_search.
    # use a for loop and if statement to find the 
    # value match to the variable.
    
    product_search = input("Enter the product code: ")
    search = [shoe for shoe in shoe_list if shoe.code == product_search]
    [print(str(obj)) for obj in search]


def value_per_item():
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: 
    value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    
    # A for loop is used to retrieve the attributes 
    # of cost and quantity, then
    # cast them into integers for multiplication.
    
    for shoe in shoe_list:
        shoe.cost = int(shoe.cost)
        shoe.quantity = int(shoe.quantity)
        value = shoe.cost * shoe.quantity
        print("Product:", shoe.product, "// Total Value:", value)


# Empty list to store integer values of each products quantity.

shoe_qty = []

def highest_qty():

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    
    # Two separate for loop are used here.
    # One for loop retrieves the quantity of each shoe and 
    # stores them in 
    # the shoe_qty list.
    # A variable is created to store the max() from the list
    # The second for loop finds the object with a 
    # matching object attribute 
    # and print the objects attributes for the user know 
    # which product has the highest quantity with 
    # its corresponding details.
    
    for shoe in shoe_list:
        shoe_qty.append(int(shoe.quantity))
        highest_num = max(shoe_qty)

    for shoe in shoe_list:   
        if int(shoe.quantity) == highest_num:
            print(
                f"{shoe.product} has the highest quantity in stock\n"
                f"Quanity: {shoe.quantity}\n"
                f"Country: {shoe.country}\n"
                f"{shoe.product} is now on sale!\n"
            )
            break


#==========Main Menu=============

def app_menu():
    
    # Create UDF function app_menu to display menu options 
    # and call functions.
    # The while fuunction is used to handle input errors.
    # If-elif-else statements are used to call functions 
    # based on the user selection.

    while True:
        print(
            "Nike Inventory Application\n"
            "\nEnter the number of the function you would like to use!\n"
            "1. Read Inventory File.\n"
            "2. Capture New Stock.\n"
            "3. View all stock.\n"
            "4. Restock.\n"
            "5. Search Product.\n"
            "6. Display Value of Products.\n"
            "7. Display Highest Quantity Product.\n"
            "8. Exit application."
        )

        user_input = input("Enter the number of the function: ")

        if user_input == "1":
            read_shoes_data()

        elif user_input == "2":
            capture_shoes()

        elif user_input == "3":
            read_shoes_data()
            view_all()

        elif user_input == "4":
            read_shoes_data()
            restock()

        elif user_input == "5":
            read_shoes_data()
            search_shoe()

        elif user_input == "6":
            read_shoes_data()
            value_per_item()

        elif user_input == "7":
            read_shoes_data()
            highest_qty()

        elif user_input == "8":
            exit()

        else:
            print("\nInvalid Input. Enter a number!\n")
            app_menu()

app_menu()    