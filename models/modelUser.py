from config.database import db
class UsuarioModel():
    def crearUser(serlf,usuario,correo,claveEncritada):
        cursor =db.cursor()
        cursor.execute('insert into usuario(nombre,correo,password) values(%s,%s,%s)', (
            usuario,
            correo,
            claveEncritada,
            ))    
        cursor.close()  
    def validarUser(self,usuario):
        cursor =db.cursor()
        cursor.execute('select correo, password from usuario where usuario.correo = %s',(usuario,))      
        usuario = cursor.fetchall()
        cursor.close()
        return usuario

def createUser(name,email,claveEncritada):
    cursor = db.cursor()
    cursor.execute("insert into usuario (nombre,correo,password) values(%s,%s,%s)", (
        name,
        email,
        claveEncritada,
    ))
    cursor.close()