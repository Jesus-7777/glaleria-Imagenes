from flask import Flask, render_template, request,redirect, url_for, flash
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
        
    """  validacionModels.validar_password(password) """
    if isValid == False:
        return render_template("crearUser.html",nombre=nombre, correo=correo, password=password)
    
    
    validacionModels.crearUser(nombre=nombre,correo=correo,password=password)
    return redirect(url_for('loginUser'))

app.run(debug=True)