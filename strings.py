# Examples of working with Strings

# String variables we will work with
s1 = 'abc'
s2 = '123'
s3 = 'ABC'
string_to_split = "We can split this sentence into a list of new strings."

# Concatenation using '+' operator
s4 = s1 + s2

print("="*50)
print("Concatenating s1 and s2: ")
print("="*50)
print("-->" + s4)

# Return an uppercase version of s1
print("="*50)
print("Uppercase s1: ")
print("="*50)
print("-->" + s1.upper())

# Return a lowercase version of s3
print("="*50)
print("Lowercase s3: ")
print("="*50)
print("-->" + s3.lower())

# Notice how the original variable has not changed
print("="*50)
print("Original variable s1 is still lowercase: ")
print("="*50)
print("-->" + s1)
print("="*50)
print("Original variable s3 is still uppercase: ")
print("="*50)
print("-->" + s3)

# .split method
split_string = string_to_split.split()
print("="*50)
print("We can split the string up: ")
print("="*50)
print(split_string)

# Access the individual strings using indexing.
print("="*50)
print("Then print the string at index 0: ")
print("="*50)
print(split_string[0])

print("="*50)
print("The string at index 1: ")
print("="*50)
print(split_string[1])

print("="*50)
print("The string at index 2: ")
print("="*50)
print(split_string[2])

# Use a for loop to print them all
print("="*50)
print("Printing the list of strings using a for loop: ")
print("="*50)
for string in split_string:
    print string

