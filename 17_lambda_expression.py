# Python lambda expressions allow you to define anonymous functions.

# Anonymous functions are functions without names. 
# The anonymous functions are useful when you need to use them once.

# A lambda expression typically contains one or more arguments, but it can have only one expression.

# lambda parameters: expression

def get_full_name(first_name,last_name,formater) :
    return formater(first_name,last_name)

result = get_full_name('Lenovo','Doc',lambda first,last : f'{last} {first}')
print(result)

# Use lambda expressions to pass anonymous functions to a function and return a function from another function.

def times(n) :
    return lambda x : x * n

double = times(3)
print(double(3))
print(double(2))


# Python stores the docstrings in the __doc__ property of the function.
# The following example shows how to access the __doc__ property of the add() function:

def add(a,b) :
    '''
    This function returns the addition of two variables
    '''
    return a + b

print(add.__doc__)