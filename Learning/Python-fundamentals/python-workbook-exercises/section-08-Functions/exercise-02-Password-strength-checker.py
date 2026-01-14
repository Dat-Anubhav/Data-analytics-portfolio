# A function to check if the password is strong
def is_strong_password(password):
    
    # Password must be at least 8 characters long
    if (len(password)<8):
        
        return False
    
    # Password must contain at least one digit
    if not any(char.isdigit() for char in password):
        
         return False
    
    # Password must contain at least one lowercase letter
    if not any(char.islower() for char in password):

        return False
    
    # Password must contain at least one uppercase letter
    if not any(char.isupper() for char in password):

        return False
    
    # Password must contain at least one special character from the given set
    if not any(char in '!@#$%^&*?/|\;:,()_+' for char in password):

        return False
    
    return True
print("\nFalse means weak password & True means strong password\n")
# Test with a strong password example
print(is_strong_password("Anubhav134@"))
# Test with a weak password example
print(is_strong_password("Anubhav"))