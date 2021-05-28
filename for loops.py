import os
os.system('clear')

# 1. items() and values()

scores = {"John": 94, "Mike": 95, "Sandra": 98, "Jennifer": 95}

for score in scores:
    print(score)
'''John
   Mike
   Sandra
   Jennifer'''
   
   
for score in scores.items():
    print(score)
'''('John', 94)
('Mike', 95)
('Sandra', 98)
('Jennifer', 95)'''


for name, score in scores.items():
    print('Student Name: ' + name + ', Score: ' + str(score))
'''Student Name: John, Score: 94
Student Name: Mike, Score: 95
Student Name: Sandra, Score: 98
Student Name: Jennifer, Score: 95'''

for score in scores.values():
    print(score)
'''94
95
98
95'''


# 2. enumerate()

grades = ["Freshman", "Sophomore", "Junior", "Senior"]

for grade in enumerate(grades):
    print(grade)
'''(0, 'Freshman')
(1, 'Sophomore')
(2, 'Junior')
(3, 'Senior')'''


for year, name in enumerate(grades, start=1):
    print('Year ' + str(year) + ': ' + name)
'''Year 1: Freshman
Year 2: Sophomore
Year 3: Junior
Year 4: Senior'''


# 3. reversed()
arrived_students = ["John", "Mike", "Sandra", "Jennifer"]

for student in reversed(arrived_students):
    print(student)
'''Jennifer
Sandra
Mike
John'''


# 4. sorted()
students = ["John", "Mike", "Sandra", "Jennifer", "Fatih"]

for student in sorted(students):
    print(student)
'''Fatih
Jennifer
John
Mike
Sandra'''


# 5. filter()

students = [{"name": "John", "id": 1}, {"name": "Mike", "id": 4}, 
            {"name": "Sandra", "id": 2},
            {"name": "Jennifer", "id": 3}, 
            {"name": "Fatih", "id": 5}]

for student in filter(lambda i: i['id'] % 2 != 0, students):
    print(student)

'''{'name': 'John', 'id': 1}
{'name': 'Jennifer', 'id': 3}
{'name': 'Fatih', 'id': 5}'''


# 6. zip()

names = ["John", "Mike", "Sandra", "Jennifer", "Fatih"]
ids = [11, 33, 22, 44, 55]

for student in zip(names,ids):
    print(student)
    
'''('John', 11)
('Mike', 33)
('Sandra', 22)
('Jennifer', 44)
('Fatih', 55)'''