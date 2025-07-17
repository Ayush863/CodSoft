import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))

length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated password:", password)