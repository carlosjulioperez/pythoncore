# Create your first tuple
tuple1 = ("disco",10,1.2 )
print(tuple1)
print(type(tuple1))

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Use negative index to get the value of the last element
print(tuple1[-1])

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

# Slice from index 0 to index 2
print(tuple2[0:3])

# We can obtain the last two elements of the tuple:
# Slice from index 3 to index 4
print(tuple2[3:5])

# Get the length of tuple
print(len(tuple2))

# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

# Create a nest tuple
NestedT = (1, 2, ("pop", "rock"), (3,4), ("disco", (1,2)))
print(NestedT) 

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])
# Element 0 of Tuple:  1
# Element 1 of Tuple:  2
# Element 2 of Tuple:  ('pop', 'rock')
# Element 3 of Tuple:  (3, 4)
# Element 4 of Tuple:  ('disco', (1, 2))

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ", NestedT[2][0])
print("Element 2, 1 of Tuple: ", NestedT[2][1])
print("Element 3, 0 of Tuple: ", NestedT[3][0])
print("Element 3, 1 of Tuple: ", NestedT[3][1])
print("Element 4, 0 of Tuple: ", NestedT[4][0])
print("Element 4, 1 of Tuple: ", NestedT[4][1])
# Element 2, 0 of Tuple:  pop
# Element 2, 1 of Tuple:  rock
# Element 3, 0 of Tuple:  3
# Element 3, 1 of Tuple:  4
# Element 4, 0 of Tuple:  disco
# Element 4, 1 of Tuple:  (1, 2)

# Print the first element in the second nested tuples
print(NestedT[2][1][0]) #r
# Print the second element in the second nested tuples
print(NestedT[2][1][1]) #o

# Similarly, we can access elements nested deeper in the tree with a third index:
# Print the first element in the second nested tuples
print(NestedT[4][1][0]) #1
# Print the second element in the second nested tuples
print(NestedT[4][1][1]) #2


# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
print(genres_tuple)

# Find the length of the tuple, <code>genres_tuple</code>:
print(len(genres_tuple))

# Find the first index of "disco"
print(genres_tuple.index("disco"))

# Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):
C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
print(C_list)