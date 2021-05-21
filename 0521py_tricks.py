import os 
clear = lambda: os.system("clear")
clear()

# To find new elelments of a list,

alist = [ 1, 3, 5, 7, 9 ]
blist = [ 4, 5, 6, 7, 8 ]

diff = set(alist) - set(blist)

print(diff)

