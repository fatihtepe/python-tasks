import os
os.system('clear')

# lambda function
tepe = lambda a, b: a**2 + b**2 + 2*(a+b)
print(tepe(3, 6)) # 63


# map function
def adds(a, b):
    return a + b
output = list(map(adds,[2, 6, 3], [1, 2, 3]))
print(output) # [3, 8, 6]


# filter function
def is_positive(x):
    return x > 0
output = list(filter(is_positive,[1, -2, 3, -4, 5, 6]))
print(output) # [1, 3, 5, 6]


# zip function
user_id = ["12121","56161","33287","23244"]
user = ["Mike","Johnny","Tam","Nicola"]
user_list = list(zip(user, user_id))
print(user_list) # [('Mike', '12121'), ('Johnny', '56161'), ('Tam', '33287'), ('Nicola', '23244')]



