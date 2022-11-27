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