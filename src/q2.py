"""HW1 Question 2

Please implement the following function according to the provided documentation.
Tests are provided for this question in the file tests/test_q2.py."""
def validate_password(password: str) -> bool:
    """checks if a password meets certain criteria, and returns 'True' 
    if the password meets the criteria otherwise 'False'"""
    """Determines whether a password meets the requirements.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """
    if len(password) < 8:  #Checking if the password has at least 8 characters
        return False
#checking if the password meets the other criteria
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(not char.isalnum() and not char.isspace() for char in password):
        return False
    return True
print(validate_password("ISAARUBa8#"))



        




