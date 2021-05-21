import os 
clear = lambda: os.system("clear")
clear()

import sys

def say_hello():
    print('hello everyone!!!')
    
print('this is the first print statement')
say_hello()

import sqlite3 as sql
# creating file path
dbfile = '/Users/tepe/Downloads/chinook.db'
# Create a SQL connection to our SQLite database
con = sql.connect(dbfile)
# creating cursor
cur = con.cursor()
# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute("SELECT title FROM albums WHERE albumid < 5"):
    print(row)
# Be sure to close the connection
con.close()


# List Comprehension
my_list = [i for i in range(1000)]
print(sum(my_list)) # 499500
print(sys.getsizeof(my_list), 'bytes') # 8856 bytes

# Generator Comprehension
my_gene = (i for i in range(1000))
print(sum(my_gene)) # 499500
print(sys.getsizeof(my_gene), 'bytes') # 112 bytes



# Multiple Inputs in Single Go
x, y, z = input('Enter values: ').split()

print(x, y, z)
print(x)
print(y)
print(z)



# Concatenate Strings Like a Pro
mix = ['H', 'e', 'l', 'l', 'o']
selam = ''.join(mix)
print(selam)  # Hello



# Count Objects with Counter
from collections import Counter

listem = [1,2,3,4,5,6,6,6,6,3,3,3,3,6,8,8,8,9,9,9]
print(Counter(listem))  # Counter({3: 5, 6: 5, 8: 3, 9: 3, 1: 1, 2: 1, 4: 1, 5: 1})



# Sort Complex Iterables in One Go

data = [{'name': 'John', 'age': 25},
        {'name': 'Max', 'age': 19},
        {'name': 'Lisa', 'age': 22}
        ]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)  # [{'name': 'Max', 'age': 19}, {'name': 'Lisa', 'age': 22}, 
                        #{'name': 'John', 'age': 25}]
                        # We have passed a lambda function 
                        # as a key to sort the dictionary by age.
                        


# Return More Than One Value From Function

def mix_calculator(a, b):
    add = a + b
    subtract = a - b
    divide = a / b
    multiply = a * b
    return add, subtract, divide, multiply

add, subtract, divide, multiply = mix_calculator(88, 8)

print('addition is:', add)
print('subtraction is: ', subtract)
print('division is:', divide)
print('multiplacation is:', multiply)
