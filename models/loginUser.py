from flask import redirect
from werkzeug.security import check_password_hash

from config.database import db
cursor = db.cursor()

def userLogin(email,clave):
    print(clave)
    try:
        cursor.execute("SELECT * FROM usuario where email = '"+email+"'")
        datos = cursor.fetchone()

        check_password_hash(datos[3],clave)
        print("check_password_hash")
        if(check_password_hash):
            print("Usuario correcta")
        else:
            print("Usuario incorrecto")
        
        print("Query Excecuted successfully")
    except:
        db.rollback()
        print("Error")