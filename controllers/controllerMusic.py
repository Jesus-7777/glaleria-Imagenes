from models import createMusic

def subir(nombre,cancion):
    cancion.save('./static/audio/' + cancion.filename)
    
    createMusic.crearMusic( nombre=nombre,
                    cancion='/static/audio/' + cancion.filename)
    return True