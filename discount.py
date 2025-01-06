def calculate_total(cart):
    """
    Calculate the total price of items in the cart.
    Apply a 10% discount if more than 5 items.
    10% discount if total value is between 20k and 50k.
    15% discount if total value is more than 50k.
    """
    total = sum(cart.values())
    if len(cart)>5:
        if total > 20000 and total < 50000:
            total *= 0.9
        elif total > 50000:
            total *= 0.85
    return total
cart = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 35000, 'Keyboard': 1500, 'Monitor': 800, 'USB Drive':1000}
print(f"Cart items: {cart}")
print(f"Total price: {calculate_total(cart)}")