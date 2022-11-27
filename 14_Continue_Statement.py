# The continue statement is used inside a for loop or a while loop. 
# The continue statement skips the current iteration and starts the next one.

# Typically, you use the continue statement with an if statement to skip the current iteration once a condition is True.

# The following shows how to use the continue statement in a for loop:

# for index in range(n):
#     if condition:
#        continue
#     # more code here


# The following example shows how to use the for loop to display even numbers from 0 to 9:

for index in range(10):
    if index % 2:
        continue

    print(index)