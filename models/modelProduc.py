from config.database import db

def crearProducto(nombre, imagen):
    cursor = db.cursor()
    cursor.execute("INSERT INTO producto(nombrepro,imagen) values(%s,%s)",(
        nombre,
        imagen,
    ))
    cursor.close()
    
def misProductos(idUser):
    cursor = db.cursor(dictionary=True)
    idUser=str(idUser)
    cursor.execute("SELECT imagen,producto.nombrepro, usuario.nombre FROM producto, usuario WHERE producto.idUsuario='"+idUser+"'")
    #str(idUser)
    productos = cursor.fetchall()
    cursor.close()
    if productos != None:
            for datoProduc in productos:
                """ print(datoProduc)
                print(datoProduc["imagen"])
                print(datoProduc["nombre"]) """
                return datoProduc