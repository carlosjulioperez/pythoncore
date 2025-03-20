# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)

# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

# Sample List
L = ["Michael Jackson", 10.1,1982,"MJ",1]
# List slicing
print(L[3:5])

# We can use the method extend to add new elements to the list:
# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)

# As lists are mutable, we can change them. For example, we can change the first element as follows
# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
# Before change: ['disco', 10, 1.2]
# After change: ['hard rock', 10, 1.2]

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)
# Before change: ['hard rock', 10, 1.2]
# After change: [10, 1.2]

# Split the string, default is by space
print('hard rock'.split())

# Split the string by comma
print('A,B,C,D'.split(','))

# When we set one variable B equal to A, both A and B are referencing the same list in memory:
# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Initially, the value of the first element in B is set as "hard rock". If we change the first element in A to "banana", we get an unexpected side effect. As A and B are referencing the same list, if we change list A, then list B also changes. If we check the first element of B we get "banana" instead of "hard rock":
# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])
# B[0]: hard rock
# B[0]: banana

# You can clone list A by using the following syntax
# # Clone (clone by value) the list A
B = A[:]
print(B)
# ['banana', 10, 1.2]

# Variable B references a new copy or clone of the original list.
# Now if you change A, B will not change:
print('B[0]:', B[0])
A[0] = "hard rock"
print(A)
print(B)