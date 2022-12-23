# Objects
# An object is a container that contains data and functionality.

# The data represents the object at a particular moment in time. 
# Therefore, the data of an object is called the state. Python uses attributes to model the state of an object.

# The functionality represents the behaviors of an object. Python uses functions to model the behaviors. 
# When a function is associated with an object, it becomes a method of the object.

# In other words, an object is a container that contains the state and methods.

class Person:
    pass

person = Person()

# When printing out the person object, you’ll see its name and memory address
# print(person)
# The id of an object is unique. In CPython, the id() returns the memory address of an object. 
# The hex() function converts the integer returned by the id() function to a lowercase hexadecimal string prefixed with 0x:
# print(id(person))
# print(hex(id(person)))

# The person object is an instance of the Person class. 
# The isinstance() function returns True if an object is an instance of a class:

# print(isinstance(person,Person))


# A class is also an object in Python
# Everything in Python is an object, including classes.

# When you define the Person class, Python creates an object with the name Person. 
# The Person object has attributes. For example, you can find its name using the __name__ attribute:

print(Person.__name__)

# The Person object has the type of type:

print(type(Person))