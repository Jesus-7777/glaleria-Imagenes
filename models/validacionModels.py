from fileinput import close
from string import punctuation
from flask import Flask, render_template, request,redirect, url_for, flash
from werkzeug.security import generate_password_hash,check_password_hash
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
    

""" def validar_password(nombre,correo,password):
    
    isValid=True
    if nombre == "":
        isValid= False
        flash("El nombre es obligatorio")
    if correo =="":
        isValid=False
        flash("El correo es obligatorio")
    if password=="":
        isValid=False
        flash("La contraseña es obligatorio")
    if len(password)<8:
        if any([c.isdigit() for c in password]):
            if any([c.islower() for c in password]):
                if any([c.isupper() for c in password]):
                    if any([True if c in punctuation else False for c in password]):
                        flash("contraseña establecida correctamente")
                        return True
                    else:
                        flash("debe tener un caracter especial")
                else:
                    flash("debe tener una mayuscula")
            else:
                flash("debe tener una minuscula")
        else:
            flash("debe tener un numero")
    else:
        flash("la contraseña bebe tener 8 caracteres")
        
    crearUser(nombre=nombre,correo=correo,password=encriptePassword) 
    return render_template("crearUser.html",nombre=nombre, correo=correo, password=password) """
    
