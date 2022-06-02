from fileinput import close
from config.database import db
from controllers import controllerAcortador

def ObtenerAcortador():
    cursor=db.cursor(dictionary=True)
    cursor.execute('select * from enlaces')
    productos=cursor.fetchall()
    cursor=close()
    return productos

def crearUrl(exten_url):
    cursor=db.cursor()
    corto=controllerAcortador.url_corto()
    cursor.execute("insert into enlaces(exten,cort) values(%s,%s) ",(exten_url,corto))
    #cursor.execute("insert into enlaces(exten) values('%s')"%exten_url)
    cursor.close()
    return corto

def traerUrlCorto(urlId):
    cursor=db.cursor()
    cursor.execute("SELECT exten FROM enlaces WHERE cort=%(cort)s",{'cort':urlId})
    productos=cursor.fetchone()
    producto=productos[0]
    cursor.close()
    return producto