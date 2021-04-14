# Task - 1 :
# You work for a manufacturer as a programmer and have been asked to 
# calculate the total profit made on the sales of a product. 
# You are given a dictionary (sales) containing the cost price 
# per unit (in dollars), sell price per unit (in dollars), and 
# the beginning inventory. Write a program to return the total profit 
# made, rounded to the nearest dollar. Assume all of the inventory 
# has been sold. The name and the keys of the dictionary are constant, 
# so use them as they are.


sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

profit = int((sales['sell_value'] * sales['inventory']) - (sales['cost_value'] * sales['inventory']))
print('the profit will be:', profit)



# Task-2 Float Type two digits after the period
amounts = [3, 29.99, 4.1]

for i in amounts:
    print("${0:.2f}".format(i))
amounts = [3, 29.99, 4.1]
