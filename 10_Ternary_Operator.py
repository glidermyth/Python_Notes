
age = input('Enter your age:')
if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

# To make it more concise, you can use an alternative syntax like this:

ticket_price = 20 if int(age) >= 18 else 5

# The following syntax is called a ternary operator in Python:

# value_if_true if condition else value_if_false

# Note that you have been programming languages such as C# or Java, 
# and you’re familiar with the following ternary operator syntax:

# condition ? value_if_true : value_if_false

# However, Python doesn’t support this ternary operator syntax.