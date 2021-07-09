import os
os.system('clear')

# Replace range(len()) With enumerate()

# Define a collection, such as list:
names = ['James', 'Jane', 'Katya', 'Jimmy', 'Lucas']

# Using the range(len(collection)) method, you'd write:
for i in range(len(names)):
    print(i, names[i])

# you will get the same result with enumerate

# Using enumerate, you can define this by writing:
for x, name in enumerate(names):
    print(x, name)


print('----------------------------------')


#The zip() function returns a zip object, 
# but you can coerce it into different datatypes 
# directly using, say, the list(), tuple(), or dict() functions.

names = ['Fatih', 'Ali', 'Melek', 'Dimitri']
ages = [32, 28, 37, 53]
gender = ['Male', 'Male', 'Female', 'Male']

# Zipping through lists with zip()
zipped = zip(names, ages, gender)
zipped_list = list(zipped)

print(zipped_list) # [('Nik', 32, 'Male'), ('Jane', 28, 'Female'), ('Melissa', 37, 'Female'), ('Doug', 53, 'Male')]