import string
import random
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
try:
    length = int(input('Enter the desired password length: '))
    if length < 8:
        raise ValueError('Password length must be at least 8 characters')
    print(f'Generated Password: {generate_password(length)}')
except ValueError as e:
    print(e)
