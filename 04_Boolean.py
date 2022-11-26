##### Python Boolean data type #####

# In programming, you often want to check if a condition is true or not and perform some actions based on the result.

# To represent true and false, Python provides you with the boolean data type. 
# The boolean value has a technical name as bool.

# The boolean data type has two values: True and False.

is_true = True
is_false = False

# When you compare two numbers, Python returns the result as a boolean value. For example:
print( 10 > 20 )
# Also, comparing two strings results in a boolean value:
print( 'a' > 'b')

# The bool() function
# To find out if a value is True or False, you use the bool() function.
print(bool('Hi'))
print(bool(0))

# Falsy and Truthy values
# When a value evaluates to True, it’s truthy. And if a value evaluates to False, it’s falsy.

# The following are falsy values in Python:

# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}
# The truthy values are the other values that aren’t falsy.