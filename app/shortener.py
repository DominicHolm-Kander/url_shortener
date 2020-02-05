import string
import random

def shortener():
    all_letters = string.ascii_letters
    return ''.join([random.choice(all_letters) for i in range(8)])