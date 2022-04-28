from config.database import db
from flask import Flask, render_template

def crearProducto(nombre, imagen):
    cursor = db.cursor()
    cursor.execute("INSERT INTO producto(nombre,imagen) values(%s,%s)",(
        nombre,
        imagen,
    ))
    cursor.close()
    
def misProductos(idUser):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT imagenes, usuario.nombre FROM producto, usuario WHERE idUsuario=%s',(idUser))
    productos = cursor.fetchall()
    cursor.close()
    print(productos)
    return productos