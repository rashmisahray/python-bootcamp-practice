# data manipulation and filtration using dictionaries
product_prices = {
    'apple': 20.00,
    'banana': 10.00,
    'orange': 25.00,
    'grapes': 45.00,
    'pineapple':50.00
}

# Filter products with prices above a certain threshold
threshold_price = 25.00
expensive_products = {product: price for product, price in product_prices.items() if price > threshold_price}

# Calculate the total cost of all products
total_cost = sum(product_prices.values())

# Output results
print("Expensive Products:")
for product, price in expensive_products.items():
    print(f"{product}: Rs.{price:.2f}")

print(f"\nTotal Cost of all Products: Rs.{total_cost:.2f}")
