from fileinput import close

from flask import flash
from config.database import db
import re

def obtenerUser():
    cursor=db.cursor(dictionary=True)
    cursor.execute('select * from productos')
    productos= cursor.fetchall()
    cursor= close()
    return productos

def crearUser(nombre,correo,password):
    cursor=db.cursor()
    cursor.execute("insert into usuario(nombre, correo, password) values(%s,%s,%s)",(nombre,correo,password))
    cursor.close()
    

def validar_password(password):
    if len(password) <= 8:
        if re.search('[a-z]',password) and re.search('[A-Z]',password):
            if re.search('[0-9]',password):
                if re.search('[$@#]',password):
                    flash('La contraseña es correcta')
                    return True
                else: 
                    flash('la contraseña debe contener mas de 8 caracteres')
            else: 
                flash('debe contener almenos un numero')    
        else: 
            flash('debe contener una minuscula y una mayuscula')
    else: 
        flash('la contraseña debe contener mas de 8 caracteres')