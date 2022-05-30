from flask import session
from models import getImages

#mostrar las imagenes del usuario
def mostrarImgen():
    email = session['email']
    userID= session['user_id']
    result = getImages.mostrarImgen(email,userID)
    return result

#mostrar las imagenes publicas
def mostrarPublic():
        produc = getImages.getImagesPublic()
        return produc
