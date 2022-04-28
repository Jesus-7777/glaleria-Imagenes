from colorama import Cursor
from config.database import db
cursor = db.cursor()
def mostrarImgen(email):
    
    cursor.execute("SELECT imagen,producto.nombrepro, usuario.nombre FROM producto, usuario WHERE usuario.correo='"+email+"'")
    resultado=cursor.fetchall()
    print (resultado)
    return resultado