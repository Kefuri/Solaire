from databasesetup import createconnection
import sqlite3 as sql
with sql.connect("Solaire.db") as db:
    global cursor
    cursor = db.cursor()

def loginprocess(username, password):
    find_user = ("SELECT * FROM users WHERE username = ? AND password = ?")
    cursor.execute(find_user,[(username),(password)])
    results = cursor.fetchall()
    print("Confirmation")
    print(username)
    print(password)
    print(results)

    if results:
        for i in results:
            print("Success")
            return True
    else:
        return False
