
from config.database import db
cursor = db.cursor()
def deleteimagenmodel(id):
    print (id)
    cursor.execute("DELETE FROM producto where id="+id+"")
    print(cursor)
    db.commit()

    return True