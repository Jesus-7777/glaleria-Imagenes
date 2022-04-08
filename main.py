from email.mime import image
from flask import Flask, render_template,request,redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from config.database import db
from models import validacionModels
from models.validacionModels import UsuarioModel, obtenerUser



app = Flask(__name__)
app.secret_key='asdjkajsdfjerybbca5445asdfafeyrfa'



@app.get("/")
def index():
    return redirect(url_for('loginUser'))
    
@app.route("/login", methods=['GET','POST'])
def loginUser():
    """ usuarioModel = UsuarioModel() """
    if request.method == "GET":
        return render_template("login.html")
    else:
        usuario = request.form['email']
        password = request.form['password']
        paswordCheck=generate_password_hash(password)
        user= obtenerUser(usuario)
    
        for datosss in user:
            print(datosss['password'])
            break
        """ user = cursor.execute('select correo, password from usuario where usuario.correo = %s',(usuario,)) """ 
        """ result = validardateuser(user,paswordCheck) """
        if user is not None and user==True:
            print("Welcome")
            session['username'] = usuario
            return redirect(url_for("viewuser"))
        else:
            flash("Correo / Password incorrect")
            return redirect(url_for("loginUser"))
            
def validardateuser(users,password):
    for user in users:
        return check_password_hash(user[3],password)

@app.get('/')
def viewUser():
    return "esto es una pagina"

@app.get("/crear")
def creaUsuario():
    return render_template("crearUser.html")

@app.get("/imagn")
def crearImagen():
    return render_template("/templates/imageloader/fromimage.html")

@app.post("/imagen")
def crearImagenPost():
    imagen= request.files['imagen']
    """ print(imagen.filename)
    imagen.save('./static/image/'+imagen.filename) """
    return render_template("/templates/imageloader/fromimage.html")

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
    
    if password =="" or password != None:
        isValid=False
        validacionModels.validate_password(password)
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