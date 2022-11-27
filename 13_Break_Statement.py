# Sometimes, you want to terminate a for loop or a while loop prematurely 
# regardless of the results of the conditional tests. In these cases, you can use the break statement
# Typically, you use the break statement with the if statement to terminate a loop when a condition is True.

# The following shows how to use the break statement inside a for loop:

# for index in range(n):
#     # more code here 
#     if condition:
#         break

# In this syntax, if the condition evaluates to True, the break statement terminates the loop immediately. 
# It won’t execute the remaining iterations.

# This example shows how to use the break statement inside a for loop:

for index in range(0, 10):
    print(index)
    if index == 3:
        break

# The break statement in the nested loop terminates the innermost loop when the y is greater than one.