from fileinput import close
import re
from flask import flash
from config.database import db



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
        flash("Ingrese al menos una Minuscula a la contraseña")
    if upperCase == False:
        flash("Ingrese al menos una Mayusculas a la contraseña")
    if numbers == False:
        flash("Ingrese al menos un Número a la contraseña")
    
    if re.search('[@_!#$%^&*()<>?/\|}{~:]',password):                        
        specialCharacter= True
    if specialCharacter == False:
        flash("Ingrese al menos un caracter a la contraseña")
        
    """ crearUser(nombre=nombre,correo=correo,password=passwordEncrypted) """
    return 
""" validate_password(nombre,correo,password) """

def vaUser(self,usuario):
    cursor=db.cursor()
    cursor.execute('SELECT correo,password FROM usuario WHERE usuario.correo=%s,'(usuario))
    data= cursor.fetchall()
    cursor= close()
    return data