import os 
os.system('clear')

listem = [2, 3, 4, 4]
print(list(map(lambda x:x * 3.14, listem)))
# [6.28, 9.42, 12.56, 12.56]


add_3 = lambda a, b, c : a + b + c
print(add_3(1, 2, 3)) # 6
