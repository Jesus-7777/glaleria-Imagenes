from colorama import Cursor
from config.database import db

def mostrarImgen(email,userID):
    cursor = db.cursor()
    userID=str(userID)
    cursor.execute("SELECT * FROM producto WHERE producto.idUsuario='"+userID+"'")
    resultado=cursor.fetchall()
    cursor.close()
    print ("aqui esta perro")
    print (resultado)
    return resultado

def getImagesId(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM producto WHERE producto.idProduc = '"+id+"'")
    myresult = cursor.fetchall()
    cursor.close() 
    return myresult

def getImagesPublic():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM producto WHERE status= 'activo'")
    myresult = cursor.fetchall()
    cursor.close()
    return myresult
