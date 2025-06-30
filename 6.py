items = ["Milk", "Bread", "Eggs"]
prices = [30, 40, 10]
quantities = [2, 1, 12]
discount_rate = 10
tax_rate = 5
print("Itemized Receipt".center(40, "-"))
print(f"{'Item':<10}{'Qty':>5}{'Price':>10}{'Total':>10}")
print("-" * 40)
subtotal = 0
for item, qty, price in zip(items, quantities, prices):
    total = qty * price
    subtotal += total
    print(f"{item:<10}{qty:>5}{price:>10}{total:>10}")
discount = (discount_rate / 100) * subtotal
tax = (tax_rate / 100) * (subtotal - discount)
total_cost = subtotal - discount + tax
print("-" * 40)
print(f"{'Subtotal':<25}₹{subtotal:>10.2f}")
print(f"{'Discount (@'+str(discount_rate)+'%)':<25}-₹{discount:>9.2f}")
print(f"{'Tax (@'+str(tax_rate)+'%)':<25}+₹{tax:>9.2f}")
print(f"{'Total Cost':<25}₹{total_cost:>10.2f}")
print("-" * 40)