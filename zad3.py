import random
import string
 
def generate_password():
    length = 10
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password
 
print(generate_password())