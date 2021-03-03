import random
import string


base_str = string.digits+string.ascii_letters

def get_random_chr(length=16):
    return ''.join(random.choice(base_str) for x in range(length))
