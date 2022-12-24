# Encapsulation is one of the four fundamental concepts in object-oriented programming 
# including abstraction, encapsulation, inheritance, and polymorphism.

# Encapsulation is the packing of data and functions that work on that data within a single object. 
# By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.

# A class is an example of encapsulation. A class bundles data and methods into a single unit. 
# And a class provides the access to its attributes via methods.

# The idea of information hiding is that if you have an attribute that isn’t visible to the outside, 
# you can control the access to its value to make sure your object is always has a valid state.


# Private attributes
# Private attributes can be only accessible from the methods of the class. 
# In other words, they cannot be accessible from outside of the class.

# Python doesn’t have a concept of private attributes. In other words, all attributes are accessible from the outside of a class.

# By convention, you can define a private attribute by prefixing a single underscore (_)

# _attribute

# class Person:
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age

# person = Person("glider",22)
# print(person._name) # The attribute should not be accessed directly

# Name mangling with double underscores
# If you prefix an attribute name with double underscores (__) like this:

# __attribute
# Python will automatically change the name of the __attribute to:

# _class__attribute
# This is called the name mangling in Python.

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

# person = Person('Glider',22)

# print(person.__name)    # This will raise an error

# print(person._Person__name)