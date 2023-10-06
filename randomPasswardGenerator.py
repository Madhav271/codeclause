import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user for the desired password length
password_length = int(input("Enter the desired password length: "))

if password_length < 4:
    print("Password length must be at least 4 characters.")
else:
    random_password = generate_password(password_length)
    print("Generated Password:", random_password)
