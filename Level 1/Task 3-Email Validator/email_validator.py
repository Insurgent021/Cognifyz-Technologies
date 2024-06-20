def is_valid_email(email):
    # Check if "@" symbol appears exactly once in the email
    if email.count("@") != 1:
        return False

    # Split the email into username and domain parts
    username, domain = email.split("@")

    # Check if username and domain are not empty
    if not username or not domain:
        return False

    # Check if domain contains a dot (.)
    if "." not in domain:
        return False

    # Check if the domain part ends with a valid top-level domain
    if domain.rsplit(".", 1)[-1] == "":
        return False
    
    return True


email = input("Enter email: ")

# Call the function to check if the email is valid and print the result
if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")