from config.database import db

def crearProducto(nombre, imagen):
    cursor = db.cursor()
    cursor.execute("INSERT INTO producto(nombre,imagen) values(%s,%s)",(
        nombre,
        imagen,
    ))
    cursor.close()
    
def misProductos(idUser):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT imagen, usuario.nombre FROM producto, usuario WHERE producto.idUsuario="+str(idUser)+"")
    productos = cursor.fetchall()
    cursor.close()
    if productos != None:
            for datoProduc in productos:
                print(datoProduc)
                print(datoProduc["imagen"])
                print(datoProduc["nombre"])
                return datoProduc