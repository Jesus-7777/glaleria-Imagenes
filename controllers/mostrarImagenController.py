from flask import session
from models import getImages
def mostrarImgen():
    email = session['email']
    result = getImages.mostrarImgen(email)
    return result
