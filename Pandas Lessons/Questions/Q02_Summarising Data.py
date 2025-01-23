#step 1
#import the libraries you will need
print("step 1")
print("import the libraries you will need")
import pandas as pd

print("step 2")
print("get the dataset")

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

print("step 3")
print("save it to a sensible variable name")

chipo = pd.read_csv(url, sep = '\t')

print("step 4")
print("look at the first 25 entries")

#Your code goes here:

print(chipo.head(25))

print("#"*10)
input()

print("step 5")
print("find out how many rows are in the dataset")

#Your code goes here:

print(chipo.shape[0])

print("#"*10)
input()

print("step 6")
print("find out how many columns are in the dataset")

#Your code goes here:

print(chipo.shape[1])

print("#"*10)
input()

print("step 7")
print("find out the names of all the columns")

#Your code goes here:

print(chipo.columns)

print("#"*10)
input()

print("step 8")
print("find out how the dataset is indexed")

#Your code goes here:

print(chipo.index)

print("#"*10)
input()

print("step 9")
print("describe the dataset, make sure to include every column")

#Your code goes here:

print(chipo.describe(include="all"))

print("#"*10)
input()

print("step 10")
print("find the most ordered item")

#Your code goes here:

print(chipo['item_name'].value_counts().head(1))

print("#"*10)
input()

print("step 11")
print("find out how many times the item from step 10 was ordered")

#Your code goes here:

print(chipo['item_name'].value_counts().max())

print("#"*10)
input()

print("step 12")
print("find out the most ordered item in the choice_description colum")

#Your code goes here:

print(chipo['choice_description'].value_counts().head(1))

print("#"*10)
input()

print("step 13")
print("find out how many items were ordered in total")

#Your code goes here:

print(chipo['quantity'].sum())

print("#"*10)
input()

print("step 14")
print("find out how many orders are in the entire dataset")

#Your code goes here:

print(chipo['order_id'].nunique())

print("#"*10)
input()

print("step 15")
print("find out how many different items are sold in this dataset")

#Your code goes here:

print(chipo['item_name'].nunique())

print("#"*10)
input()


print("step 16")
print("find out the data type of the item_price column")

#Your code goes here:

print(chipo['item_price'].dtype)

print("#"*10)
input()

print("step 17")
print("change the data type of the item_price column to float")

#Your code goes here:

chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype(float)

print("#"*10)
input()

print("step 18")
print("find out the total revenue of all orders in the dataset")

#Your code goes here:

print(chipo['item_price'].sum())

print("#"*10)
input()

print("step 19")
print("find out the average price of an order")

#Your code goes here:

print(chipo.groupby('order_id')['item_price'].sum().mean())

print("#"*10)
input()

