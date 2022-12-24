# We have learned about instance methods that are bound to a specific instance. 
# It means that instance methods can access and modify the state of the bound object.

# Also, we learned about class methods that are bound to a class. 
# The class methods can access and modify the class state.

# Unlike instance methods, static methods aren’t bound to an object. 
# In other words, static methods cannot access and modify an object state.

# In addition, Python doesn’t implicitly pass the cls parameter (or the self parameter) to static methods. 
# Therefore, static methods cannot access and modify the class’s state.

# In practice, you use static methods to define utility methods or group functions that have some logical relationships in a class.

# To define a static method, you use the @staticmethod decorator

# class className:
#     @staticmethod
#     def static_method_name(param_list):
#         pass