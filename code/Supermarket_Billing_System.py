import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Dictionary storing product names and prices
products = {
    "Rice": 60,
    "Wheat": 40,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 35,
    "Butter": 55,
    "Tea": 120,
    "Oil": 150,
    "Biscuits": 20,
    "Soap": 35
}

# List storing purchased items
cart = []


def add_product():
    name = product_var.get()
    quantity = quantity_var.get()

    if not name:
        messagebox.showerror("Error", "Please select a product.")
        return

    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive quantity.")
        return

    price = products[name]
    amount = price * quantity

    # Store each purchase as a dictionary in the list
    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "amount": amount
    })

    bill_table.insert(
        "", tk.END,
        values=(name, price, quantity, amount)
    )

    update_total()
    quantity_var.set("1")


def update_total():
    total = sum(item["amount"] for item in cart)
    total_label.config(text=f"Total: ₹{total:.2f}")


def generate_bill():
    if not cart:
        messagebox.showwarning("Warning", "Please add products first.")
        return

    total = sum(item["amount"] for item in cart)
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    bill = []
    bill.append("=" * 40)
    bill.append("       SUPERMARKET BILL")
    bill.append("=" * 40)
    bill.append(f"Date: {date_time}")
    bill.append("-" * 40)
    bill.append(
        f"{'Product':<12}{'Price':>7}{'Qty':>5}{'Amount':>10}"
    )
    bill.append("-" * 40)

    for item in cart:
        bill.append(
            f"{item['name']:<12}"
            f"{item['price']:>7}"
            f"{item['quantity']:>5}"
            f"{item['amount']:>10}"
        )

    bill.append("-" * 40)
    bill.append(f"TOTAL: ₹{total:.2f}")
    bill.append("=" * 40)
    bill.append("Thank you for shopping!")

    bill_text = "\n".join(bill)

    # Display the generated bill
    bill_window = tk.Toplevel(root)
    bill_window.title("Generated Bill")
    bill_window.geometry("430x450")

    text_area = tk.Text(bill_window, font=("Courier New", 11))
    text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    text_area.insert(tk.END, bill_text)
    text_area.config(state=tk.DISABLED)

    # File handling: save bill to a text file
    try:
        with open("supermarket_bills.txt", "a", encoding="utf-8") as file:
            file.write(bill_text + "\n\n")

        messagebox.showinfo(
            "Success",
            "Bill generated and saved to supermarket_bills.txt"
        )
    except OSError as error:
        messagebox.showerror("File Error", str(error))


def clear_cart():
    cart.clear()

    for row in bill_table.get_children():
        bill_table.delete(row)

    update_total()


# Main GUI window
root = tk.Tk()
root.title("Supermarket Billing System")
root.geometry("700x520")
root.resizable(False, False)

title = tk.Label(
    root,
    text="SUPERMARKET BILLING SYSTEM",
    font=("Arial", 18, "bold"),
    bg="navy",
    fg="white",
    pady=15
)
title.pack(fill=tk.X)

# Product selection area
input_frame = tk.Frame(root, pady=15)
input_frame.pack()

tk.Label(input_frame, text="Product:").grid(
    row=0, column=0, padx=5, pady=5
)

product_var = tk.StringVar()
product_box = ttk.Combobox(
    input_frame,
    textvariable=product_var,
    values=list(products.keys()),
    state="readonly",
    width=18
)
product_box.grid(row=0, column=1, padx=5)
product_box.current(0)

tk.Label(input_frame, text="Quantity:").grid(
    row=0, column=2, padx=5
)

quantity_var = tk.StringVar(value="1")
quantity_entry = tk.Entry(
    input_frame, textvariable=quantity_var, width=8
)
quantity_entry.grid(row=0, column=3, padx=5)

tk.Button(
    input_frame,
    text="Add Product",
    command=add_product,
    bg="green",
    fg="white"
).grid(row=0, column=4, padx=8)

# Table displaying purchased products
columns = ("Product", "Price (₹)", "Quantity", "Amount (₹)")

bill_table = ttk.Treeview(
    root, columns=columns, show="headings", height=12
)

for column in columns:
    bill_table.heading(column, text=column)
    bill_table.column(column, width=155, anchor=tk.CENTER)

bill_table.pack(padx=15, pady=10)

# Total amount
total_label = tk.Label(
    root,
    text="Total: ₹0.00",
    font=("Arial", 15, "bold"),
    fg="darkgreen"
)
total_label.pack(pady=8)

# Action buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Generate Bill",
    command=generate_bill,
    bg="blue",
    fg="white",
    width=15
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Clear Cart",
    command=clear_cart,
    bg="orange",
    width=15
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    width=15
).grid(row=0, column=2, padx=10)

root.mainloop()
