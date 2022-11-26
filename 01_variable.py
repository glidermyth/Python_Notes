# If you’ve been working in other programming languages such as Java, 
# C#, or C/C++, you know that these languages use semicolons (;) to separate the statements.

# However, Python uses whitespace and indentation to construct the code structure.

# To create a block comment, you start with a single hash sign (#) followed by a single space and a text string.

# A documentation string is a string literal that you put as the first lines in a code block, for example, a function.

# Unlike a regular comment, a documentation string can be accessed at run-time using  obj.__doc__ 
# attribute where obj is the name of the function.
""" example docstring """

# Python uses single quotes ('), double quotes ("), triple single quotes (''') and 
# triple-double quotes (""") to denote a string literal.

##### When you develop a program, you need to manage values, a lot of them. To store values, you use variables.#####

# In Python, a variable is a label that you can assign a value to it. 
# And a variable is always associated with a value. For example:

# variable_name = value
message = 'Hello, World'
print(message)

# The following are the variable rules that you should keep in mind:

# Variable names can contain only letters, numbers, and underscores (_). 
# They can start with a letter or an underscore (_), not with a number.
# Variable names cannot contain spaces. To separate words in variables, you use underscores for example sorted_list.
# Variable names cannot be the same as keywords, reserved words, and built-in functions in Python.
