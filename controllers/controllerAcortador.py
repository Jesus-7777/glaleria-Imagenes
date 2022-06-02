from models import modelcontrolador
import random
import string

def url_corto():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=4)
        rand_letters = "".join(rand_letters)
        return rand_letters
