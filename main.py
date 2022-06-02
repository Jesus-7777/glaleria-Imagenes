from pyexpat import model
from flask import Flask, render_template, request, redirect, url_for, flash, session
from controllers import controllerUser, mostrarImagenController, deleteimagenController,imageController, controllerMusic
from models import validacionModels, verMusic, modelUser, userLogueo, modelcontrolador


app = Flask(__name__)
app.secret_key = 'asdjkajsdfjerybbca5445asdfafeyrfa'


def estaIniciado():
    return True if 'loggedin' in session else False


@app.get("/")
def index():
    produc = mostrarImagenController.mostrarPublic()
    print(produc)
    return render_template("index.html",produc=produc)


@app.get("/senReset")
def viewreset():
    return render_template("/resetPass/emailUserPass.html")


@app.route("/senReset", methods=['GET', 'POST'])
def sendresetPost():
    correo = request.form.get('correo')
    validacionModels.isertToken(correo)
    flash("Se enviara a tu correo las instrucciones de cambio de contraseña 🔏", "exito")
    return redirect(url_for('viewreset'))


@app.route("/reset/<token>")
def reset(token):
    return render_template("/resetPass/resetPassword.html", token=token)


@app.route("/reset", methods=['GET', 'POST'])
def resetPassPost():
    correo = request.form.get('correo')
    token = request.form.get('token')
    password = request.form.get('password')
    print("estamos restableciendo contraseña")
    if validacionModels.cambioPss(token, password):
        flash("La contraseña se cambio correctamente ✅", "exito")
        return redirect(url_for('loginUser'))
    else:
        flash("Ocurrio un error vuelva a enviar el correo 📧", "error")
        return redirect(url_for('viewreset'))


@app.get("/messageEmail")
def viewMessge():
    return render_template("/confirEmail/confimaEmail.html")


@app.route("/login", methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        email = request.form['email']
        clave = request.form['password']
        autenticado = userLogueo.userLogin(email, clave)
        idEmal = modelUser.traerID(email)
        if autenticado == True:
            session['loggedin'] = True
            session['email'] = email
            session['user_id'] = idEmal
            print('este es el id')
            print(session['user_id'])
            return redirect("/vista")
        else:
            flash("Datos Erroneos. Confirme usuario y contraseña. Debe contener 8 o mas caracteres, MAYUSCULAS, minusculas, números y caracteres especiales.", "error")
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
    if not controllerUser.crearProductocontroller(nombre, correo, password):
        flash("Ingrese los valores correctos", "error")
        return render_template("/loginUser/crearUser.html", nombre=nombre, correo=correo)
    # return redirect(url_for('viewMessge'))
    flash("se enviara un correo de confirmacion al correo con el que te registraste 👍", "exito")
    return redirect(url_for('loginUser'))


@app.get("/subir")
def mostrarArchivo():
    if not estaIniciado():
        return redirect(url_for('loginUser'))
    return render_template("/productos/crearArchivo.html")


@app.route("/subir", methods=['GET', 'POST'])
def subirArchivoPost():
    nombre = request.form['nombre']
    imagen = request.files['image']
    idUser = session['user_id']
    if controllerUser.subir(idUser,nombre, imagen):
        flash("El archivo se agrego correctamente ✅", "exito")
    return render_template("/productos/crearArchivo.html")


@app.route("/valida_email/<token>")
def validar_email(token):
    if validacionModels.verificarToken(token):
        flash("Su cuenta se valido correctamente 👍, ya puedes ingesar", "exito")
        return redirect(url_for('loginUser'))
    else:
        return "error 404"


@app.get("/vista")
def vistaUsuario():
    if not estaIniciado():
        return redirect(url_for('loginUser'))
    else:
        imagen = mostrarImagenController.mostrarImgen()
        return render_template("/vistaUser/viewUser.html", imagen=imagen)


@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    return redirect(url_for('loginUser'))


@app.route("/deleteimg/<id>")
def delete(id):
    deleteimagenController.deleteimagen(id)
    return redirect(url_for('vistaUsuario'))

@app.route("/imgStatus/<id>")
def cambiarStatus(id):
    imageController.cambiarStatusImagen(id)
    return redirect(url_for('vistaUsuario'))

@app.get("/radio")
def vistaRadio():
    resultMusic=verMusic.getMusic()
    print(resultMusic)
    return render_template("./radio/radioIndex.html",resultMusic=resultMusic)

@app.get("/subirMusic")
def subirMusic():
    return render_template("./radio/subirCancion.html")

@app.route("/subirMusic", methods=['GET', 'POST'])
def subirMusicPost():
    nombre = request.form['nombre']
    cancion = request.files['cancion']
    if controllerMusic.subir(nombre, cancion):
        flash("El archivo se agrego correctamente ✅", "exito")
    return render_template("./radio/radioIndex.html")

"""Parte del acortador"""

@app.get("/acortador")
def vistaAcortador():
    productos=modelcontrolador.ObtenerAcortador()
    return render_template("./vistaUser/acortador.html",productos=productos)

@app.route("/crearAcortador",methods=["GET","POST"])
def crearUrlPost():
    if request.method=='POST':
        exten_url=request.form.get('exten')
        corto=modelcontrolador.crearUrl(exten_url)
        return render_template("productos/crearAcortador.html",corto=corto)
    #return render_template("index.html",corto=corto)

@app.get('/short/<urlId>')
def traerUrl(urlId):
    producto=modelcontrolador.traerUrlCorto(urlId)
    return redirect(producto)

app.run(debug=True)
