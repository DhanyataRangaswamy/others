import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password_length = 5

print("Generated password:", generate_password(password_length))

