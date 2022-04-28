from unicodedata import name
from flask import flash
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from models import modelProduc


def userLogin(email,clave):
    try:
        print(clave)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuario where correo = '"+email+"'")
        datos = cursor.fetchone()
        contravalid = check_password_hash(datos[3],clave)
        if contravalid: 
            print('Enviado Correctamente')
            base=datos[0]
            """ imagebase=modelProduc.misProductos(base)
            print(imagebase) """
        else:
            print('Error No se envio')
        return contravalid
    except Exception as ex:
        print(ex)
        
def userName(correo):
    cursor = db.cursor()
    cursor.execute("SELECT id FROM usuario where correo =%s",(correo,))
    datos = cursor.fetchone()
    cursor.close()
    if datos != None:
        for namedata in datos:
            return namedata
    