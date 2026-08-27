# Project: Online Shopping Cart System

A procedural, function-based shopping cart system demonstrating modular logic and basic data structures.

## 1. Problem Statement
A retail store needs a python-based online shopping cart system. The system should allow users to perform basic operations: view available products, add products to a cart, modify item quantities, remove products, apply compound discounts (percentage coupon and a flat discount), calculate subtotal, calculate category-specific GST, and calculate the final total bill with a printed ASCII invoice.

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: Clean, decoupled functions for cart manipulation (`add_product`, `remove_product`, `change_quantity`).
* **Computational Logic**: Functions for calculations (`calculate_subtotal`, `calculate_discount`, `calculate_gst`, and `print_receipt`).
* **Data Store & Input Setup**: Defines product inventory maps and category-specific GST tax rates.
* **Driver Logic (Main)**: An interactive console menu loop that drives the shopping operations.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **Inventory Catalog**: Mapping of product ID to name, unit price, and category.
- **Cart Data**: Mapping of product ID to quantity.
- **Discounts**: Global percent and flat discount variables.
- **GST Rates**: Category-specific GST rate percentages.

### No Needs (Irrelevant Information)
- Physical store shelf layouts, billing counter designs, checkout lines.
- Specific credit/debit card numbers or bank clearance API.
- Customer profiles, names, email addresses, or history.

## 4. Algorithm
1. Initialize cart dictionary, inventory catalog dictionary, and category GST rate dictionary.
2. Accept choice input (1-8):
   - Option 1 (View Products): Print inventory list.
   - Option 2 (View Cart): Print current cart items.
   - Option 3 (Add Product): Validate quantity $>0$ and add to cart.
   - Option 4 (Change Quantity): Validate quantity $>0$ and change cart value.
   - Option 5 (Remove Product): Remove key from cart dictionary.
   - Option 6 (Apply Discount): Update percent and flat discount values.
   - Option 7 (Print Receipt): Compute subtotal, deduct discount, calculate itemized post-discount GST, and print receipt.
   - Option 8 (Exit): Terminate program.

## 5. Core Logic
```python
def add_product(cart, product_id, quantity):
    if quantity <= 0:
        raise ValueError()
    cart[product_id] = cart.get(product_id, 0) + quantity

def remove_product(cart, product_id):
    if product_id not in cart:
        raise KeyError()
    del cart[product_id]

def change_quantity(cart, product_id, quantity):
    if product_id not in cart:
        raise KeyError()
    if quantity <= 0:
        raise ValueError()
    cart[product_id] = quantity

def calculate_subtotal(cart, inventory):
    subtotal = 0.0
    for pid, qty in cart.items():
        subtotal += inventory[pid]["price"] * qty
    return subtotal

def calculate_discount(subtotal, discount_percent, discount_flat):
    pct_disc = subtotal * (discount_percent / 100.0)
    total_disc = pct_disc + discount_flat
    return min(total_disc, subtotal)

def calculate_gst(cart, inventory, discount_ratio, gst_rates, default_rate=0.18):
    total_gst = 0.0
    for pid, qty in cart.items():
        item_sub = inventory[pid]["price"] * qty
        item_disc = item_sub * discount_ratio
        category = inventory[pid]["category"]
        rate = gst_rates.get(category, default_rate)
        total_gst += item_disc * rate
    return total_gst

def print_receipt(cart, inventory, discount_percent, discount_flat, gst_rates, default_rate=0.18):
    subtotal = calculate_subtotal(cart, inventory)
    disc_val = calculate_discount(subtotal, discount_percent, discount_flat)
    discount_ratio = (subtotal - disc_val) / subtotal if subtotal > 0 else 0.0
    gst_val = calculate_gst(cart, inventory, discount_ratio, gst_rates, default_rate)
    grand_total = subtotal - disc_val + gst_val
    
    print("=" * 75)
    print("                   ONLINE SHOPPING CART INVOICE                    ")
    print("=" * 75)
    print(f"{'ID':<6} {'Product Name':<20} {'Qty':<4} {'Price':<8} {'Subtotal':<10} {'GST':<8} {'Total':<10}")
    print("-" * 75)
    
    for pid, qty in cart.items():
        price = inventory[pid]["price"]
        item_sub = price * qty
        item_net = item_sub * discount_ratio
        rate = gst_rates.get(inventory[pid]["category"], default_rate)
        item_gst = item_net * rate
        item_tot = item_net + item_gst
        name = inventory[pid]["name"]
        print(f"{pid:<6} {name:<20} {qty:<4} ${price:<7.2f} ${item_sub:<9.2f} ${item_gst:<7.2f} ${item_tot:<9.2f}")
        
    print("-" * 75)
    print(f"{'Subtotal:':<63} ${subtotal:.2f}")
    if disc_val > 0:
        disc_label = f"Discount ({discount_percent}% off + ${discount_flat:.2f} flat):"
        print(f"{disc_label:<63} -${disc_val:.2f}")
    print(f"{'GST Total:':<63} ${gst_val:.2f}")
    print("-" * 75)
    print(f"{'GRAND TOTAL:':<63} ${grand_total:.2f}")
    print("=" * 75)
    print("                 Thank you for shopping with us!                 ")
    print("=" * 75)
```

