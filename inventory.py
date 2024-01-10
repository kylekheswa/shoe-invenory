# Class definition
class Shoe:
    """
    Represents a shoe item with country of origin, code, product name, cost, and quantity.
    """
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Return a string representation of the shoe."""
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# List to store shoe objects
shoe_list = []

# Functions outside the class
def read_shoes_data():
    """
    Read shoe data from the 'inventory.txt' file and populate the shoe_list.
    """
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]  # Skip the first line
            for line in lines:
                data = line.strip().split(",")
                country, code, product, cost, quantity = data
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def update_inventory_file():
    """
    Update the 'inventory.txt' file with the data from the shoe_list.
    """
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Inventory file updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating the inventory file: {e}")

def capture_shoes():
    """
    Capture shoe data from user input and add it to the shoe_list. Also, update the 'inventory.txt' file.
    """
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe data captured successfully.")

    # Update the text file with the new shoe data
    update_inventory_file()

def view_all():
    """
    Display details of all shoes in the shoe_list.
    """
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    """
    Restock shoes with the lowest quantity and update the 'inventory.txt' file.
    """
    lowest_quantity = float('inf')
    shoe_to_restock = None

    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity:
            lowest_quantity = shoe.get_quantity()
            shoe_to_restock = shoe

    if shoe_to_restock:
        print(f"The shoe with code {shoe_to_restock.code} needs to be restocked.")
        restock_quantity = int(input("Enter the quantity to restock: "))
        shoe_to_restock.quantity += restock_quantity
        print(f"Restocked {restock_quantity} units.")

        # Update the text file with the new quantity
        update_inventory_file()

    else:
        print("No shoes in inventory.")

def seach_shoe():
    """
    Search for a shoe by code and display its details.
    """
    code_to_search = input("Enter the code of the shoe you want to search: ")
    found = False
    for shoe in shoe_list:
        if shoe.code == code_to_search:
            print("Found the following shoe:")
            print(shoe)
            found = True
            break
    if not found:
        print(f"No shoe with code {code_to_search} found.")

def value_per_item():
    """
    Calculate and display the value of each shoe item.
    """
    print("\nValue per Item:")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Value: {value}")

def highest_qty():
    """
    Find and display the shoe with the highest quantity in inventory.
    """
    max_quantity = -1
    max_quantity_shoe = None
    for shoe in shoe_list:
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            max_quantity_shoe = shoe
    if max_quantity_shoe:
        print(f"The shoe with the highest quantity is {max_quantity_shoe.product} with {max_quantity} units.")
    else:
        print("No shoes in inventory.")

# Main Menu
while True:
    print("\n===== Main Menu =====")
    print("1. Read Shoes Data")
    print("2. Capture Shoes")
    print("3. View All Shoes")
    print("4. Re-stock Shoes")
    print("5. Search Shoe")
    print("6. Calculate Value per Item")
    print("7. Find Shoe with Highest Quantity")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        seach_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
