# To define a class, you use the class keyword followed by the class name.
# class Person:
#     pass

# To create an object from the Person class, you use the class name followed by parentheses (), like calling a function:
# pobj = Person()

# Python is dynamic. It means that you can add an attribute to an instance of a class dynamically at runtime.
# For example, the following adds the name attribute to the person object:

# pobj.name = 'Glider'

# To define and initialize an attribute for all instances of a class, you use the __init__ method. 
# The following defines the Person class with two instance attributes name and age:

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# When you create a Person object, Python automatically calls the __init__ method to initialize the instance attributes. 
# In the __init__ method, the self is the instance of the Person class.

# person = Person('Lenovo',1)

# Define instance methods
# The following adds an instance method called greet() to the Person class

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello Mr. {self.name}"

# person = Person('Lenovo',1)
# print(person.greet())

# Define class attributes
# Unlike instance attributes, class attributes are shared by all instances of the class. 
# They are helpful if you want to define class constants or variables that keep track of the number of instances of a class.

# class Person:

#     counter = 0

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello Mr. {self.name}"

# person = Person('Lenovo',1)
# print(person.greet())
# You can access the counter attribute from the Person class:
# print(Person.counter)
# Or from any instances of the Person class:
# print(person.counter)

# Define class method
# Like a class attribute, a class method is shared by all instances of the class. 
# The first argument of a class method is the class itself. By convention, its name is cls. 
# Python automatically passes this argument to the class method. 
# Also, you use the @classmethod decorator to decorate a class method.

# class Person:

#     counter = 0

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Person.counter += 1

#     def greet(self):
#         return f"Hello Mr. {self.name}"

#     @classmethod
#     def show_counter(cls):
#         return cls.counter


# person = Person('Lenovo',1)
# print(Person.show_counter())


# Define static method
# A static method is not bound to a class or any instances of the class. 
# In Python, you use static methods to group logically related functions in a class. 
# To define a static method, you use the @staticmethod decorator.

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return 9 * c / 5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return 5 * (f - 32) / 9

# To call a static method, you use the ClassName.static_method_name() syntax. For example:

# f = TemperatureConverter.celsius_to_fahrenheit(30)
# print(f)  # 86

# Notice that Python doesn’t implicitly pass an instance (self) as well as class (cls) as the first argument of a static method.



# Single inheritance
# A class can reuse another class by inheriting it. When a child class inherits from a parent class, the child class can access the attributes and methods of the parent class.

# For example, you can define an Employee class that inherits from the Person class:

# class Employee(Person):
#     def __init__(self, name, age, job_title):
#         super().__init__(name, age)
#         self.job_title = job_title

# Inside the __init__ method of the Employee class calls the __init__method of the Person class to initialize the name and age attributes. 
# The super() allows a child class to access a method of the parent class.

# The Employee class extends the Person class by adding one more attribute called job_title.

# The Person is the parent class while the Employee is a child class. 
# To override the greet() method in the Person class, you can define the greet() method in the Employee class as follows:

# class Employee(Person):
#     def __init__(self, name, age, job_title):
#         super().__init__(name, age)
#         self.job_title = job_title

#     def greet(self):
#         return super().greet() + f" I'm a {self.job_title}."

# The greet() method in the Employee is also called the greet() method of the Person class. 
# In other words, it delegates to a method of the parent class.

# The following creates a new instance of the Employee class and call the greet() method:

# employee = Employee('John', 25, 'Python Developer')
# print(employee.greet())