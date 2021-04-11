# LEAP YEAR CALCULATOR (without using conditional statement(if))
# Print True if the given year by the user is a leap year,
# print False otherwise.


year = int(input('Please enter a year: '))
result = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(result)