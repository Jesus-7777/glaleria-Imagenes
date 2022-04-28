from flask import flash, session
from models.deleteImagen import deleteimagenmodel

def deleteimagen(id):
    result = deleteimagenmodel(id)
    if result:
        flash ("Eliminado con exito!")
    else:
        flash ("No se pudo eliminar!")

