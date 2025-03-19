sentence = "the dog is named Sammy"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a')) 

# Consider the variable <code>d</code> use slicing to print out the first three elements:
d = "ABCDEFG"
print(d[:3]) 
# or 
print(d[0:3])

# Slicing
Letters="ABCDEFGHIJK"
print(Letters[0:4]) # ABCD

# Use a stride value of 2 on the following string :
Good="GsoAo+d"
print(Good[::2]) # Good

e = 'clocrkr1e1c1t'
print(e[::2])

# Uppercase
print("uppercase".upper())

name ="Michael Jackson" 
print (len(name))

# Take the slice on variable name with only index 0 to index 3
print (name[0:4]) # Mich

# Take the slice on variable name with only index 8 to index 11
print (name[8:12]) # Jack

# Get every second element. The elments on index 1, 3, 5 ...
print (name[::2]) # McalJcsn

# Get every second element in the range from index 0 to index 4
print (name[0:5:2]) # Mca

# Concatenate two strings
statement = name + "is the best"
print (statement)

# Print the string for 3 times
print (3 * "Michael Jackson")

# New line escape sequence
print(" Michael Jackson \n is the best" )

# Tab escape sequence
print(" Michael Jackson \t is the best" )

# Include back slash in string
print(" Michael Jackson \\ is the best" )

# We can also place an "r" before the string to display the backslash:
# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )

a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print (b)

# Replace the old substring with the new target substring by removing some punctuations.
a = "Hello! Michael Jackson has: 12 characters."
print(a)
b = a.replace('!','').replace(':','').replace('.','')
print(b)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
print ( name.find('el') )

# Find the substring in the string.
print ( name.find('Jack') )

# If cannot find the substring in the string
print ( name.find('Jasdfasdasdf') )

# The method <code>Split</code> splits the string at the specified separator, and returns a list:
#Split the substring into list
name = "Michael Jackson"
split_string = name.split()
print (split_string)
name = "Michael,Jackson"
split_string = name.split(",")
print (split_string)