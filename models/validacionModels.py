from fileinput import close
from re import U
from tkinter.messagebox import NO
from sqlalchemy import true
from werkzeug.security import check_password_hash,generate_password_hash
from flask import flash
from config.database import db

cursor=db.cursor(dictionary=True)
def correoExis(correo):
    cursor =db.cursor()
    cursor.execute('SELECT correo FROM usuario WHERE correo= %s',(correo,))   
    useremail = cursor.fetchall()
    print(useremail)
    cursor.close()
    return False


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
            