from colorama import Cursor
from config.database import db
cursor = db.cursor()
def mostrarImgen(email):
    
    cursor.execute("SELECT * FROM usuario, producto where usuario.correo='"+email+"'")
    resultado=cursor.fetchall()
    print (resultado)
    return resultado