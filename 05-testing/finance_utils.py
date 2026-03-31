def convert_currency(amount, rate):
    """Converts an amount from one currency to another using a given rate."""
    if amount < 0 or rate <= 0:
        return None
    return round(amount * rate, 2)

def calculate_tax(price, tax_rate):
    """Calculates the tax for a given price and tax rate."""
    if price < 0 or tax_rate < 0:
        return None
    return round(price * (tax_rate / 100), 2)

def calculate_total(price, tax_rate, discount=0):
    """Calculates the total price after tax and optional discount."""
    if price < 0 or tax_rate < 0 or discount < 0:
        return None
    tax = calculate_tax(price, tax_rate)
    total = price + tax - discount
    return max(0, round(total, 2))
