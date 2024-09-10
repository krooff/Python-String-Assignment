#Task 1: Input Length Validator

def name_length_validation():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    else:
        print(f"Name is valid: {first_name} {last_name}")

# Call the function
name_length_validation()
