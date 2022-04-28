from flask import flash
from sqlalchemy import false
from werkzeug.security import generate_password_hash
import re
from models import validacionModels
from models import modelProduc
from models import userLogueo


def crearProductocontroller(nombre,correo,password):
        passwordEncrypted=generate_password_hash(password)
        isValid=False
        validaPass=Authentication(password)
        repitemail=validacionModels.correoExis(correo)
        if nombre == "":
            isValid= False
            flash("El nombre es obligatorio","error")
        
        if correo =="":
            isValid=False
            flash("El correo es obligatorio","error")
        
        if password =="":
            isValid=False
            flash("Tenga en cuenta lo siguiente: la contraseña es obligatoria","error")
        
        if not (validaPass.validate()):
            isValid =False
        else:
            isValid=True
            
        if repitemail:
            flash('existe el correo',"error")
            print('existe....')
            isValid=False
            
        if isValid ==False:
            return False
        
        validacionModels.crearUser(nombre=nombre,correo=correo,password=passwordEncrypted)
        
        return True   

class Authentication(object):
    def __init__(self, password = ''):
        self.password = password
    def __lower(self):
        lower = any(c.islower() for c in self.password)
        return lower
    def __upper(self):
        upper = any(c.isupper() for c in self.password)
        return upper
    def __digit(self):
        digit = any(c.isdigit() for c in  self.password)
        return digit
    def __character(self):
        patternpw=re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}')
        passwordval = re.search(patternpw, self.password)
        return passwordval
        
    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()
        character = self.__character()
        length = len(self.password)

        report =  lower and upper and digit and character and length >= 8

        if report:
            return True

        elif not lower:
            flash("No usaste Minusculas","error")
            return False

        elif not upper:
            flash("No usaste Mayusculas","error")
            return False

        elif length <8:
            flash("La contraseña debe tener 8 caracteres","error")
            return False

        elif not digit:
            flash("No usaste digito","error")
            return False
        
        elif not character:
            flash("No usaste caracteres","error")
            return False
        else:
            pass

def subir(nombre,imagen):
    imagen.save('./static/image/' + imagen.filename)
    
    modelProduc.crearProducto(nombre=nombre,
                    imagen='/static/image/' + imagen.filename)
    return True

def pasarUser(iduser):
    #datoName=userLogueo.userName(correo)
    print(int(iduser))
    modelProduc.misProductos(int(iduser))
    return