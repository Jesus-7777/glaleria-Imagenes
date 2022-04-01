from math import fabs
import re
from flask import Flask, render_template, request,redirect, url_for, flash
from werkzeug.security import generate_password_hash,check_password_hash
from models import validacionModels

app = Flask(__name__)
app.secret_key='asdjkajsdfjerybbca5445asdfafeyrfa'

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/login")
def loginUser():
    return render_template("login.html")

@app.get("/crear")
def creaUsuario():
    return render_template("crearUser.html")

@app.post("/crear")
def creaUsuarioPost():
    nombre = request.form.get('nombre',)
    correo = request.form.get('correo')
    password = request.form.get('password')
    encriptePassword=generate_password_hash(password)
    minuscula = False
    mayuscula= False
    numeros = False
    caracterSpecial = False
    isValid=True
    
    if nombre == "":
        isValid= False
        flash("El nombre es obligatorio")
    
    if correo =="":
        isValid=False
        flash("El correo es obligatorio")
    
    if password =="":
        isValid=False
        flash("La contraseña es obligatorio")
    
    if len(password) < 8 :                       
        flash("La contraseña debe tener minimo 8 caracteres")                       
        isValid=False 
    
    for c in password:
        if c.islower()== True:
            minuscula= True
        if c.isupper()== True:
            mayuscula= True
        if c.isdigit()==True:
            numeros= True 

    if minuscula == False:
        flash("Ingrese al menos una Minuscula a la contraseña")
    if mayuscula == False:
        flash("Ingrese al menos una Mayusculas a la contraseña")
    if numeros == False:
        flash("Ingrese al menos un Número a la contraseña")
    
    if re.search('[@_!#$%^&*()<>?/\|}{~:]',password):                        
        caracterSpecial= True
    if caracterSpecial == False:
        flash("Ingrese al menos un caracter a la contraseña")

    if isValid == False:
        return render_template("crearUser.html",nombre=nombre, correo=correo, password=password)
    
    
    validacionModels.crearUser(nombre=nombre,correo=correo,password=encriptePassword)
    return redirect(url_for('loginUser'))

app.run(debug=True)