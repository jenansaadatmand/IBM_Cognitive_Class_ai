# RegEx (Regular Expression) in Python is a tool for matching and handling strings:
# Built-in RegEx module, re, provides several functions, including search, split, findall, and sub

# Import RegEx module 
import re

# search() function searches for specified patterns within a string

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

print()
# Regular expressions (RegEx) are patterns used to match and manipulate strings of text. There are several special sequences in RegEx that can be used to match specific characters or patterns.
    
# Special sequence	    Meaning	        Example:
# \d	Matches any digit character (0-9)	"123" matches "\d\d\d"    

# \D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"

# \w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w"
    
# \W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
    
# \s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\s\w\w\w\w\w"
    
# \S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S"
    
# \b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"

# \B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"
    
# A simple example of using the <code>\d</code> special sequence in a regular expression pattern with Python code:
    
# The regular expression pattern is defined as r"\d\d\d\d\d\d\d\d\d\d", which uses the \d special sequence to match any digit character (0-9), and the \d sequence is repeated ten times to match ten consecutive digits
        
pattern = r"\d\d\d\d\d\d\d\d\d\d"
text = "My phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

print()

# A simple example of using the <code>\W</code> special sequence in a regular expression pattern with Python code:
# The regular expression pattern is defined as r"\W", which uses the \W special sequence to match any character that is not a word character (a-z, A-Z, 0-9, or _). The string we're searching for matches in is "Hello, world!"


pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)
print()

# The findall() function finds all occurrences of a specified pattern within a string.
s2  = "Michael Jackson was a singer and known as the 'King of Pop'"

# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)
print()

# A regular expression's split() function splits a string into an array of substrings based on a specified pattern.
# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)
# The split_array contains all the substrings, split by whhitespace characters
print(split_array)
print()

# The sub function (substitue) of a regular expression in Python is used to replace all occurrences of a pattern in a string with a specified replacement.

# Define the regular expression pattern to search for 
pattern = r"King of Pop"
# Define the replacement string
replacement = "legend"
# Use the sub function to replace the pattern with the replcacement string
new_string = re.sub(pattern, replacement, s2, flags = re.IGNORECASE)

# Print out the list of matched words
print(new_string)
print()

# Print out a  backslash:
print("\\")
print(r"\ ")
print("\n")
print("I \t am")
