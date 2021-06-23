import os
os.system('clear')

# List Comprehensions

mylist = [i for i in range(10)]
print(mylist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def some_function(a):
    return(a + 5) / 2

my_formula = [some_function(i) for i in range(10)]
print(my_formula)  # [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]


filtered = [i for i in range(20) if i % 2 == 0]
print(filtered)  # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]



# Merging dictionaries

dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
print (merged)  # {'a': 1, 'b': 3, 'c': 4}

# Python >= 3.9 only
merged = dict1 | dict2
print (merged)  # {'a': 1, 'b': 3, 'c': 4}

    

# String to title case

mystring = "10 awesome python tricks"
print(mystring.title())  # 10 Awesome Python Tricks


# Split a string into a list

mystring = 'The quick brow bear'
mylist = mystring.split(' ')
print(mylist)  ['The', 'quick', 'brow', 'bear']




