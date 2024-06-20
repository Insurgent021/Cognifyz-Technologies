# Importing the "re" library for regular expressions
import re

def password_strength_evaluator(password):
    # Initialize strength counter and feedback list
    strength = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should include at least 8 characters")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Check for digits
    if re.search(r'[\d]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")

    # Strength Evaluation
    if strength == 5:
        strength_level = "Very Strong"
    elif strength == 4:
        strength_level = "Strong"
    elif strength == 3:
        strength_level = "Moderate"
    elif strength == 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"

    # Returning answer in a dictionary
    return {
        "strength_level": strength_level,
        "feedback": feedback
    }


password = input("Enter your password: ")

# Function execution
result = password_strength_evaluator(password)

# Print the result
print(f"Password Strength: {result['strength_level']}")

if result['feedback']:
    print("Feedback:")
    # Print feedback messages
    for message in result['feedback']:
        print(f"- {message}")
