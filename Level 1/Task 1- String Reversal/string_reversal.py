def reversed_string(string):
    # Return the reversed string using slicing
    return string[::-1]


str = input("Enter the string: ")

# Call the function to reverse the string
rev_str = reversed_string(str)

# Print the reversed string
print(rev_str)
