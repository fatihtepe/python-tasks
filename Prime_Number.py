'''Task : Write a program that takes a number from the 
user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number'''



n = int(input('Please enter a number: '))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
    if count == 3:
        break
if (n == 0) or (n == 1) or (count == 3):
    print(f'{n} is not a prime number')
else:
    print(f'{n} is a prime number')
    
    
# Alternative Solution: if number is prime will return True

def check_prime(number):
    for x in range(2, int(number ** 0.5) + 1):
        if number % x == 0:
            return False
    return True
