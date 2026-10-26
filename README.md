
# Supermarket Billing System

## 1. Project Overview

The Supermarket Billing System is a GUI-based application developed using Python. It helps users manage supermarket purchases by selecting products, entering quantities, calculating the total bill, and saving generated bills to a text file.

The project demonstrates the practical implementation of Lists, Dictionaries, File Handling, Functions, Exception Handling, and GUI programming using Tkinter.

## 2. Objectives

- Develop a simple and user-friendly billing application.
- Display available products and their prices.
- Allow users to select products and specify quantities.
- Calculate individual product amounts and the total bill.
- Generate and display a formatted bill.
- Save billing records in a text file.
- Demonstrate fundamental Python programming concepts.

## 3. Features

- **Product Selection:** Select products from a dropdown menu.
- **Quantity Input:** Enter the quantity of each product.
- **Automatic Calculation:** Calculate the amount using price multiplied by quantity.
- **Shopping Cart:** Display purchased products in a table.
- **Bill Generation:** Generate a formatted bill with the date and time.
- **File Storage:** Save bills in `supermarket_bills.txt`.
- **Clear Cart:** Remove all current purchases from the cart.
- **Input Validation:** Prevent invalid or non-positive quantities.
- **Error Handling:** Display appropriate error messages for invalid inputs and file errors.
- **Graphical Interface:** Use Tkinter widgets for user interaction.

## 4. Technologies Used

- **Programming Language:** Python 3
- **GUI Library:** Tkinter
- **Table Widget:** ttk.Treeview
- **Data Structures:** Lists and Dictionaries
- **File Handling:** Text files using `open()`
- **Date and Time:** datetime module
- **Exception Handling:** try-except statements

## 5. Project Structure

```text
Supermarket-Billing-System/
│
├── Supermarket_Billing_System.py
├── README.md
└── supermarket_bills.txt
```

Note: `supermarket_bills.txt` is created automatically when a bill is generated. It may not exist before the first bill is saved.

## 6. Installation and Requirements

### Requirements

- Python 3.10 or later recommended
- Tkinter support
- A code editor such as VS Code, IDLE, or PyCharm

No external Python packages are required. Tkinter is generally included with standard Python installations.

### Installation Steps

1. Install Python from https://www.python.org/downloads/ if it is not already installed.
2. Save the source code as `Supermarket_Billing_System.py`.
3. Open a terminal or command prompt in the project directory.
4. Execute the following command:

```bash
python Supermarket_Billing_System.py
```

On some Windows systems, use:

```bash
py Supermarket_Billing_System.py
```

## 7. How to Use the Application

1. Run the Python program.
2. Select a product from the dropdown menu.
3. Enter the desired quantity.
4. Click **Add Product** to add the item to the billing table.
5. Repeat the process to add more products.
6. Check the displayed total amount.
7. Click **Generate Bill** to view the formatted bill.
8. The generated bill is appended to `supermarket_bills.txt`.
9. Click **Clear Cart** to start a new purchase.
10. Click **Exit** to close the application.

## 8. Product Catalogue

The application contains the following sample products and prices:

| Product | Price |
|---|---:|
| Rice | ₹60 |
| Wheat | ₹40 |
| Sugar | ₹45 |
| Milk | ₹30 |
| Bread | ₹35 |
| Butter | ₹55 |
| Tea | ₹120 |
| Oil | ₹150 |
| Biscuits | ₹20 |
| Soap | ₹35 |

Prices are sample values and can be modified in the `products` dictionary.

## 9. Python Concepts Implemented

### Lists
The `cart` list stores all purchased items. Each item is represented by a dictionary.

### Dictionaries
The `products` dictionary maps product names to their prices. Individual cart dictionaries store product names, prices, quantities, and amounts.

### File Handling
The `open()` function with append mode (`"a"`) stores generated bills in a text file without overwriting previous records.

### GUI Programming
Tkinter provides the main window, labels, buttons, entry fields, dropdown menu, and billing table.

### Functions
Separate functions organize the program into manageable tasks, such as adding products, updating totals, generating bills, and clearing the cart.

### Exception Handling
`try-except` statements handle invalid quantities and file-related errors.

### Loops and Comprehensions
Loops display cart items and clear table rows. List comprehensions and generator expressions help retrieve product names and calculate totals.

### Date and Time
The `datetime` module records the date and time when a bill is generated.

## 10. Billing Formula

The amount for each product is calculated as:

```text
Amount = Price × Quantity
```

The total bill is calculated as:

```text
Total Bill = Sum of Amounts of All Purchased Items
```

Example:

| Product | Price | Quantity | Amount |
|---|---:|---:|---:|
| Rice | ₹60 | 2 | ₹120 |
| Milk | ₹30 | 3 | ₹90 |
| Bread | ₹35 | 1 | ₹35 |
| **Total** | | | **₹245** |

## 11. File Handling Details

The application stores bills in `supermarket_bills.txt`.

- File mode `"a"` appends new bills to existing records.
- `encoding="utf-8"` supports text encoding, including the rupee symbol.
- Each bill contains the date and time, product details, quantities, amounts, and total.
- Previous bills remain in the file when new bills are generated.

The text file acts as a simple local billing record. It is not a database.

## 12. Testing

The following test cases can be used to verify the application's behaviour.

| Test Case | Input or Action | Expected Result |
|---|---|---|
| TC01 | Add Rice, quantity 2 | Amount displayed as ₹120 |
| TC02 | Add Milk, quantity 3 | Amount displayed as ₹90 |
| TC03 | Add multiple products | Total is calculated correctly |
| TC04 | Enter quantity 0 | Validation error is displayed |
| TC05 | Enter a negative quantity | Validation error is displayed |
| TC06 | Enter text instead of a quantity | Validation error is displayed |
| TC07 | Generate a bill with an empty cart | Warning message is displayed |
| TC08 | Generate a bill with products | Bill window opens and the bill is saved |
| TC09 | Generate multiple bills | New bills are appended to the file |
| TC10 | Click Clear Cart | Cart and table are cleared; total becomes ₹0 |
| TC11 | Click Exit | Application closes |

## 13. Limitations

- Product prices are predefined in the source code.
- The application does not maintain inventory or update stock quantities.
- There is no customer login or administrator authentication.
- Bills are stored in a plain text file rather than a database.
- Tax, discounts, and payment gateway integration are not implemented.
- The application is designed for a single local user.

## 14. Future Enhancements

- Add, update, and delete products through the GUI.
- Introduce stock and inventory management.
- Add discounts, GST calculations, and payment methods.
- Generate printable PDF invoices.
- Store product and billing records in SQLite or MySQL.
- Add customer details and unique invoice numbers.
- Provide daily, weekly, and monthly sales reports.
- Introduce user authentication and administrator controls.

## 15. Learning Outcomes

Through this project, the developer gains practical experience in:

- Using lists and dictionaries to organize data.
- Developing desktop applications with Tkinter.
- Performing file operations in Python.
- Validating user input and handling exceptions.
- Applying functions and loops to solve a real-world problem.
- Calculating totals and formatting billing records.
- Organizing a small Python project for execution and documentation.

## 16. Conclusion

The Supermarket Billing System demonstrates how basic Python programming concepts can be combined to create a practical billing application. It provides product selection, quantity management, automatic bill calculation, graphical interaction, and persistent text-file storage. The project can be extended with inventory management, database integration, taxation, and reporting features to make it more suitable for real-world supermarket operations.

## 17. Author

**Project Name:** Supermarket Billing System  
**Language:** Python  
**Interface:** Tkinter GUI  
**Project Type:** Academic Mini Project
