from email import message
from flask import Flask, render_template,request,redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from config.database import db
from models import userLogueo
from controllers import controllerUser
from models import validacionModels
from models import loginUser


app = Flask(__name__)
app.secret_key='asdjkajsdfjerybbca5445asdfafeyrfa'



@app.get("/")
def index():
    return render_template("index.html")
    
@app.route("/login", methods=['GET','POST'])
def loginUser():
    if request.method=='POST':
        email = request.form['email']
        clave = request.form['password']
        autenticado = userLogueo.userLogin(email,clave)  

        if autenticado == True:
            session['loggedin'] = True
            print(session)
            return redirect("/vista")
        else:
                
            flash(" Datos incorrectos")
            return redirect("/login")


    return render_template("/loginUser/login.html")
        

@app.get("/crear")
def creaUsuario():
    return render_template("/loginUser/crearUser.html")

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
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    password = request.form.get('password')
    if not controllerUser.crearProductocontroller(nombre,correo,password):
        return render_template("/loginUser/crearUser.html",nombre=nombre,correo=correo)
    return redirect(url_for('loginUser'))


@app.get("/vista")
def vistaUsuario():
    return render_template("/vistaUser/viewUser.html")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('loginUser'))


app.run(debug=True)