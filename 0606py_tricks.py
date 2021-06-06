import os 
os.system('clear')

# 1 capitalize()
s = 'this is a sentence.'

# Re-inventing the wheel:
s = s[0].upper() + s[1:]

# Using the Python built-in function:
s.capitalize()
print(s.capitalize()) # This is a sentence.




# 2 title()
ss = 'useful python built-in string functions but few people use'

# Re-inventing the wheel:
words = s.split(' ')
words = [w[0].upper() + w[1:] for w in words]
s = ' '.join(words)

# Using the Python built-in function:
print(ss.title()) # Useful Python Built-In String Functions But Few People Use



