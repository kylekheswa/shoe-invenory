# Shoe Inventory Management System

This Python program implements a simple Shoe Inventory Management System. The system allows users to perform various operations related to managing a list of shoe items, such as capturing new shoe data, viewing all shoes, restocking items, searching for a shoe by code, calculating the value per item, and finding the shoe with the highest quantity in inventory.

## Class Definition

The program defines a `Shoe` class with the following attributes:

- `country`: Country of origin
- `code`: Shoe code
- `product`: Product name
- `cost`: Cost of the shoe
- `quantity`: Quantity of the shoe

Additionally, several utility functions are provided to interact with the shoe data:

- `get_cost()`: Returns the cost of the shoe.
- `get_quantity()`: Returns the quantity of the shoe.
- `__str__()`: Returns a string representation of the shoe.

## Functionality

1. **Read Shoes Data**: Reads shoe data from the 'inventory.txt' file and populates the `shoe_list`.

2. **Capture Shoes**: Captures shoe data from user input, adds it to the `shoe_list`, and updates the 'inventory.txt' file.

3. **View All Shoes**: Displays details of all shoes in the `shoe_list`.

4. **Re-stock Shoes**: Restocks shoes with the lowest quantity and updates the 'inventory.txt' file.

5. **Search Shoe**: Searches for a shoe by code and displays its details.

6. **Calculate Value per Item**: Calculates and displays the value of each shoe item.

7. **Find Shoe with Highest Quantity**: Finds and displays the shoe with the highest quantity in inventory.

8. **Exit**: Exits the program.

## Usage

1. Run the program.
2. Select options from the main menu by entering the corresponding numbers.
3. Follow the prompts to perform various operations.

## File Handling

The program reads and updates shoe data from/to the 'inventory.txt' file. The file should have a CSV format with the header "Country,Code,Product,Cost,Quantity".

## Dependencies

- Python 3.x

## How to Run

1. Make sure you have Python installed on your system.
2. Save the program in a file with a ".py" extension (e.g., `shoe_inventory.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the program is saved.
5. Run the program using the command: `python shoe_inventory.py`.

Enjoy managing your shoe inventory with this simple system!
