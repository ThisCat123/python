import random
import string

def generate_password(length):
    """This function generates a random password
    of a given length using a combination of
    uppercase letters, lowercase letters,
    digits, and special characters"""


    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(all_chars) for i in range(length))

    return password




password = generate_password(10)
print('your generated password:')
print(password)
