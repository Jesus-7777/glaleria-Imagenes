from flask import Flask, render_template,request,redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from config.database import db
from models import validacionModels
from models.modelUser import UsuarioModel


app = Flask(__name__)
app.secret_key='asdjkajsdfjerybbca5445asdfafeyrfa'

@app.get("/")
def index():
    return redirect(url_for('loginUser'))
    
@app.route("/login", methods=['GET','POST'])
def loginUser():
    if request.method=='POST':
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.get("/crear")
def creaUsuario():
    return render_template("crearUser.html")

@app.post("/crear")
def creaUsuarioPost():
    nombre = request.form.get('nombre',)
    correo = request.form.get('correo')
    password = request.form.get('password')
    passwordEncrypted=generate_password_hash(password)
    isValid=True
    """ validacionModels.validate_password(nombre,correo,password) """
    """ return redirect(url_for('index')) """
    """ return redirect(url_for('creaUsuarioPost')) """
    """ return render_template("crearUser.html",nombre=nombre, correo=correo) """
    
    if nombre == "":
        isValid= False
        flash("El nombre es obligatorio")
        """ print("El nombre es obligatorio") """    
    
    if correo =="":
        isValid=False
        flash("El correo es obligatorio")
        """ print("El correo es obligatorio") """
    
    if password =="":
        isValid=False
        flash("La contraseña es obligatorio")
    
    if 8 > len(password) :                       
        flash("La contraseña debe tener minimo 8 caracteres")  
        validacionModels.validate_password(password)                     
        isValid=False
    
    if isValid == False:
        """ print(nombre,correo,password) """
        return render_template("crearUser.html",nombre=nombre,correo=correo)
    
    validacionModels.crearUser(nombre=nombre,correo=correo,password=passwordEncrypted)
    return redirect(url_for('loginUser'))

app.run(debug=True)