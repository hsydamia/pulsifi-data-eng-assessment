# Given that I have a dictionary of orders on what to buy
orders = {"apple": 5, "banana": 2, "pear": 4}

# This is the price of every item in a fruit shop
fruit_shop = {"apple": 1, "banana": 2, "pear": 3}

total_amount = sum(orders[i] * fruit_shop[i] for i in orders)
print(total_amount)

