#Azubi store products 

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price for each product
total_prices = [price * quantity for price, quantity in zip(prices, last_week)]

# Calculate the total price for all products
total_price_all_products = sum(total_prices)

# Calculate the total quantity sold for all products
total_quantity_sold = sum(last_week)

# Calculate the average price per unit sold
average_price_per_unit = total_price_all_products / total_quantity_sold

# Display the result
print("Total Price for All Products:", total_price_all_products)
print("Total Quantity Sold for All Products:", total_quantity_sold)
print("Average Price per Unit Sold:", average_price_per_unit)

#Task 2 to create a new price list that reduces the old prices by $ 5

# Define the lists
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Reduce prices by $5
new_prices = [price - 5 for price in prices]

# Display the old and new price lists
print("Old Prices:", prices)
print("New Prices:", new_prices)

#Task 3 
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

def calculate_total_revenue(prices, quantities):
    # Calculate the total revenue for each product and sum them up
    total_revenue = sum(price * quantity for price, quantity in zip(prices, quantities))
    return total_revenue

# Calculate total revenue
total_revenue = calculate_total_revenue(prices, last_week)

# Display the result
print("Total Revenue Generated: $", total_revenue)

#Task 4
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate daily revenue for each product
daily_revenue = [price * sales for price, sales in zip(prices, last_week)]

# Calculate the total revenue for the week
total_revenue = sum(daily_revenue)

# Calculate the average daily revenue
average_daily_revenue = total_revenue / len(last_week)

# Display the results
print("Daily Revenue for Each Product:")
for product, revenue in zip(products, daily_revenue):
    print(f"{product}: ${revenue}")

print("\nTotal Revenue for the Week: ${}".format(total_revenue))
print("Average Daily Revenue: ${:.2f}".format(average_daily_revenue))

#task 5 based on the new prices, which products are less than $ 30 
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

new_prices = [price - 5 for price in prices]  # Reducing each price by $5

# Find products with prices less than $30
affordable_products = [product for product, price in zip(products, new_prices) if price < 30]

# Display the affordable products
print("Products with prices less than $30:")
for product in affordable_products:
    print(product)
