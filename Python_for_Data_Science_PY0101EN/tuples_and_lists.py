# Compound data types: Tuples and lists 
# Tuples are ordered sequence, immutable, written as comma-separated elements within parentheses
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
print(Ratings)
# tuples can contain string, int, and float 

print(type(Ratings))
tuples = ("disco", 10, 1.2)
print(tuples)
print()

# Each element in a tuple can be accessed via an index
print(tuples[0])
print(tuples[1])
print(tuples[2])
print()

print(tuples[-1])
print(tuples[-2])
print(tuples[-3])
print()

# Concatenating tuples by adding them using the operator (+)
tuples2 = tuples + ("hard rock", 10) 
print(tuples2)
print()

#Accessing items within tuples via index number
print(tuples2[-1])

# Slicing tuples to retrieve a portion of tuples
print(tuples2[0:3]) # not including index 3, the last index is one larger than the index you want

# Accessing the last two elements using slicing
print("This is the last two elements",tuples2[3: 5]) 
print()

# to obtain the length of the tuple 
print(len(tuples2))
print()

# Tuples are immutable (we cannot change it)
Ratings1 = Ratings 
print(Ratings1)

# As a consequence of immutability, if we would like to manipulate a tuple, we must create a new tuple instead

# Creating a new tuple, we can assign a different tuple to Ratings tuple
Ratings = (2, 10, 1)
print(Ratings)
print()

# To sort a tuple we use sorted() function
RatingsSorted = sorted(Ratings)
print(RatingsSorted) # input original tuple, the output is a sorted tuple
print()
# A tuple can contain other tuples, Nesting tuples

NT = (1,2, ("pop", "rock"), (3, 4), ("disco", (1,2)))
print(NT) 
# Accessing items within nested tuples using index
print(NT[0])
print(NT[2])
print(NT[3])
print(NT[-1])
print()
# If we select an index with a tuple, the same index convention applies.
print(("pop", "rock")[1])
print(NT[2][1]) # accessing the second element within the tuple that is within the NT tuple
print(NT[2][0]) # accessing the first element within the tuple that is within the NT tuple
print()

print(NT[3][0])
print(NT[-1][1])

# We can access different characters within the tuples
print(NT[2][1][0]) # accessing the first letter
print(NT[2][1][3]) # accessing the fourth letter
print()

# Lists: are ordered sequence, represented with square bracket, lists are mutable 
# Lists can contain strings, integers, and floats
L = ["Michael Jackson", 10.1, 1982]
# lists can be nested in other lists  
L1 = ["Michael Jackson", 10.1, 1982, [1, 2], ['A', 1]]
print(L1)
# nesting a tuple in a list
L1 = ["Michael Jackson", 10.1, 1982, [1, 2], ('A', 1), ('pop', 'rock')]
print(L1)
# Each element can be accessed via the index
print(L[0])
print(L[1])
print(L[2])
print(L[-1])
print(L[-2])
print(L[-3])
print()
print(L[0][-1])
print(L1[-1])  
print(L1[-1][0][2])
print()

# Slicing in lists to retrieve a portion of a list
L =["Michael JAckson", 10.1, 1982, "MJ", 1]
print(L[3:5]) # not including index 5, last index is one larger than the length of the list

# Concatenate or combine lists by ading them using the operator (+)
# Here we creat a new list by adding another list
L1 = L + ["pop", 10]
print(L1)
print()

# Lists are mutable, therfore, we can change them 
# Everytime we apply a method the list changes
# .extend(new list) method to concatenate lists
# Here we create a nw list using the .extend() method, you can more than one element or a list to a list
L.extend(["pop", 10]) 
print(L)

# you can add only one item using .append() method
L.append("Toto")
print(L)
L.append(['blob', 100]) # appending a list to a list
print(L)
print()

# Changing elements within a list using its index
A = ["disco", 10, 1.2]
A[0] = 'hard rock'
print(A)
# Deleting an item from a list using del()
del(A[0])
print(A)
del(A[1])
print(A)
print()

# Converting a string to a list using .split() method, separates every group of characters separated by a space into an element of a list 
a = "hard rock".split()
print(a)

# use the split() function to separate strings on a specific character known as a delimiter 
# pass the delimiter we want to split on as an rgument, in this case a comma

print("A, B, C, D".split(",")) 


# Multiple names referring to the same object is known as aliasing, if A and B refrencing the same list, then if zou change one the other list changes
a = ["banana", 10, 1.2]
b = a # creating an alias list, not a clone, i.e. both a and b refering to the same list, so changing one list will lead to side effect on chaning the other list 
print(a)
print(b)
b[0] = "hard rock"
print(b[0])
print(a[0])
print(a)
print(b)
print()


# Cloning lists
A = ["hard rock", 10, 1.2]
B = A[:] # clone list a from begining index to end index
print(B) # refrences a new clone or copy of list a
print()


# In this case: if you change a, b will not change
A[0] = 'banana'
print(A)
print(B) # list B does not change
print()


# get help on list, tuples in python by passing the list in the help() function
# help(A) # class list iterable, mutable sequence

A = (0, 1, 2, 3)
print(A[-1])
print(A[3])
print()

B = ["a", "b", "c"]
print(B[1:])
