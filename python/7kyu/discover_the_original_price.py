# https://www.codewars.com/kata/552564a82142d701f5001228/train/python


def discover_original_price(discounted_price, sale_percentage):
    return float(f'{discounted_price * 100 / (100 - sale_percentage):.2f}')
