# In programming, you often want to execute a block of code multiple times. To do so, you use a for loop.

# The following illustrates the syntax of a for loop:

# for index in range(n):
#     statement

# In this syntax, the index is called a loop counter. 
# And n is the number of times that the loop will execute the statement.

for index in range(6) :
    print(index,end=', ')


# By default, the range() function uses zero as the starting number for the sequence.
# In addition, the range() function allows you to specify the starting number like this:
# range(start, stop)

for index in range(10,15) :
    print(index)


# By default, the range(start, stop) increases the start value by one in each loop iteration.
# To increase the start value by a different number, you use the following form of the range() function:
# range(start, stop, step)

for index in range(1,11,2):
    print(index,end=' ')


fruits = ['apple','banana','orange','grapes','dates']
for name in fruits :
    print(name,end=' ')


##### Python for else statement #####
# In Python, the for statement can have an optional else clause, 
# which you may not be familiar with especially if you’re coming from other languages such as Java or C#.

# The following shows the syntax of the for statement with the else clause:

# for item in iterables:
#     # process item 
# else:
#     # statement

# In this syntax, the else clause will execute only if the loop runs normally. 
# In other words, the else clause won’t execute if the loop encounters a break statement.
# In addition, the else clause also executes when the iterables object has no item.


# people = [{'name': 'John', 'age': 25},
#         {'name': 'Jane', 'age': 22},
#         {'name': 'Peter', 'age': 30},
#         {'name': 'Jenifer', 'age': 28}]

# name = input('Enter a name:')

# for person in people:
#     if person['name'] == name:
#         print(person)
#         break
# else:
#     print(f'{name} not found!')

# By using the for else statement, the program doesn’t need to use a flag and an if statement after the loop.
# In this new program, if the input name matches a person on the list, 
# it’ll show the person’s information and exit the loop by using the break statement.

# When the loop encounters the break statement, the else clause won’t execute.