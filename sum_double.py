'''Given two integer values, return their sum. 
If the two values are the same, then return 
double their sum.'''

def sum_double(x, y):
    if x != y:
        return x + y
    else:
        return (x + y) * 2 