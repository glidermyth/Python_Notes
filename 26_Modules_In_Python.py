# Python modules
# A module is a piece of software that has a specific functionality. 
# A Python module is a file that contains Python code.

# For example, when building a shopping cart application, 
# you can have one module for calculating prices and another module for managing items in the cart. 
# Each module is a separate Python source code file.

# A module has a name specified by the filename without the .py extension. 
# For example, if you have a file called pricing.py, the module name is pricing.

# To use objects defined in a module, you need to import the module using the following import statement:

# import module_name

# For example, to use the pricing module in the main.py file, you use the following statement:

# import pricing

# This module name allows you to access functions, variables, etc. 
# from the imported module in the current module. 
# For example, you can call a function defined in the imported module using the following syntax:

# module_name.function_name()

# If you don’t want to use the pricing as the identifier in the main.py, you can rename the module name to another as follows:

# import pricing as selling_price

# If you want to reference objects in a module without prefixing the module name, 
# you can explicitly import them using the following syntax:

# from module_name import fn1, fn2

# Now, you can use the imported functions without specifying the module name like this:

# fn1()
# fn2()

# It’s possible to rename an imported name to another by using the following import statement:

# from <module_name> import <name> as <new_name>

# The following example renames the get_net_price() function from the pricing module to calculate_net_price() function:

# from pricing import get_net_price as calculate_net_price

# net_price = calculate_net_price(
#     price=100,
#     tax_rate=0.1,
#     discount=0.05
# )

# To import every object from a module, you can use the following syntax:

# from module_name import *

# This import statement will import all public identifiers including variables, constants, functions, classes, etc., to the program.

# However, it’s not a good practice because if the imported modules have the same object, 
# the object from the second module will override the first one. The program may not work as you would expect.



##### Python module search path #####
# When you import a module in a program:

# import module

# Python will search for the module.py file from the following sources:

# The current folder from which the program executes.
# A list of folders specified in the PYTHONPATH environment variable, if you set it before.
# An installation-dependent list of folders that you configured when you installed Python.
# Python stores the resulting search path in the sys.path variable that comes from the sys module.

# The following program shows the current module search path:

# import sys

# for path in sys.path:
#     print(path)

# Here’s a sample output on Windows:

# D:\Python\
# C:\Program Files\Python38\python38.zip
# C:\Program Files\Python38\DLLs
# C:\Program Files\Python38\lib
# C:\Program Files\Python38
# C:\Users\PythonTutorial\AppData\Roaming\Python\Python38\site-packages
# C:\Program Files\Python38\lib\site-packages 


# To make sure Python can always find the module.py, you need to:

# Place module.py in the folder where the program will execute.
# Include the folder that contains the module.py in the PYTHONPATH environment variable. 
# Or you can place the module.py in one of the folders included in the PYTHONPATH variable.
# Place the module.py in one of the installation-dependent folders.
# Modifying the Python module search path at runtime
# Python allows you to modify the module search path at runtime by modifying the sys.path variable. 
# This allows you to store module files in any folder of your choice.

# Since the sys.path is a list, you can append a search-path to it.

# The following example adds the d:\modules to the search path and use the recruitment module stored in this folder:

# >>> import sys
# >>> sys.path.append('d:\\modules\\')
# >>> import recruitment
# >>> recruitment.hire()
# Hire a new employee...