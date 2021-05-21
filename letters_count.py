'''Task:
    Count the number of each letter in a sentence.
The department you work for undertook a project 
construction that makes word / text analysis.
You are asked to calculate the number of letters or any 
chars in the sentences entered under this project.
    Write a Python program that;
1. takes a sentence from the user,
2. counts the number of each letter of the sentence,
3. collects the letters/chars as a key and the counted 
    numbers as a value in a dictionary.
'''


sentence = input('Please enter: ')

def sentence_dict(sentence):
    s_dict = {}
    for char in sentence:
        if char in s_dict.keys():
            s_dict[char] += 1
        else:
            s_dict[char] = 1
    return s_dict

print(sentence_dict(sentence))
