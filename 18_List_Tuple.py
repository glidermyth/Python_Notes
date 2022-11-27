# A list is an ordered collection of items.
# Python uses the square brackets ([]) to indicate a list.

fruits = ['apple','banana','grapes','orange']
numbers = [1,2,3,4,5]
print(fruits)

# A list can contains other lists. The following example defines a list of lists:
coordinates = [[0,0],[100,100],[200,200]]

# Since a list is an ordered collection, you can access its element by indexes like this:

# list[index]

# Lists are zero-based indexes. In other words, the first element has an index of 0, 
# the second element has an index of 1, and so on.

print(numbers[1])

# The negative index allows you to access elements starting from the end of the list.
print(numbers[-1])

# To change an element, you assign a new value to it using this syntax:
# list[index] = new_value

numbers[0] = 7

# The append() method appends an element to the end of a list.

numbers.append(9)
print(numbers)

# The del statement allows you to remove an element from a list by specifying the position of the element.
del numbers[0]
print(numbers)

# The pop() method removes the last element from a list and returns that element
# Typically, you use the pop() method when you want to remove an element 
# from a list and still want to access the value of that element.

second = numbers.pop(1)
print(second)

# To remove an element by value, you use the remove() method.
# For example, the following removes the element with value 9 from the numbers list.
print(numbers)
numbers.remove(9)
print(numbers)


##### Python tuples #####
# Sometimes, you want to create a list of items that cannot be changed throughout the program. 
# Tuples allow you to do that.

# A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. 
# So by definition, a tuple is an immutable list.

# Defining a tuple :
# A tuple is like a list except that it uses parentheses () instead of square brackets [].

rgb = ('red','green','blue')

# Once defining a tuple, you can access an individual element by its index.
print(rgb[1])

# To define a tuple with one element, you need to include a trailing comma after the first element.
num = (3,)
print(type(num))
# If you exclude the trailing comma, the type of the numbers will be int.


##### To sort a list, you use the sort() method: #####

# list.sort()

# The sort() method sorts the original list in place. 
# It means that the sort() method modifies the order of elements in the list.

# By default, the sort() method sorts the elements of a list using the less-than operator (<). 
# In other words, it places the lower elements before the higher ones.

# To sort elements from higher to lower, you pass the reverse=True argument to the sort()


# The sort() method sorts a list in place. In other words, it changes the order of elements in the original list.
# To return the new sorted list from the original list, you use the sorted() function:

# sorted(list)

# The sorted() function doesn’t modify the original list.

# By default, the sorted() function sorts the elements of the list from lowest to highest using 
# the less-than operator (<).
# If you want to reverse the sort order, you pass the reverse argument as True like this:

# sorted(list,reverse=True)


# Lists support the slice notation that allows you to get a sublist from a list:

# sub_list = list[begin: end: step]

# In this syntax, the begin, end, and step arguments must be valid indexes. 
# And they’re all optional.
# The begin index defaults to zero. The end index defaults to the length of the list. 
# And the step index defaults to 1.

numbers = [1,2,3,4,5,6,7,8,9]
new_list = numbers[1:5]
print(new_list)
new_list = numbers[::2] # selecting all the elements but using step 2
print(new_list)


##### Unpacking a list #####
colors = ['red', 'blue', 'green']
# Basically, you can assign elements of a list (and also a tuple) to multiple variables. For example:

red, blue, green = colors

# This statement assigns the first, second, and third elements of the colors list to the 
# red, blue, and green variables.

# In this example, the number of variables on the left side is the same as the 
# number of elements in the list on the right side.
# If you use a fewer number of variables on the left side, you’ll get an error.

# If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

# First, unpack the needed elements to variables.
# Second, pack the leftover elements into a new list and assign it to another variable.
# By putting the asterisk (*) in front of a variable name, 
# you’ll pack the leftover elements into a list and assign them to a variable. For example:

red, blue, *other = colors

print(red)
print(blue)
print(other)


##### Python for loop to iterate over a list #####

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

# Sometimes, you may want to access indexes of elements inside the loop. 
# In these cases, you can use the enumerate() function.
# The enumerate() function returns a tuple that contains the current index and element of the list.

for item in enumerate(cities) :
    print(item)

# To find the index of an element in a list, you use the index() function.
result = cities.index('Mumbai')
print(result)


# In Python, an iterable is an object that includes zero, one, or many elements. 
# An iterable has the ability to return its elements one at a time.
# Because of this feature, you can use a for loop to iterate over an iterable.

# An iterable can be iterated over. And an iterator is the agent that performs the iteration.
# To get an iterator from an iterable, you use the iter() function. For example:

colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

# Once you have the iterator, you can get the next element from the iterable using the next() function:

color = next(colors_iter)
print(color)



# Python list comprehensions
# In programming, you often need to transform elements of a list and return a new list.

numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)

# A list comprehension consists of the following parts:

# An input list (numbers)
# A variable that represents the elements of the list (number)
# An output expression (number**2) that returns the elements of the output list from the elements of the input list.
# The following shows the basic syntax of the Python list comprehension:

# [output_expression for element in list]

# Python List comprehensions provide an optional predicate that allows you to specify 
# a condition for the list elements to be included in the new list:

# [output_expression for element in list if condition]

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1] > 8600]

print(highest_mountains)