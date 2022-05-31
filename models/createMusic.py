from config.database import db

def crearMusic(nombre, cancion):
    cursor = db.cursor()
    cursor.execute("INSERT INTO music(descripcion,cancion) values(%s,%s)",(
        nombre,
        cancion,
    ))
    cursor.close()