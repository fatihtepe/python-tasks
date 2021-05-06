'''Task : Print the prime numbers which are between 1 
    to entered limit number (n).

1. You can use a nested for loop.
2. Collect all these numbers into a list

The desired output for n=100 :
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]'''

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input('Enter a number: '))
listem = []

for x in range(2,n):
    if is_prime_num(x):
        listem.append(x)
print(listem)