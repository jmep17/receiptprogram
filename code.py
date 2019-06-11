# create loveseat desc variable
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
# create loveseat price
lovely_loveseat_price = 254.00

# create settee desc variable
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
# create settee price
stylish_settee_price = 180.50

# create lamp desc variable
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
# create lamp price
luxurious_lamp_price = 52.15

# set sales tax to 0.88 (8.8%)
sales_tax = .088

# keeping track of customer's total price
customer_one_total = 0
# keeping track of customer's items
customer_one_itemization = ""

# customer buying loveseat 
# change total price 
customer_one_total += lovely_loveseat_price 

# also change itemization
customer_one_itemization += lovely_loveseat_description

# customer buying lamp
# change total
customer_one_total += lovely_loveseat_price + luxurious_lamp_price 

# now change itemization
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description 

# ready to check out
# calculate tax 
customer_one_tax = customer_one_total * sales_tax
# adding calculated tax 
# to the total
customer_one_total = customer_one_total + customer_one_tax 

# printing their receipt 
print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)
