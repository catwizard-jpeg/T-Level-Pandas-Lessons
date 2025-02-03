import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/orders.csv")

#this data file contains details of all the orders that have
#been made to an online retailer

#the data set contains the following information:
# - Order Number
# - ID of customer who made the order
# - Code of the product ordered
# - Quantity of that product ordered
# - Total price of products in the row      

# Currently this data is hard for people to read
# We can use pandas to process this data        
# We can manipulate the data to show things that
#   the online retailer would want to know
#   (data manipulation means rearranging the data - not modifying it)

# We can find out the following things from this data:
# - What is the most ordered product
# - Which customer placed the most orders
# - Which customer spent the most money
# - How many orders contained just one product
# - How many orders contained multiple products
# - How much money was spend across all orders

# We can produce graphs to make this information easy
# to read and interpret
