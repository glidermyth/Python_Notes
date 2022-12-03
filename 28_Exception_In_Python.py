
# The try...except statement works as follows:

# The statements in the try clause execute first.
# If no exception occurs, the except clause is skipped and the execution of the try statement is completed.
# If an exception occurs at any statement in the try clause, the rest of the clause is skipped and the except clause is executed.

# try:
#     first_number = float(input('Enter first number: '))
#     second_number = float(input('Second first number: '))
#     result = first_number/second_number
#     print(f"The result is {result}")
# except:
#     print(f"Some error has occurred")

# The try...except statement allows you to handle a particular exception. 
# To catch a selected exception, you place the type of exception after the except keyword:

# try:
#     first_number = float(input('Enter first number: '))
#     second_number = float(input('Second first number: '))
#     result = first_number/second_number
#     print(f"The result is {result}")
# except ValueError:
#     print(f"Please enter numbers")

# The try...except allows you to handle multiple exceptions by specifying multiple except clauses:

# try:
#     first_number = float(input('Enter first number: '))
#     second_number = float(input('Second first number: '))
#     result = first_number/second_number
#     print(f"The result is {result}")
# except ValueError as verr:
#     print(f"Please enter numbers")
# except ZeroDivisionError as zerr:
#     print(f"Can not divide by zero")

# If you want to have the same response to some types of exceptions, you can group them into one except clause:

# try:
#     first_number = float(input('Enter first number: '))
#     second_number = float(input('Second first number: '))
#     result = first_number/second_number
#     print(f"The result is {result}")
# except (ValueError, ZeroDivisionError) :
#     print("Some error has occurred")

# It’s a good practice to catch other general errors by placing the catch Exception block at the end of the list:

# try:
#     first_number = float(input('Enter first number: '))
#     second_number = float(input('Second first number: '))
#     result = first_number/second_number
#     print(f"The result is {result}")
# except ValueError as verr:
#     print(f"Please enter numbers")
# except ZeroDivisionError as zerr:
#     print(f"Can not divide by zero")
# except Exception as e:
#     print("Some error has occurred")


# The try...except statement also has an optional clause called finally:

# try:
#     # code that may cause exceptions
# except:
#     # code that handle exceptions
# finally:
#     # code that clean up

# The finally clause always executes whether an exception occurs or not. 
# And it executes after the try clause and any except clause.


# try:
#     first_number = float(input('Enter first number: '))
#     second_number = float(input('Second first number: '))
#     result = first_number/second_number
#     print(f"The result is {result}")
# except ValueError as verr:
#     print(f"Please enter numbers")
# finally : 
#     print("The resources has been released")

# The catch clause in the try...catch...finally statement is optional. So you can write it like this:

# try:
#     # the code that may cause an exception
# finally:
#     # the code that always executes

# Typically, you use this statement when you cannot handle the exception but you want to clean up resources. 
# For example, you want to close the file that has been opened.


# Python try…except…else statement
# The try statement has an optional else clause with the following syntax:

# try:
#     # code that may cause errors
# except:
#     # code that handle exceptions
# else:
#     # code that executes when no exception occurs

# The try...except...else statement works as follows:

# If an exception occurs in the try clause, Python skips the rest of the statements in the try clause and the except statement execute.
# In case no exception occurs in the try clause, the else clause will execute.
# When you include the finally clause, the else clause executes after the try clause and before the finally clause.


