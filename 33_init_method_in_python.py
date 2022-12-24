#----- Introduction to the Python __init__() method -----#

# When you create a new object of a class, Python automatically calls the __init__() method to initialize the object’s attributes.
# Unlike regular methods, the __init__() method has two underscores (__) on each side. Therefore, the __init__() is often called dunder init. 
# The name comes abbreviation of the double underscores init.
# The double underscores at both sides of the __init__() method indicate that Python will use the method internally. 
# In other words, you should not explicitly call this method.

# Since Python will automatically call the __init__() method immediately after creating a new object, 
# you can use the __init__() method to initialize the object’s attributes.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showInfo(self):
        print(f"Name : {self.name} and age : {self.age}")


person = Person('Glider',22)
person.showInfo()

# When you create an instance of the Person class, Python performs two things:

# First, create a new instance of the Person class by setting the object’s namespace such as __dict__ attribute to empty ({}).
# Second, call the __init__ method to initialize the attributes of the newly created object.

# Note that the __init__ method doesn’t create the object but only initializes the object’s attributes. 
# Hence, the __init__() is not a constructor.
