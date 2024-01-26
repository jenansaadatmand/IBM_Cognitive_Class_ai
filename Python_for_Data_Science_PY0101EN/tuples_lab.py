# Tuples lab
# Creating a tuple
tuple1 = ("disco", 10, 1.2)
print(tuple1)
# type of variable tuple
print(type(tuple1))
print()


# Indexing 
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[-1]) # use the negative index to print the last element in the tuple
# display the next two elements using a negative index
print(tuple1[-2]) # second last element
print(tuple1[-3]) # third last element
print()

# printing the type of each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print(type(tuple1[-1]))
print(type(tuple1[-2]))
print(type(tuple1[-3]))
print()

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)
print()

# slice a tuple to retrieve a portion of it
print(tuple2[0:3]) # result in tuple1
print(tuple2[3:]) # result in ("hard rock", 10), obtain the last two elements

# Obtain the length of the tuple
print(len(tuple2))

# sorting
Ratings = (0, 9,6,5,10, 8, 9, 6,2)
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

# Nested tuple, create a nest tuple
NestedT = (1, 2, ("pop", "rock"), (3,4), ("disco", (1,2)))
print(NestedT)
print()

# Print element on each index
print("Element 0 of Tuple:", NestedT[0])
print("Element 1 of Tuple:", NestedT[1])
print("Element 2 of Tuple:", NestedT[2])
print("Element 3 of Tuples:", NestedT[3])
print("Element 4 of Tuple:", NestedT[4])
print()

# Use the second index to access other tuples. Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ", NestedT[2][0])
print("Element 2, 1 of Tuple: ", NestedT[2][1])
print("Element 3, 0 of Tuple: ", NestedT[3][0])
print("Element 3, 1 of Tuple: ", NestedT[3][1])
print("Element 4, 0 of Tuple: ", NestedT[4][0])
print("Element 4, 1 of Tuple: ", NestedT[4][1])
print()
# Access strings in the second nested tuples using a third index
print("Element 4, 1, 0 of Tuple: ", NestedT[4][1][0])
print()

# Print the first element in the second nested tuples
print(NestedT[2][1][0])
print(NestedT[2][1][1])
print(NestedT[4][1][0])
print(NestedT[4][1][1])
print()

# Quiz:
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(genres_tuple)
print()

# Find the length of the tuple
print(len(genres_tuple))

# Access the element, with respect to index 3:
print(genres_tuple[3])

# Use slicing to obtain indexes 3, 4 and 5
print(genres_tuple[3:6]) # not including 6
print()

# Find the first two elements of the tuple genres_tuple
print(genres_tuple[0:2]) # Not including 2

# find the first index of "disco"
print(genres_tuple[-1][0])
print(genres_tuple[7][0])
print(genres_tuple.index("disco"))
print()


# Generate a sorted list from the Tuple C_tuples 
C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
print(C_list)







