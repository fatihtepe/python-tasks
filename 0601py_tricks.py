import os
os.system('clear')

# 1
candidateage = 30
candidate_exp = 5
candidate_salary_expect = 95000

if candidateage > 18:
    if candidate_salary_expect <= 100000:
        if candidate_exp >= 2:
            print('Congrats! You are eligible for job')
        else:
            print('Not eligible')
# Nothing wrong wiht the above code but there is better way!

if candidateage> 18 & candidate_exp >=2 & candidate_salary_expect <=10000:
    print('You are eligible for job')
else:
    print('Not eligible')
    
    

# 2 Inline Conditionals

x = 5
print('x equals 5') if x==5 else print('x is not 5')
for i in range(x+5): print(i)   

check = lambda x:True if x%5==0 else False
print(check(10)) ## True
print(check(12)) ## False



# 3 List Comprehensions

squares = [i * i for i in range(10) if i % 2 == 0]
print(squares) # [0, 4, 16, 36, 64]




# 4 F- Strings

name = 'Fatih'
age = 45
print(f'This is {name} and I am {age} years old')
# This is Fatih and I am 45 years old



# 5 Enumerate

lst = [23, 6, 68, 90, 11, 38, 23]
for index, value in enumerate(lst):
    if value % 2 == 0: 
        lst[index] = 'Even'
    else:
        lst[index] = 'Odd'
print(lst) # ['Odd', 'Even', 'Even', 'Even', 'Odd', 'Even', 'Odd']

