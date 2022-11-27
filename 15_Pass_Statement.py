# Suppose that you have the following if...else statement:

# counter = 1
# max = 10
# if counter <= max:
#     counter += 1
# else:
#     # implement later

# In the else clause, you haven’t got any code yet. But you’ll write code for this else clause later.

# In this case, if you run the code, you’ll get a syntax error (SyntaxError).

# This is where the Python pass statement comes into play:

# counter = 1
# max = 10
# if counter <= max:
#     counter += 1
# else:
#     pass

# The pass statement is a statement that does nothing. 
# It’s just a placeholder for the code that you’ll write in the future.

# When you run the code that contains a pass statement, 
# the Python interpreter will treat the pass statement as a single statement. 
# As a result, it doesn’t issue a syntax error.

# def fn():
#     pass

# class Stream:
#     pass