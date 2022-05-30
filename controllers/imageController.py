from flask import flash,session
from models import getImages, actualStatusImg

def cambiarStatusImagen(id):
    datosBase=getImages.getImagesId(id)
    for imgstatus in datosBase:
        stado=imgstatus[4]
        if actualStatusImg.cambiar(id,stado):
            print('bueno')
        else:
            print('malo')