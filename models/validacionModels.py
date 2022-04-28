from fileinput import close
from flask import copy_current_request_context
from werkzeug.security import check_password_hash,generate_password_hash
from config.database import db
from models import validacionEmail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

from models.loginUser import userLogin

s=URLSafeTimedSerializer('Secreto78SDDNCJSHadqwrweczc')
sK=URLSafeTimedSerializer('kdfjlahdjknvaksjdbvfgdgagfgddgfdafag64fg6asd4f56as4d6f54s65df4ga')

import threading

cursor=db.cursor(dictionary=True)
def correoExis(correo):
    cursor =db.cursor()
    cursor.execute('SELECT * FROM usuario WHERE correo= %s',(correo,))   
    useremail = cursor.fetchall()
    cursor.close()
    for username in useremail:
        if username != None:
            print('invalido')
            return True
        else:
            print('valido')
            return False

def verificarToken(token):
    cursor=db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuario WHERE token= %s',(token,))
    token_user= cursor.fetchall()
    if token_user != None:
        for userToken in token_user:
            tokenDato=userToken["token"]
            cursor.execute('UPDATE usuario SET estado="activo", token=NULL WHERE token= %s',(tokenDato,))
            cursor= close()
            return True
    else:
        return "no se pudo verificar"
    

def crearUser(nombre,correo,password):
    token=s.dumps(correo)
    cursor=db.cursor()
    cursor.execute("insert into usuario(nombre, correo, password,token) values(%s,%s,%s,%s)",(nombre,correo,password,token))
    cursor.close()
    
    """ validacionEmail.envioEmail(nombre,correo) """
    @copy_current_request_context
    def send_email(nombre,correo):
        validacionEmail.envioEmail(nombre,correo,token)
    
    sender = threading.Thread(name='mail_sender',
                                target=send_email(nombre,correo),
                                args=(nombre,correo))
    sender.start()

def isertToken(correo):
    tokenPass=sK.dumps(correo)
    cursor=db.cursor()
    cursor.execute("UPDATE usuario SET token=%s WHERE correo=%s",(tokenPass,correo))
    cursor.close()
    validacionEmail.sendPassReset(correo,tokenPass)
    return True
