
#task 1
# Declare four variables
followers = 1500
average_rating = 4.5
favorite_app = "Instagram"
is_premium_user = True

print(followers, type(followers))
print(average_rating, type(average_rating))
print(favorite_app, type(favorite_app))
print(is_premium_user, type(is_premium_user))


"""
#task 2
# Take the order price as a string
price = input("Enter Zomato order price: ")

# Convert string to float
price = float(price)

# Calculate 18% GST
gst = price * 0.18

# Calculate final bill
final_bill = price + gst

# Print the final bill
print("GST amount: ₹", gst)
print("Final bill amount: ₹", round(final_bill, 2))
"""



#task 3
prices = ['199.99', '299.50', '150']

# Converts strings to floats
float_prices = [float(price) for price in prices]

# Calculates total cart value
total = sum(float_prices)

print("Product prices:", float_prices)
print("Total cart value: ₹", round(total, 2))

#task-4
def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False

print(is_discount_applicable(450))
print(is_discount_applicable(750))

#task-5
ratings = ['4.5', '3.0', '5', '4.2']

# Convert strings to floats
float_ratings = [float(rating) for rating in ratings]

# Find the highest rating
highest_rating = max(float_ratings)

print("Ratings:", float_ratings)
print("Highest rating:", highest_rating)


