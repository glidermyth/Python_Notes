#----- Introduction to the Python class variables -----#
# Everything in Python is an object including a class. In other words, a class is an object in Python.

# When you define a class using the class keyword, Python creates an object with the name the same as the class’s name. For example:

# class HTMLDocument:
#     pass

# This example defines the HtmlDocument class and the HtmlDocument object. The HtmlDocument object has the __name__ property:

# print(HTMLDocument.__name__)

# It’s also an instance of the type class:

# print(isinstance(HTMLDocument, type))

# Class variables are bound to the class. They’re shared by all instances of that class.
# The following example adds the extension and version class variables to the HtmlDocument class

# class HTMLDocument:

#     extension = 'html'
#     version = 5


#----- Get the values of class variables -----#
# To get the values of class variables, you use the dot notation (.). For example

# print(HTMLDocument.extension)
# print(HTMLDocument.version)

# Another way to get the value of a class variable is to use the getattr() function. 
# The getattr() function accepts an object and a variable name. It returns the value of the class variable. For example:

# extension = getattr(HtmlDocument, 'extension')
# version = getattr(HtmlDocument, 'version')

# print(extension)  # html
# print(version)  # 5

# If the class variable doesn’t exist, you’ll also get an AttributeError exception. 
# To avoid the exception, you can specify a default value if the class variable doesn’t exist like this:

# media_type = getattr(HtmlDocument, 'media_type', 'text/html')
# print(media_type) # text/html

#----- Set values for class variables -----#
# To set a value for a class variable, you use the dot notation:

# HtmlDocument.version = 10

# or you can use the setattr() built-in function:

# setattr(HtmlDocument, 'version', 10)

# Since Python is a dynamic language, you can add a class variable to a class at runtime after you have created it. 
# For example, the following adds the media_type class variable to the HtmlDocument class:

# HtmlDocument.media_type = 'text/html'
# print(HtmlDocument.media_type)

# Similarly, you can use the setattr() function:

# setattr(HtmlDocument, media_type, 'text/html')
# print(HtmlDocument.media_type)

#----- Delete class variables -----#
# To delete a class variable at runtime, you use the delattr() function:

# delattr(HtmlDocument, 'version')

# Or you can use the del keyword:

# del HtmlDocument.version


#----- Class variable storage -----#
# Python stores class variables in the __dict__ attribute. 
# The __dict__ is a mapping proxy, which is a dictionary. For example:

# print(HTMLDocument.__dict__)


#----- Callable class attributes -----#
# Class attributes can be any object such as a function.

# When you add a function to a class, the function becomes a class attribute. 
# Since a function is callable, the class attribute is called a callable class attribute. For example:

class HtmlDocument:

    extension = 'html'
    version = 5

    def render(self):
        print("rendering the html pagr ...")

print(HtmlDocument.__dict__)