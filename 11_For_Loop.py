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