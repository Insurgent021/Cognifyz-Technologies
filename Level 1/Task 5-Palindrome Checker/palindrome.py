def palindrome_check(string):
    # Reverse the input string
    reversed_str = string[::-1]
    
    # Check if the reversed string is equal to the original string
    if reversed_str == string:
        print(f"The string '{string}' is a palindrome.")
    else:
        print(f"The string '{string}' is not a palindrome.")


str = input("Enter the string: ")

# Call the function to check if the string is a palindrome
palindrome_check(str)
