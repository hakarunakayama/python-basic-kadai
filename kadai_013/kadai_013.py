import random

price = random.randrange(100, 1000, 100)
tax = 10

def calculation(price, tax):
    return int(price * (1 + (tax / 100)))

calculation(price, tax)