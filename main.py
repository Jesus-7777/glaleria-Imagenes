from pyexpat import model
from flask import Flask, render_template,request,redirect, url_for, flash, session
from models import userLogueo
from controllers import controllerUser,mostrarImagenController
from models import validacionModels
from models import modelProduc



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
    flash("Se enviara a tu correo las instrucciones de cambio de contraseña 🔏","exito")
    return redirect(url_for('viewreset'))

@app.route("/reset/<token>")
def reset(token):
    return render_template("/resetPass/resetPassword.html",token=token)

@app.route("/reset", methods=['GET','POST'])
def resetPassPost():
    correo = request.form.get('correo')
    token = request.form.get('token')
    password = request.form.get('password')
    print("estamos restableciendo contraseña")
    if validacionModels.cambioPss(token,password):
        flash("La contraseña se cambio correctamente ✅","exito")
        return redirect(url_for('loginUser'))
    else:
        flash("Ocurrio un error vuelva a enviar el correo 📧","error")
        return redirect(url_for('viewreset'))
    

@app.get("/messageEmail")
def viewMessge():
    return render_template("/confirEmail/confimaEmail.html")

@app.route("/login", methods=['GET','POST'])
def loginUser():
    if request.method=='POST':
        email = request.form['email']
        clave = request.form['password']
        print(clave)
        autenticado = userLogueo.userLogin(email,clave)  
        if autenticado == True:
            session['loggedin'] = True
            session['email']=email
            return redirect("/vista")
        else:
            flash("Datos Erroneos. Confirme usuario y contraseña. Debe contener 8 o mas caracteres, MAYUSCULAS, minusculas, números y caracteres especiales.","error")
            #flash("Debe contener 8 o mas caracteres, MAYUSCULAS, minusculas, números y caracteres especiales.","error")
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
        flash("Ingrese los valores correctos","error")
        return render_template("/loginUser/crearUser.html",nombre=nombre,correo=correo)
    #return redirect(url_for('viewMessge'))
    flash("se enviara un correo de confirmacion al correo con el que te registraste 👍","exito")
    return redirect(url_for('loginUser'))

@app.get("/subir")
def mostrarArchivo():
    if not estaIniciado():
        return redirect(url_for('loginUser'))
    return render_template("/productos/crearArchivo.html")

@app.route("/subir", methods=['GET','POST'] )
def subirArchivoPost():
    nombre = request.form['nombre']
    imagen = request.files['image']
    if controllerUser.subir(nombre,imagen):
        flash("El archivo se agrego correctamente ✅","exito")
    return render_template("/productos/crearArchivo.html")

@app.route("/valida_email/<token>")
def validar_email(token):
    if validacionModels.verificarToken(token):
        flash("Su cuenta se valido correctamente 👍, ya puedes ingesar","exito")
        return redirect(url_for('loginUser'))
    else:
        return "error 404"

@app.get("/vista")
def vistaUsuario():
    if not estaIniciado():
        return redirect(url_for('loginUser'))
    else: 
        imagen = mostrarImagenController.mostrarImgen()
        #productos = modelProduc.misProductos(),productos=productos
        return render_template("/vistaUser/viewUser.html",imagen=imagen)

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('loginUser'))

app.run(debug=True)