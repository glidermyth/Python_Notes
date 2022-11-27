# A function is a named code block that performs a job or returns a value.

# Sometimes, you need to perform a task multiple times in a program.
# And you don’t want to copy the code for that same task all over places.
# To do so, you wrap the code in a function and use this function to perform the task whenever you need it.

#--> Function definition
# A function definition starts with the def keyword and the name of the function.

# If the function needs some information to do its job, you need to specify it inside the parentheses (). 
# The greet function in this example doesn’t need any information, so its parentheses are empty.

# The function definition always ends in a colon (:)

#--> Function body
# All the indented lines that follow the function definition make up the function’s body.

# The text string surrounded by triple quotes is called a docstring. It describes what the function does. 
# Python uses the docstring to generate documentation for the function automatically.

#--> Calling a function
# When you want to use a function, you need to call it. 
# A function call instructs Python to execute the code inside the function.

# To call a function, you write the function’s name, 
# followed by the information that the function needs in parentheses.


def greet(name) :
    """ This functions prints the name """
    print(name)

greet('someone') #calling the function


# Parameters vs. Arguments
# Sometimes, parameters and arguments are used interchangeably. 
# It’s important to distinguish between the parameters and arguments of a function.

# A parameter is a piece of information that a function needs. 
# And you specify the parameter in the function definition. 

# An argument is a piece of data that you pass into the function. 


def add(a,b) :
    return a+b

result = add(6,7)
print(f'Result : {result}')


##### Default Parameter #####

# When you define a function, you can specify a default value for each parameter.
# To specify default values for parameters, you use the following syntax:

# def function_name(param1, param2=value2, param3=value3, ...):

# In this syntax, you specify default values (value2, value3, …) for each parameter 
# using the assignment operator (=).

# When you call a function and pass an argument to the parameter that has a default value, 
# the function will use that argument instead of the default value.

# However, if you don’t pass the argument, the function will use the default value.

# To use default parameters, you need to place parameters with the default values after other parameters. 
# Otherwise, you’ll get a syntax error.

# For example, you cannot do something like this:

# def function_name(param1=value1, param2, param3):
# This causes a syntax error.

def greet(name='someone',message='hii') :
    print(f'{name} {message}')

greet()
greet('yo','bro')


##### Python keyword arguments #####

# To improve the readability, Python introduces the keyword arguments.

# The following shows the keyword argument syntax:

# fn(parameter1=value1,parameter2=value2)

# By using the keyword argument syntax, you don’t need to specify the 
# arguments in the same order as defined in the function.
# Therefore, you can call a function by swapping the argument positions like this:

# fn(parameter2=value2,parameter1=value1)

# Once you use a keyword argument, you need to use keyword arguments for the remaining parameters.

greet(message='hello',name='world')