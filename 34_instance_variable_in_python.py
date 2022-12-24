# In Python, class variables are bound to a class while instance variables are bound to a specific instance of a class. 
# The instance variables are also called instance attributes.

class HtmlDocument:
    extension = 'html'
    version = 5

print(HtmlDocument.__dict__)
# The HtmlDocument class has two class variables: extension and version. Python stores these two variables in the __dict__ attribute.

html = HtmlDocument()
print(html.__dict__)
# The html is an instance of the HtmlDocument class. It has its own __dict__ attribute:
# The html.__dict__ is now empty

# The html.__dict__ stores the instance variables of the home object 
# like the HtmlDocument.__dict__ stores the class variables of the HtmlDocument class.

# Unlike the __dict__ attribute of a class, the type of the __dict__ attribute of an instance is a dictionary.
print(type(html.__dict__))

# Python looks up the variables extension and version in html.__dict__ first. 
# If it doesn’t find them there, it’ll go up to the class and look up in the HtmlDocument.__dict__.

# However, if Python can find the variables in the __dict__ of the instance, it won’t look further in the __dict__ of the class.