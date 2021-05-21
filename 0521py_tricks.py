import os 
clear = lambda: os.system("clear")
clear()

# To find new elements of a list,
alist = [ 1, 3, 5, 7, 9 ]
blist = [ 4, 5, 6, 7, 8 ]

diff = set(alist) - set(blist)
print(diff)  # {1, 3, 9}



# Map() Function
def product(n1,n2): 
    return n1 *n2 

list1 = (1, 2, 3, 4) 
list2 = (10,20,30,40)

result = map(product, list1,list2) 
print(list(result))  # [10, 40, 90, 160]



# Map + Lambda Combination
list1 = (1, 2, 3, 4) 
list2 = (10,20,30,40)

result = map(lambda x,y: x * y, list1,list2) 
print(list(result))  # [10, 40, 90, 160]




# slice(start:stop[:step]) 
x = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

print(x[ 1: 6: 2])  # [2, 4, 6]
print(x[::-1])  # [8, 7, 6, 5, 4, 3, 2, 1]




# Zip and Enumerate together

NAME = ['Sid','John','David']
BIRD = ['Eagle','Sparrow','Vulture']
CITY =['Mumbai','US','London']

for i,(name,bird,city) in enumerate(zip(NAME,BIRD,CITY)):
    print(i,' represents ',name,' , ',bird,' and ',city)
    '''0  represents  Sid  ,  Eagle  and  Mumbai
       1  represents  John  ,  Sparrow  and  US
       2  represents  David  ,  Vulture  and  London'''




# Tuples

# how to define a list
num_list = [1,2,3,4]
# how to define a tuple
num_tuple = (1,2,3,4)
# use tuple() to convert
num_convert = tuple(num_list)



# Sets

# how to define a list
num_list = [1,2,3,4]
# how to define a set
num_set = {1, 2, 3, 4}
# use set() to convert
num_convert = set(num_list)


nums = {1,2,3,4,4}
print(nums) # {1,2,3,4}



# Combining a list of strings into a single one

sentence_list = ["my", "name", "is", "George"]
sentence_string = " ".join(sentence_list)
print(sentence_string)  # my name is George



# Initialising a list filled with some number

print([0]*1000) # List of 1000 zeros 
print([8.2]*1000) # List of 1000 8.2's



# Merging dictionaries
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
z = {**x, **y}
print(z)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}



# Reversing a string

name = "George"
print(name[::-1])  # egroeG



# Returning multiple values from a function
def get_a_string():
    a = "George"
    b = "is"
    c = "cool"
    return a, b, c
sentence = get_a_string()
print(sentence) # ('George', 'is', 'cool')
(a, b, c) = sentence
print(a, b, c)  # George is cool



# List comprehension
a = [1, 2, 3]
b = [num*2 for num in a] # Create a new list by multiplying each element in a by 2
print(b)  # [2, 4, 6]



# Iterating over a dictionary
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
for key, value in m.items():
    print('{0}: {1}'.format(key, value))
    '''a: 1
       b: 2
       c: 3
       d: 4'''
       



# Iterating over list values while getting the index too
m = ['a', 'b', 'c', 'd']
for index, value in enumerate(m):
    print('{0}: {1}'.format(index, value))
    '''0: a
       1: b
       2: c
       3: d'''



# Initialising empty containers
a_list = list()
a_dict = dict()
a_map = map()
a_set = set()


# Removing useless characters on the end of your string
name = "  George "
name_2 = "George///"
name.strip() # prints "George"
name_2.strip("/") # prints "George"



# Find the most frequent element in a list
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 4, 4]
print(max(set(test)))  # 4


# Check the memory usage of an object
import sys
x = 8
print(sys.getsizeof(x))  # 28

