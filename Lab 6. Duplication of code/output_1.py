def apply_discount(price, discount):
    return price * 0.9 if discount else price


def calculate_total_price(product_prices, discount):
    return sum(apply_discount(price, discount) for price in product_prices)


def calculate_total_price_with_tax(product_prices, discount, tax_rate):
    total_price = calculate_total_price(product_prices, discount)
    return total_price * (1 + tax_rate)
