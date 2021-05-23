import os 
clear = lambda: os.system("clear")
clear()

'''Accessing Index and Value at the Same Time
enumerate() inbuilt function lets you access index and 
value at the same time within a or loop.'''

arr = [2,4,6,3,'six',10]

for index,value in enumerate(arr):
    print(index, value)

'''
0 2
1 4
2 6
3 3
4 six
5 10
'''


'''Check for an Anagram
An anagram is a word that is formed by rearranging 
the letters of a different word, using all the original 
letters exactly once.'''

def check_anagram(first_word, second_word):
      return sorted(first_word) == sorted(second_word)
  
print(check_anagram("silent", "listen"))   # True
print(check_anagram("ginger", "danger"))   # False



'''Converting two lists into a dictionary
The following method can be used to convert 
two lists into a dictionary.'''

list1 = ['karl','lary','keera']
list2 = [28934,28935,28936]
dictt0 = dict(zip(list1,list2))
print(dictt0)  # {'karl': 28934, 'lary': 28935, 'keera': 28936}



'''Error Handling'''

# Example 1
try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
    print(c)
except:  
    print("Can't divide with zero") 

# Example 2
try:    
    #this will throw an exception if the file doesn't exist.     
    fileptr = open("/Users/tepe/Downloads/Info_Flyer.pdf","r")    
except IOError:    
    print("File not found")    
else:    
    print("The file opened successfully")    
    fileptr.close()  




'''Most Frequent in a List
This method below returns the most frequent 
elements that appears in a list.'''

def most_frequent(nums):
    return max(set(nums), key = nums.count)

frlist = [1,2,3,4,5, 6, 7, 8,8,8]
print(most_frequent(frlist))  # 8




'''Calculator Without if-else
This code snippet shows how simply you can write a 
calculator without using any if-else conditions.'''

import operator

action = {
  "+" : operator.add,
  "-" : operator.sub,
  "/" : operator.truediv,
  "*" : operator.mul,
  "**" : pow
}

print(action['*'](5, 5))    # 25




'''Swap Values
A quick way to swap two variables without 
the need for an extra one.'''

a,b = 5,7

# Method 1
b,a = a,b

# Method 2
def swap(a,b):
  return b,a
swap(a,b)


