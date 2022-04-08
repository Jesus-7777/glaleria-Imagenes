from fileinput import close
import re
from flask import flash
from config.database import db
from models import validacionEmail


def obtenerUser():
    cursor=db.cursor(dictionary=True)
    cursor.execute('select * from usua')
    productos= cursor.fetchall()
    cursor= close()
    return productos

def crearUser(nombre,correo,password):
    cursor=db.cursor()
    cursor.execute("insert into usuario(nombre, correo, password) values(%s,%s,%s)",(nombre,correo,password))
    cursor.close()
    validacionEmail.envioEmail(nombre,correo)
    

def validate_password(password):
    """J3$u$diaz"""
    upperCase = False
    lowerCase= False
    numbers = False
    specialCharacter = False
    
    for c in password:
        if c.islower()== True:
            lowerCase= True
        if c.isupper()== True:
            upperCase= True
        if c.isdigit()==True:
            numbers= True 
    
    if lowerCase == False:
        flash("Una letra Minuscula.")
    if upperCase == False:
        flash("Una letra Mayusculas.")
    if numbers == False:
        flash("Un Número entre 0 - 9")
    if re.search('[@_!#$%^&*()<>?/\|}{~:]',password):                        
        specialCharacter= True
    if specialCharacter == False:
        flash("Un caracter de simbolos")
        
    """ crearUser(nombre=nombre,correo=correo,password=passwordEncrypted) """
    return 
""" validate_password(nombre,correo,password) """