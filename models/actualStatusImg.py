from config.database import db

def cambiar(id,status):
    cursor = db.cursor()
    if status == 'activo':
            estado= 'inactivo'
    if status == 'inactivo':
            estado= 'activo'
    cursor.execute("UPDATE producto SET status = %s WHERE idProduc = %s ",(estado,id))
    db.commit()
    return True