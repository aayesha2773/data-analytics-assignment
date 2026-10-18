

"""
# task-1 Create a Python script that takes any product name string (e.g., 'Redmi Note 12 Pro') and prints the name in all uppercase and all lowercase using the upper() and lower() methods.
product_name = input("Enter product name: ")

print("Uppercase:", product_name.upper())
print("Lowercase:", product_name.lower())
"""
"""
# task-2 
def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name

print(clean_brand_name(' oneplus-Nord '))
"""
"""
#task- 3
product = 'Apple iPhone 14 Pro Max'

# Find the position of the first space
split_point = product.index(' ')

# Extract brand name and model using slicing
brand = product[:split_point]
model = product[split_point + 1:]

print("Brand Name:", brand)
print("Model:", model)
"""
"""
#task-4 
def format_product_display(name, price):
    return f"{name} - ₹{price}"   #uses an f-string to combine the product name, a hyphen, the rupee symbol (₹), and the price.


print(format_product_display('Boat Earbuds', 1299))
"""
"""
#task-5
products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_products = []

for name in products:
    name = name.strip()       # Remove leading and trailing spaces
    name = name.replace("-", " ")  # Replace hyphens with spaces
    name = name.title()       # Convert to title case
    cleaned_products.append(name)

print(cleaned_products)

"""