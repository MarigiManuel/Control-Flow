#Control Flow Statements

#Using if and else statements
"""
age = input('Enter your age: ')
if int(age) >= 18:
    print("Elligible to vote!")
else:
    print('Not elligible')
    

Exam_Score = input("What grade did you obtain?: ")
if Exam_Score.upper() == 'A':                           #The upper() method allows for the case-insentive input.
    print('Congratulations, you passed!')
else:
    print('Pull up your socks!')
   

#Using if, elif, and else statements.

age = input('Enter your age: ')

try:
    your_age = int(age)
    
    if your_age < 10:
        ticket_price = 50
    elif your_age < 18:
        ticket_price = 200
    elif your_age <= 100:
        ticket_price = 500
    else:
        ticket_price = 1000
    print(f'Your ticket price is ${ticket_price}.')
except ValueError:
    print('Please enter a valid age as a number.')
 """

#Ternary Operators
age = input('Enter age:')
ticket_price = 30 if int(age) >= 18 else 5     #They follow the syntax: result = value_if_true if condition else value_if_false

print(f'Your ticket price is ${ticket_price}!') 