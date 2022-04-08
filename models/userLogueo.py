from colorama import Cursor
from flask import flash
from sqlalchemy import CheckConstraint
from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash


def userLogin(email,clave):
    try:
        print(clave)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM usuario where correo = '"+email+"'")
        datos = cursor.fetchone()
        contravalid = check_password_hash(datos[3],clave)
        
        print("Query Excecuted successfully") 
        return contravalid
    except Exception as ex:
        print(ex)
        
