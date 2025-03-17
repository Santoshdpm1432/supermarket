
name = input("Enter your name: ")
print(f"Welcome, {name}, to Santosh Super Market!")

# Store items and prices
items = {
    "apple": 20,
    "rice": 30,
    "wheat": 20,
    "cheese": 50,
    "chicken": 25,
}

# User's cart
cart = {}
total_cost = 0

while True:
    print("Available items in the supermarket:")
    for item, price in items.items():
        print(f"{item.capitalize()}: {price}")

    # Taking user input for item selection
    choice = input("Enter the item name to add to cart (or type 'checkout' to finish shopping): ").lower()

    if choice == "checkout":
        break  # Exit the shopping loop
    if choice in items:
        try:
            qty = int(input(f"How many {choice}(s) do you want? "))
            if qty > 0:
                cart[choice] = cart.get(choice, 0) + qty
                total_cost += items[choice] * qty
                print(f" {qty} {choice}(s) added to your cart.")
            else:
                print(" Please enter a valid quantity.")
        except ValueError:
            print(" Invalid input. Please enter a numeric value for quantity.")
    else:
        print(" Invalid item, please choose from the list.")

# Final bill
print("=========Shopping Summary==========")

print("=====================================")
if cart:
    for item, qty in cart.items():
        print(f"{item.capitalize()}: {qty} x {items[item]} = {qty * items[item]}")
    print(f"Total Amount: {total_cost}")
    print(f"Thank you for shopping with us, {name}! Have a great day!")
else:
    print("Your cart is empty. Visit again!")

