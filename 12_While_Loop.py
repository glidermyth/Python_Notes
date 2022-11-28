# Python while statement allows you to execute a code block repeatedly as long as a condition is True.

# The following shows the syntax of the Python while statement:

# while condition:  
#    body

max = 5
counter = 0

while counter < max :
    print(counter)
    counter+=1

command = ''

while command.lower() != 'quit' :
    command = input('>')
    print(f'Echo: {command}')


##### Python while else statement #####
# In Python, the while statement may have an optional else clause:

# while condition:
#     # code block to run
# else:
#     # else clause code block

# In this syntax, the condition is checked at the beginning of each iteration. 
# The code block inside the while statement will execute as long as the condition is True.

# When the condition becomes False and the loop runs normally, the else clause will execute. 
# However, if the loop is terminated prematurely by either a break or return statement, 
# the else clause won’t execute at all.


# First, specify the condition as True in the while loop like this:

# while True:
#     # code block

# This allows the code block to execute for the first time. 
# However, since the condition is always True, it creates an indefinite loop. This is not what we expected.
# Second, place a condition to break out of the while loop:

# while True:
#     # code block

#     # break out of the loop
#     if condition
#         break

# In this syntax, the code block always executes at least one for the first time and 
# the condition is checked at the end of each iteration.