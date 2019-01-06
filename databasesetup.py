import sqlite3 as sql
def createconnection():
    with sql.connect("Solaire.db") as db:
        global cursor
        cursor = db.cursor()

    print("Cursor up")
