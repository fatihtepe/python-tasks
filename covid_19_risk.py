''' Problem :
Task : Estimating the risk of death from coronavirus. Write a program that;
    Takes "Yes" or "No" from the user as an answer to the following questions :

Are you a cigarette addict older than 75 years old? Variable → age
Do you have a severe chronic disease? Variable → chronic
Is your immune system too weak? Variable → immune
    
    Set a logical algorithm using boolean logic operators (and/or) and use 
if-statements with the given variables in order to print out us a message : 
"You are in risky group"(if True ) or "You are not in risky group" (if False).'''



print('Enter two answer choices: Yes and No')
age = input('Are you a cigarette addict older than 75 years old?: ').lower().strip() == 'yes'
chronic = input('Do you have a severe chronic disease?: ').lower().strip() == 'yes'
immune = input('Is your immune system too weak?: ').lower().strip() == 'yes'
risk = chronic and (age or immune)

if risk:
    print('You are in risky group')
else:
    print('You are not in risky group')