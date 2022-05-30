from config.database import db

def crearProducto(idUser,nombre, imagen):
    cursor = db.cursor()
    cursor.execute("INSERT INTO producto(idUsuario,nombrepro,imagen) values(%s,%s,%s)",(
        idUser,
        nombre,
        imagen,
    ))
    cursor.close()