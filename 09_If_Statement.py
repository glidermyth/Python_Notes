# You use the if statement to execute a block of code based on a specified condition.
# The if statement checks the condition first.
# If the condition evaluates to True, it executes the statements in the if-block. 
# Otherwise, it ignores the statements.

# Typically, you want to perform an action when a condition is True and another action when the condition is False.
# To do so, you use the if...else statement.

age = int(input('Enter the age : '))

if age>=18 :
    print(f'You can vote.Your age is {age}')
else :
    print(f'You can not vote.Your age is {age}')

# If you want to check multiple conditions and perform an action accordingly, 
# you can use the if...elif...else statement. The elif stands for else if.

# Here is the syntax if the if...elif...else statement:

if age<5 :
    print(f'Your ticket price is 3')
elif age<16 :
    print(f'Your ticket price is 12')
elif age<18:
    print(f'Your ticket price is 15')
else :
    print(f'Your ticket price is 22')

