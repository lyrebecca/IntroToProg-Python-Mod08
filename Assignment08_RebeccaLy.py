# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# RebeccaLy,08-26-2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        RebeccaLy,08-26-2020,Modified code to complete assignment 8
    """

    # Creates a constructor and initializes product_name and product_price as variables
    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

    # Creates a string representation using product_name and product_price
    def __str__(self):
        return self.product_name + ", " + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <RebeccaLy>,<08-26-2020>,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name): # Uses the file as a parameter
        product_list = []  # clear current data
        file = open(file_name, "r")  # opens the file in read mode
        for line in file: # Iterates through each line in the file
            name, price = line.split(",") # Splits by a comma
            product = Product(name.strip(), float(price.strip())) # Strips variables of any extra spaces
            product_list.append(product) # Appends variable to list in memory
        file.close()  # closes the file
        return product_list # Returns product list in memory

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects): # Takes in file name and list in memory
        file = open(file_name, "w") # Opens file with write method
        for product in list_of_product_objects: # Overwrites file with contents in memory
            file.write(str(product) + "\n") # Creates a new line for each row
        file.close() # Closes the file


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Displays menu, obtains user input and reads from the file:

    methods:
        display_menu()
        user_menu_choice()
        show_current_data(list_of_products)
        user_product_input()

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <RebeccaLy>,<08-26-2020>,Modified code to complete assignment 8
    """
    pass
    @staticmethod
    def display_menu(): # Displays menu to user
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current product list
        2) Add products to list
        3) Save and Exit Program
        ''')
        print()  # Add an extra line for looks

    # Asks user to pick a menu option and returns a string
    @staticmethod
    def user_menu_choice():
        """ Gets the menu choice from a user

                :return: string
                """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # Displays current data stored in memory
    @staticmethod
    def show_current_data(list_of_products):
        for row in list_of_products: # Iterates through each row
            print(row)

    # Gets the product input from the user and stores into a variable
    @staticmethod
    def user_product_input():
        product_name = input("Enter a product name: ")
        product_price = input("Enter a product price: ")
        product = Product(product_name, product_price)
        return product


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)


# Show user a menu of options
while(True):
    IO.display_menu()
# Get user's menu option choice

    option = IO.user_menu_choice()
    # Show user current data in the list of product objects
    if option == '1':
        IO.show_current_data(lstOfProductObjects)
    # Let user add data to the list of product objects
    elif option == '2':
        product = IO.user_product_input()
        lstOfProductObjects.append(product)

    # let user save current data to file and exit program
    elif option == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        exit(0)

# Main Body of Script  ---------------------------------------------------- #

