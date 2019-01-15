import sqlite3 as sql
with sql.connect("Solaire.db") as db:
    global cursor #cursor made global to use throughout all functions
    cursor = db.cursor() #Establishes a cursor

def fetchplayers():
    selectbyELO = ("SELECT username, ELO FROM users ORDER BY ELO DESC LIMIT 10")
    cursor.execute(selectbyELO)
    return cursor.fetchall()
