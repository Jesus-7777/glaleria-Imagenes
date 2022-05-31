from config.database import db

def getMusic():
    cursor = db.cursor(dictionary=True)
    """ cursor = db.cursor() """
    cursor.execute("SELECT * FROM music")
    myresult = cursor.fetchall()
    cursor.close()
    print(myresult)
    return myresult