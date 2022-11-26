##### String in Python #####

# A string is a series of characters. In Python, anything inside quotes is a string. 
# And you can use either single or double quotes. For example:

message_one = 'This is a string'
message_two = "this is also a string"

# If a string contains a single quote, you should place it in double-quotes like this:
message_three = "It's a string"

# And when a string contains double quotes, you can use the single quotes:
message_four = '"Beautiful is better than ugly.". Said Tim Peters'

# To escape the quotes, you use the backslash (\). For example:
message_five = 'It\'s also a valid string'

# The Python interpreter will treat the backslash character (\) special. 
# If you don’t want it to do so, you can use raw strings by adding the letter r before the first quote. For example:
message_six = r'C:\python\bin'

# To span a string multiple lines, you use triple-quotes “””…””” or ”’…”’. For example:
message_seven = """
    This message is written by someone
    This is a multi line string
"""
print(message_seven)

# Sometimes, you want to use the values of variables in a string.
# For example, you may want to use the value of the name variable inside the message string

name = 'VS'
message_eight = f'Hello, {name} code'
print(message_eight)

# Concatenating Python strings
# When you place the string literals next to each other, Python automatically concatenates them into one string.

greeting = 'Good' 'Morning'
print(greeting)

# To concatenate two string variables, you use the operator +:

greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)


# Accessing string elements
# Since a string is a sequence of characters, 
# you can access its elements using an index. The first character in the string has an index of zero.

str = "Python String"
print(str[0])
print(str[1])

# If you use a negative index, Python returns the character starting from the end of the string. For example:

print(str[-1])  # g
print(str[-2])  # n
"""
+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 

"""

# Getting the length of a string
# To get the length of a string, you use the len() function. For example:

str_len = len(str)
print(str_len)

# Slicing strings
# Slicing allows you to get a substring from a string. For example:

print(str[0:2])

# The str[0:2] returns a substring that includes the character from the index 0 (included) to 2 (excluded).
# The syntax for slicing is as follows:
# string[start:end]

# The substring always includes the character at the start and excludes the string at the end.
# The start and end are optional. If you omit the start, it defaults to zero. 
# If you omit the end, it defaults to the string’s length.

# Python strings are immutable
# Python strings are immutable. It means that you cannot change the string. 
# For example, you’ll get an error if you update one or more characters in a string:

# str = "Python String"
# str[0] = 'J'    # This line will throw error

# When want to modify a string, you need to create a new one from the existing string. For example:

new_str = 'J' + str[1:]
print(new_str)