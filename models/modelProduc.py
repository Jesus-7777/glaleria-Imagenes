from config.database import db

def crearProducto(nombre, imagen):
    cursor = db.cursor()
    cursor.execute("INSERT INTO producto(nombre,imagen) values(%s,%s)",(
        nombre,
        imagen,
    ))
    cursor.close()
    
def misProductos():
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM producto')
    productos = cursor.fetchall()
    #producto = cursor.fetchone()
    cursor.close()
    return productos