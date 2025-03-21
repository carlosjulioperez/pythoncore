# Set = Conjunto

# Cast the following list to a set:
print(['A','B','C','A','B','C'])
print(set(['A','B','C','A','B','C']))
# ['A', 'B', 'C', 'A', 'B', 'C']
# Set hasn't permit duplicates
# {'C', 'B', 'A'}

# Add the string 'D' to the set S.
S={'A','B','C'}
S.add('D')
print(S)
# {'D', 'B', 'C', 'A'}

# Find the intersection of set A and B.
A={1,2,3,4,5}
B={1,3,9, 12}
print(A & B)
# set([1, 3])
# or
print(A.intersection(B))
# set([1, 3])

# Find the difference in set1 but not set2
print(A.difference(B))

A = set(["Thriller", "Back in Black", "AC/DC"])
A.add("NSYNC")
print(A)

# Remove the element from set
A.remove("NSYNC")
print(A)

# Verify if the element is in the set
print("AC/DC" in A)
# True