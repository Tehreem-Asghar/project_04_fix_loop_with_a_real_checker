"""
A small calculator module used by the billing system.
Handles basic arithmetic plus discount and tax calculations.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def apply_discount(price, discount_percent):
    """
    Applies a percentage discount to a price.
    e.g. apply_discount(100, 20) -> 80  (20% off of 100)
    """
    return price - (price * discount_percent / 100)


def calculate_total_with_tax(price, tax_rate):
    """
    tax_rate is a decimal, e.g. 0.08 for 8% tax.
    """
    tax = price * tax_rate
    return price + tax


def average(numbers):
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)