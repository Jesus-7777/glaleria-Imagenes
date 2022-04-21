from flask import Flask, render_template,request,redirect, url_for, flash, session
from models import userLogueo
from controllers import controllerUser
from models import validacionModels


app = Flask(__name__)
app.secret_key='asdjkajsdfjerybbca5445asdfafeyrfa'

def estaIniciado():
    return True if 'loggedin' in session else False

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/senReset")
def viewreset():
    return render_template("/resetPass/emailUserPass.html")

@app.route("/senReset", methods=['GET','POST'])
def sendresetPost():
    correo = request.form.get('correo')
    validacionModels.isertToken(correo)
    
    """ return render_template("/resetPass/emailUserPass.html",correo=correo) """
    return redirect(url_for('viewMessge'))

@app.route("/reset/<token>")
def reset(token):
    print(token)
    return render_template("/resetPass/resetPassword.html")

@app.route("/senReset", methods=['GET','POST'])
def resetPost():
    print("estamos restableciendo contraseña")
    

@app.get("/messageEmail")
def viewMessge():
    return render_template("/confirEmail/confimaEmail.html")

@app.route("/login", methods=['GET','POST'])
def loginUser():
    if request.method=='POST':
        email = request.form['email']
        clave = request.form['password']
        autenticado = userLogueo.userLogin(email,clave)  
        if autenticado == True:
            session['loggedin'] = True
            return redirect("/vista")
        else:
            flash("Datos Erroneos. Confirme usuario y contraseña.")
            flash("Debe contener 8 o mas caracteres, MAYUSCULAS, minusculas, números y caracteres especiales.")
            return redirect("/login")
    return render_template("/loginUser/login.html")

@app.get("/crear")
def creaUsuario():
    return render_template("/loginUser/crearUser.html")

@app.post("/crear")
def creaUsuarioPost():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    password = request.form.get('password')
    if not controllerUser.crearProductocontroller(nombre,correo,password):
        return render_template("/loginUser/crearUser.html",nombre=nombre,correo=correo)
    return redirect(url_for('viewMessge'))

@app.route("/valida_email/<token>")
def validar_email(token):
    if validacionModels.verificarToken(token):
        return "se valido el email"

@app.get("/vista")
def vistaUsuario():
    if not estaIniciado():
        return redirect(url_for('loginUser'))
    return render_template("/vistaUser/viewUser.html")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('loginUser'))

app.run(debug=True)