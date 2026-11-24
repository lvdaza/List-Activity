
orders = []
for i in range(1, 6):
    item = input(f"Enter Order {i}: ").strip().title()
    orders.append(item)

print("\nOriginal Orders:", orders)

additional_order = input("\nEnter additional order: ").strip().title()
orders.append(additional_order)
print("Updated Orders:", orders)

priority_order = input("\nEnter priority order: ").strip().title()
orders.insert(0, priority_order)
print("Updated Orders:", orders)

search_item = input("\nSearch for an order: ").strip().title()
if search_item in orders:
    print(f"Number of Occurrences: {orders.count(search_item)}")
    print(f"First Index: {orders.index(search_item)}")
else:
    print("Order not found.")

cancel_item = input("\nEnter order to cancel: ").strip().title()
if cancel_item in orders:
    orders.remove(cancel_item)
    print(f"'{cancel_item}' canceled.")
else:
    print("Order not found; nothing removed.")
print("Updated Orders:", orders)

if orders:
    removed_last = orders.pop()
    print(f"\nLast Order Removed: {removed_last}")

orders.sort()

print("\n===== FINAL ORDER REPORT =====")
print(f"Orders: {orders}")
print(f"Total Remaining Orders: {len(orders)}")

