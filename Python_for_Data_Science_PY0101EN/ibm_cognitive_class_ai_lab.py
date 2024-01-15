# IBM cognitive class AI
# Objectives: After completing this lab you will be able to:

# * Write basic code in Python
# * Work with various types of data in Python
# * Convert the data from one type to another
# * Use expressions and variables to perform operations

# Tasks:
# 1. Say "Hello" to the world in Python. print() is a function. You passed the string 'Hello, Python!' as an argument to instruct Python on what to print.
# 2. What version of Python are we using?
# 3. Writing comments in Python
# 4. Errors in Python
# 5. Does Python know about your error before it runs your code?
# 6. Exercise: Your First Program
# 7. Types of objects in Python
# 8. Integers
# 9. Floats
# 10. Converting from one object type to a different object type
# 11. Boolean data type
# 12. Exercise: Types
# 13. Expressions and Variables
# 14. Expressions
# 15. Exercise: Expressions
# 16. Variables
# 17. Exercise: Expression and Variables in Python



# Answers: 

print("1. Say Hello to the world in Python")
print('Hello World') # know how to print a string in output and how to execute code within cells in a notebook.

print("2. check python version") # sys is a built-in module that contains many system-specific parameters and functions, including the Python version in use. Before using it, we must explictly import it.
import sys
print(sys.version)

print("3. writing comments in python") # Python will ignore everything past the # on a given line.
print('Hello World') # This line prints a string
print("4. error in python. print string as error message")
#print("Hello, Python"

print("5. Does Python know about your error before it runs your code?")

#print string and error to see the running order
#print("This will be printed") 
#frint("This will cause error")
#print("This will NOT be printed")

print("6. Exercise: Your First Program")
print("Hello World!") 

print("7. Types of objects in Python")

# Type of objects in Python. Python is an interpreted object-oriented language 
print("object types, data structures: strings, integers, floats, list, tuples, dictionary, sets, arrays")

# strings(str): collection of chracters, words. strings can be represented with single quotes ('1.2') or double quotes ("1.2"), but you can't mix both (e.g., "1.2')
# integers(int):whole numbers, positive & negative
# float: decimal (real) numbers, positive and negative
print("type() function to check the class of the data type")

print("8. Integers:")
print(type(11))
print(type(-11))
print(type(0))

print("9. Floats")
print(type(2.14))
print(type(-2.14))
print("a string:")
type("Hello, Python 101!")
print()

# Floats represent real numbers; they are a superset of integer numbers but also include "numbers with decimals". 

print(" There are some limitations when it comes to machines representing real numbers, but floating point numbers are a good representation in most cases. You can learn more about the specifics of floats for your runtime environment, by checking the value of sys.float_info after importing sys module. This will also tell you what's the largest and smallest number that can be represented with them")
    

print(sys.float_info)

print("10. Converting from one object type to a different object type. This is called typecasting or i.e. changing object type") 

print(type(2))
print("converting/type cast integers to floats, and checking its type at the sametime")

print(type(int(2)))

# When we convert an integer into a float, we don't change the value (i.e., the significand) of the number. However, if we cast a float into an integer, we could potentially lose some information. For example, if we cast the float 1.1 to integer we will get 1 and lose the decimal information (i.e., 0.1):

print("casting float to integer and lose information")
# For example, if we cast the float 1.1 to integer we will get 1 and lose the decimal information (i.e., 0.1):
print(int(1.1)) 

print("Converting from string to integers or floats")
# if we have a string that contains a number within it. we can cast that string into an integer
print(int('1'))

# if we try to do the so with a string we will get an error.
#print(int('1 or 2 people'))
# you will get ValueError: invalid literal for int() with base 10: '1 or 2 people'

print("Converting strings containing") # floating point into float objects
print(float('1.2'))

print("converting numbers into strings")

print(str(1))
print(str(1.2))
print()

print("11. Boolean data type, an object of type Boolean can take one of two values: True or False")
# Notice that the value True has an uppercase "T". The same is true for False (i.e. you must use the uppercase "F").

print(True)
print(False)

print("When you ask Python to display the type of a boolean object it will show bool which stands for boolean")

print(type(True))
print(type(False))
print()


print("casting bool to int or float:")
print("convert True to int and False to int:")
print(int(True))
print(int(False))

print("convert True to float and False to float:)")
print(float(True))
print(float(False))
print()

print("casting int to bool:")
print("convert 1 into True and 0 into False:")
print(bool(1))
print(bool(0))
print()

print("12. Exercise: Types")

print("What is the data type of the result of: 6/2, remember division always results in floating point")
print(type(6/2))

print("What is the type of the result of: 6 // 2? (Note the double slash //")

print(type(6//2)) # int, as the double slashes stand for integer division 
print()

print("13. Expressions and Variables")
# Expressions in Python can include operations among compatible types (e.g., integers and floats). For example, basic arithmetic operations like adding multiple numbers:
print("Addition operation expression")
print("43 + 60 + 16 + 41")
print("# Subtraction operation expression")
print("50-60")
print("We can do multiplication using an asterisk:")
print("5*5")
print("We can also perform division with the forward slash:")
print("25/5")
print("25/6")
print()
print("we can use the double slash // for integer division, where the result is rounded down to the nearest integer:")
print("Integer division operation expression")
print("25//5")
print("25//6")
print()

print("14. Expressions")
print("Let's write an expression that calculates how many hours there are in 160 minutes:")

print("160/60")
print()

print("# 15. Exercise: Expressions")
print("mathematical expression, evaluating parenthesis first:")
print("30 + 2 + 60")
print("(30 + 2) * 60")
print()

print("16. variables: placeholders for values to be used later on in the program:")
print("x = 43 + 60 + 16 + 41")
x = 43 + 60 + 16 + 41
print(x)
print("y = x/60")
y = x/60
print(y)
print()
print("If we save a value to an existing variable, the new value will overwrite the previous value:")
print("x = x / 60")
x = x/60
print(x) # x was 160 and now x is reassigned to 2.6666666666666665

print()
print("# Name the variables meaningfully")
total_min = 43 + 42 + 57 # Total length of albums in minutes
print(total_min)

print("#name the variables meaningfully:")
total_hours = total_min / 60 # Total length og albums in hours

print("# complicate expression:")
total_hours = (43 + 42 + 57) / 60 # Total hours in a single expression
print(total_hours)

print("If you'd rather have total hours as an integer, you can of course replace the floating point division with integer division (i.e., //)")

print("43 + 42 + 57) // 60")
total_hours = (43 + 42 + 57) // 60 # value = 2 instead of 2.66666
print(total_hours)
print()

print("# 17. Exercise: Expression and Variables in Python")

print("What is the value of x where x = 3 + 2 * 2")
x = 3 + 2 * 2
print(x)
print("What is the value of y where y = (3 + 2) * 2?")
y = (3 + 3) * 2
print(y)

print("What is the value of z where z = x + y?")
z = x + y
print(z)
