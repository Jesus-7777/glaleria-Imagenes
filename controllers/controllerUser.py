from inspect import trace
from flask import flash
from sqlalchemy import false
from werkzeug.security import generate_password_hash
import re
from models import validacionModels


def crearProductocontroller(nombre,correo,password):
        passwordEncrypted=generate_password_hash(password)
        isValid=False
        validaPass=Authentication(password)
        """  repitemail=validacionModels.correoExis(correo) """
        if nombre == "":
            isValid= False
            flash("El nombre es obligatorio")
        
        if correo =="":
            isValid=False
            flash("El correo es obligatorio")
        
        if password =="":
            isValid=False
            flash("Tenga en cuenta lo siguiente: ")
        
        if not (validaPass.validate()):
            isValid =False
        else:
            isValid=True
            
        """ if repitemail == None:
            flash('existe el correo')
            print('existe....')
            isValid=False """
            
            
            
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
            flash("Nousaste Minusculas")
            return False

        elif not upper:
            flash("Nousaste Mayusculas")
            return False

        elif length <8:
            flash("La contraseña debe tener 8 caracteres")
            return False

        elif not digit:
            flash("No usaste digito")
            return False
        
        elif not character:
            flash("No usaste caracteres")
            return False
        else:
            pass
        