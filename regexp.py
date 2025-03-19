# Python provides a built-in module called <code>re</code>, which allows you to work with regular expressions. 
import re

s1 = "Michael Jackson is the best"

# Define the patterm to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

pattern = r"\d\d\d\d\d\d\d\d\d\d" # Matches any ten consecutive digits
text = "My Phone number is 1234467890"
match = re.search(pattern, text)

if match:
    print("Phone number found: ", match.group())
else:
    print("No match")

pattern = r"\W" # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)
print("Matches: ", matches)

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"
# Use the findall() function to find all ocurrences of the "as" in the stering
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)

# Define the regular expression pattern to search for
pattern = r"king of pop"

# Define the replacement string
replacement = "legend"

# use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string)