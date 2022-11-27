# Python has three logical operators:

# and
# or
# not

a_val = True
b_val = True

print(a_val and b_val)
# The and operator returns True if both conditions are True. 
# And it returns False if either the condition a or b is False.


b_val = False

print(a_val or b_val)
# the or operator checks multiple conditions. But it returns True when either or both individual conditions are True
# The or operator returns False only when both conditions are False.


print(not a_val)
# The not operator applies to one condition. 
# And it reverses the result of that condition, True becomes False and False becomes True.

# Precedence of Logical Operators
# When you mix the logical operators in an expression, 
# Python will evaluate them in the order which is called the operator precedence.

# The following shows the precedence of the not, and, and or operators:
# not	 ->   High
# and	 ->   Medium
# or	 ->   Low