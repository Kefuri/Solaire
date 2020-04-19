from dbconnections import cursor

def fetchplayers():
    selectbyELO = ("SELECT username, ELO FROM users ORDER BY ELO DESC LIMIT 10")
    cursor.execute(selectbyELO)
    return cursor.fetchall()
    db.close()
