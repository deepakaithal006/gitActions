def calculate_total(subtotal):
    """Calculate the final bill with discount and GST."""

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    # Apply 10% discount if subtotal is above ₹300
    if subtotal > 300:
        subtotal = subtotal * 0.90

    # Add 5% GST to the discounted amount
    total = subtotal * 1.05

    return round(total, 2)


# Example usage
print(calculate_total(200))  # 210.0
print(calculate_total(400))  # 378.0