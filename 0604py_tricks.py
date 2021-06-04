import os
os.system('clear')

# List methods: append and extend

x = [1, 2, 3]
y = [4, 5]
x.append(y)
print(x) # [1, 2, 3, [4, 5]]

x = [1, 2, 3]
y = [4, 5]
x.extend(y)
print(x) # [1, 2, 3, 4, 5]

# map and lambda
'''The .map() function allows us to 
map an iterable to a function. For example:'''

def add2(x):
    return x + 2

print(list(map(add2, [1, 2, 3]))) # [3, 4, 5]


result = [1, 2, 3]
print(list(map(lambda x: x + 2, result))) # [3, 4, 5]


