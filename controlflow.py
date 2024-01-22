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


#Ternary Operators
age = input('Enter age:')
ticket_price = 30 if int(age) >= 18 else 5     #They follow the syntax: result = value_if_true if condition else value_if_false

print(f'Your ticket price is ${ticket_price}!') 
 

#For Loops
for m in range(5):
    print(m)
    m += 1

for index in range(0, 11, 5):
    print(index)

#Using the Python while statement to build a simple command prompt program
command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")

#Simple Python while statement
max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1

#While loop using a string
word = input("Enter a word: ")
reversed_word = ''

while len(word) > 0:
    reversed_word += word[-1]
    word = word[:-1]

print(f"Reversed word: {reversed_word}")


#More example
score = 100
student_score = 10
while student_score < score:
    print(student_score)
    student_score +=20


#Python break statement

#Break in a for loop
for index in range(10):
    print(index)
    if index == 2:
        break
        
for index in range(0, 10):
    print(index)
    if index == 3:
        break
   
#the break statement in a nested loop
for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})") 

#The break statement inside the while loop
print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favorite color:')
    if color.lower() == 'quit':
        break

while True:
    color = input('Enter your favorite color (type "exit" to stop):')
    if color.lower() == 'exit':
        break

#The break statement inside a while loop with an integer condition
counter = 0

while counter < 5:
    print(f"Current counter value: {counter}")
    
    if counter == 3:
        print("Breaking out of the loop.")
        break
    
    counter += 1

print("Loop finished.")


#The Python continue statement

#Python continue in a for loop example
for i in range(10):
    print(i)
    if i == 3:
        continue
        
for index in range(10):
    if index % 4:
        continue

    print(index)

#Python continue in a while loop example

# print the odd numbers 
counter = 0
while counter < 10:
    counter += 1

    if not counter % 3:
        continue

    print(counter)


#The Pass statement

for i in range(5):
    # Some condition, but no action needed for now
    if i % 2 == 0:
        pass
    else:
        print(i)

def not_implemented_yet():
    pass

not_implemented_yet()

#The pass statement is a statement that does nothing. 
#It’s just a placeholder for the code that you’ll write in the future.
#When you run the code that contains a pass statement, the Python interpreter will treat the pass statement as a single statement. 
#As a result, it doesn’t issue a syntax error.
#Technically, you can use the pass statement in many statement in Python.
"""