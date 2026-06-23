import string
import secrets

def generate_password(size, uppercase, numbers, symbols):
    alphabet = string.ascii_lowercase
    
    if uppercase:
        alphabet += string.ascii_uppercase
    
    if numbers:
        alphabet += string.digits
    
    if symbols:
        alphabet += string.punctuation

    password = "".join(secrets.choice(alphabet) for _ in range(size))

    return password