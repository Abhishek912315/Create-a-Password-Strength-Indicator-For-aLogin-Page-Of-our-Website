def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) > 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()_+[]{}|;:'\",.<>?`~" for char in password)

    # Check the strength
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
        return "Medium"
    else:
        return "Weak"

# Get the password from the user
password = input("Enter your password: ")
strength = check_password_strength(password)

# Display the strength
print(f"Password strength: {strength}")
