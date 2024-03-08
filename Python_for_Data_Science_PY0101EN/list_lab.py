# List lab

#  A list is a sequence collection of different objects such as integers, strings, floats, and even other lists
# The address of each element within a list is called an index
# An index is used to access and refer to items within a list
# To create a list type the list within square brackets [ ], with your content inside the parenthesis and separated by commas

# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)  

# Use negative and regular indexing with a list
print(L[0])
print(L[0][0])
print(L[1])
print(L[-1])
print()

# Print the elements on each index
print('the same element using negative and positive indexing:\n Positive:', L[0], '\n Negative:', L[-3]) 
print('the same element using negative and positive indexing:\n Positive:', L[1], '\n Negative:', L[-2])
print('the same element using negative and positive indexing:\n Positive:', L[2], '\n Negative:', L[-1])

print()
# List content, strings, integers, floats, nested lists, nested tuples and other data structures
sample_list = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
print(sample_list)

# list operations
# Slicing in lists, if we want the last two elements
print(sample_list[3:])
print(sample_list[3:5])
print(sample_list[-2:])
print()
# slicing a new list
L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
print(L)
print(L[3:])
print(L[3:5])
print()

# We can use the .extend() method to add new elements to the list
L = ["Michael Jackson", 10.2]
L.extend(["pop", 10]) # use extend to add multiple elements pass a list into extend to add elements
print(L)
L.append("Toto") # append one element
print(L)
L.append(["Momo", 15]) # adding one element as a nested list
print(L) 
print()

# Each time we apply a method, the list changes
# Append the list ['a', 'b']
L.append(['a', 'b'])
print(L)
print()
# Lists are mutable, we can change them 
A =["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
print()


# Delete an element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)
print()

# converting a string to a list using split() method, the method split translates every group of characters separated by a space into an element in a list:
# Split the string, default is by space  
print('hard rock'.split())
# split the string on a specific character, which we call a delimiter. We pass the character we would like to split on into the argument, eg. comma. The result is a list
# Split the string by comma
print('A, B, C, D'.split())
print()

# Copy and clone list
# When we set one variable B equal to A, both A and B are refrencing the same list in memory
# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Initially, the value of the first element in B is set as "hard rock". If we change the first element in A to "banana", we get an unexpected side effect. As A and B are referencing the same list, if we change list A, then list B also changes. If we check the first element of B we get "banana" instead of "hard rock":
print('B[0]:', B[0])
A[0] = 'banana'
print('B[0]:', B[0])
print()

# Clone (clone by value) the list A
B = A[:] # clone list A by value from the begining to the end, here B is a new list 
print(B) # variable B references a new copy or clone of the original list
print()

# Now if we change A, B will not change
print('B[0]:', B[0])
A[0]= 'hard rock'
print('B[0]:', B[0])
print(A)
print(B)
print()

# Quiz:
# Creat a list a_list, with the following elements 1, hello, [1, 2, 3] and True
a_list = [1, "hello", [1, 2, 3], True]
print(a_list)

# Find the value stored at index 1 of a_list
print(a_list[1]) 

# Retrieve the elements stored at index 1, 2 and 3 of a_list
print(a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']
A = [1, 'a']
B = [2, 1, 'd']
print(A + B)
print()