## 6. Data Store & Input Setup
```python
inventory = {
    "P001": {"name": "Laptop", "price": 1200.00, "category": "Electronics"},
    "P002": {"name": "Headphones", "price": 150.00, "category": "Electronics"},
    "P003": {"name": "Winter Jacket", "price": 80.00, "category": "Clothing"},
    "P004": {"name": "Algorithmic Book", "price": 45.00, "category": "Books"},
    "P005": {"name": "Organic Apples", "price": 12.00, "category": "Groceries"}
}

gst_rates = {
    "Electronics": 0.18,
    "Clothing": 0.12,
    "Groceries": 0.05,
    "Books": 0.00
}

cart = {}
discount_percent = 10.0
discount_flat = 15.0
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Add and Modify
* **Input**: Add Laptop (qty 1), Headphones (qty 2), change Headphones qty to 1.
* **Expected Output**: Cart contains Laptop (qty 1) and Headphones (qty 1).

### Test Case 2: Product Removal
* **Input**: Remove Headphones from cart.
* **Expected Output**: Cart contains only Laptop.

### Test Case 3: Invalid Quantity Bound
* **Input**: Attempt to set quantity to 0 or negative.
* **Expected Output**: Raises `ValueError` exception.

### Test Case 4: Category-Wise GST Calculation
* **Input**: Laptop ($1200, Electronics at 18%).
* **Expected Output**: GST calculation produces $216.00.

### Test Case 5: Discount Overflow Cap
* **Input**: Subtotal $100, Discount $150.
* **Expected Output**: Calculated discount value capped at $100.

## 8. Driver Logic (Main)
To run the driver logic, open the [ShoppingCart.ipynb](ShoppingCart.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Dynamic Input Output (Sample Run)
```text
--- ONLINE SHOPPING MENU ---
1. View Products
2. View Cart
3. Add Product
4. Change Quantity
5. Remove Product
6. Apply Discount
7. Print Receipt
8. Exit
Enter choice (1-8): 7
===========================================================================
                   ONLINE SHOPPING CART INVOICE                    
===========================================================================
ID     Product Name         Qty  Price    Subtotal   GST      Total     
---------------------------------------------------------------------------
P001   Laptop               1    $1200.00 $1200.00   $192.10  $1259.34  
P002   Headphones           1    $150.00  $150.00    $24.01   $157.42   
P005   Organic Apples       5    $12.00   $60.00     $2.67    $56.03    
---------------------------------------------------------------------------
Subtotal:                                                       $1410.00
Discount (10.0% off + $15.00 flat):                             -$156.00
GST Total:                                                      $218.78
---------------------------------------------------------------------------
GRAND TOTAL:                                                    $1472.78
===========================================================================
                 Thank you for shopping with us!                 
===========================================================================
```
