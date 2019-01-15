import sqlite3 as sql

with sql.connect("Solaire.db") as db:
    global cursor #cursor made global to use throughout all functions
    cursor = db.cursor() #Establishes a cursor

def fetchcreatures():
    query=('SELECT creatureName FROM creatures')
    cursor.execute(query)
    return cursor.fetchall()
