'''Task:
Find out if a given number is an "Armstrong Number".
    An n-digit number that is the sum of the nth powers of 
its digits is called an n-Armstrong number. 

Examples :
371 = 33 + 73 + 13;
9474 = 94 + 44 + 74 + 44;
93084 = 95 + 35 + 05 + 85 + 45.

Write a Python program that;
1.takes a positive integer number from the user,
2. checks the entered number if it is Armstrong,
3. consider the negative, float and any entries other than 
numeric values then display a warning message to the user.'''


number = input('Please enter a positive number: ')

if number.isdigit():
    list_str_num = list(number)
    power = len(list_str_num)
    result = 0

    for num in list_str_num:
        result += int(num) ** power
    if result == int(number):
        print(f'{number} is an Armstrong number')
    else:
        print(f'{number} is not an Armstrong number')  
else:
    print('It is an invalid entry. Don\'t use non-numeric, float, or negative values!')



# Second Solution:

while True :
    number = input("enter a positive number: ")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "is invalid entry. enter numberic value!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number.")
            break