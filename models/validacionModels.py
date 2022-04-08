from dataclasses import dataclass
from fileinput import close
import json
from tkinter.messagebox import NO
from werkzeug.security import check_password_hash,generate_password_hash
import re
from flask import flash
from config.database import db

cursor=db.cursor(dictionary=True)
class UsuarioModel():
    def validarUser(self,usuario):
        cursor =db.cursor()
        cursor.execute('select correo, password from usuario where usuario.correo = %s',(usuario,))      
        userdata= cursor.fetchall()
        cursor.close()
        return userdata

def obtenerUser(usuario):
    cursor=db.cursor(dictionary=True)
    cursor.execute('select correo, password from usuario where usuario.correo = %s',(usuario,)) 
    productos= cursor.fetchall()
    cursor= close()
    return productos

def crearUser(nombre,correo,password):
    cursor=db.cursor()
    cursor.execute("insert into usuario(nombre, correo, password) values(%s,%s,%s)",(nombre,correo,password))
    cursor.close()
    

def usuarioExit(correo,password):
        print(password)
        passwordChek=generate_password_hash(password)
        cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND clave = ?', (correo, passwordChek))
        dataBases = cursor.fetchone()
        
        if dataBases!=None:
            for data in dataBases:
                """ check_password_hash(data[3],passwordChek) """
            print(data['correo'])
        else:
            print("Usuario incorrecto")
            
        print("Query Excecuted successfully")
            

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