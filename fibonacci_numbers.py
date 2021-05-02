'''Assignment-008/5 (Fibonacci Numbers)

Task : Create a list consisting of Fibonacci numbers 
from 1 to 55 using control flow statements.

The desired output is like :
fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]'''


n = 55
fibonacci_num = [1, 1]
counter = 0

while counter < n:
    counter = fibonacci_num[-1] + fibonacci_num[-2]
    fibonacci_num.append(counter)
    
print(fibonacci_num)

