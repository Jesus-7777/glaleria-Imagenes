from fileinput import close
from flask import flash
from requests import session
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from controllers import controllerUser


def userLogin(email,clave):
    try:
        cursor=db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario where correo = %s",(email,))
        datos = cursor.fetchall()
        cursor= close()
        print(clave)
        if datos != None:
            for dato in datos:
                contravalid = check_password_hash(dato["password"],clave)
                print(contravalid)
                if contravalid: 
                    print('Enviado Correctamente')
                    base =dato["id"]
                    #controllerUser.pasarUser(base)
                    #modelProduc.misProductos(base)
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
    