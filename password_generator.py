import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("🔐 Password Generator")

length = int(input("Enter password length: "))
password = generate_password(length)

print("✅ Generated Password:", password)