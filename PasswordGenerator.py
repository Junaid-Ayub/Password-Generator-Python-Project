import random
import string

def generate_password(length=12):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase + uppercase + digits + symbols

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)

try:
    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
        print("Password length too short. Using default length 12.")
        length = 12
except ValueError:
    print("Invalid input. Using default length 12.")
    length = 12

password = generate_password(length)
print("Your generated password is:", password)