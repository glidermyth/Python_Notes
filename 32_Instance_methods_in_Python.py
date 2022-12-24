#----- Introduction to the Python methods -----#
# By definition, a method is a function that is bound to an instance of a class. 

# The following defines a Request class that contains a function send():

# class Request:
    
#     def send():
#         print("send")

# Request.send()

# The send() is a function object, which is an instance of the function class.

# print(Request.send)

# request = Request()
# If you display the request.send, it’ll return a bound method object:

# print(request.send)

# So the http_request.send is not a function like Request.send. 
# The following checks if the Request.send is the same object as http_request.send. 
# It’ll returns False as expected:

# print(type(request.send) is type(Request.send))

# print(type(Request.send))
# print(type(request.send))

# So when you define a function inside a class, it’s purely a function. 
# However, when you access that function via an object, the function becomes a method.

# Therefore, a method is a function that is bound to an instance of a class.

# If you call the send() function via the http_request object, you’ll get a TypeError as follows

# http_request.send()

# Error:
# TypeError: send() takes 0 positional arguments but 1 was given

# Because the http_request.send is a method that is bound to the http_request object, 
# Python always implicitly passes the object to the method as the first argument.


class Request:

    def send(self):
        print(self)

req = Request()

print(req)
req.send()

# The req object is the same as the one Python passes to the send() method as the first argument because they have the same memory address. 