from dbconnections import cursor, db

def getbattleteams(userID):
    query = 'SELECT teamID, teamname FROM userteams WHERE userID = ?'
    cursor.execute(query, [(userID)])
    return cursor.fetchall()

def updateelo(userID, battlestate):
    fetchELO = '''SELECT ELO FROM users WHERE userID=?''' #query to get ELO
    setELO = '''UPDATE users SET ELO = ? WHERE userID = ? ''' #Query to update ELO
    cursor.execute(fetchELO, [(userID)]) #executes get query
    currentELO = cursor.fetchone()[0] #places result in variable
    print(f"Current ELO is {currentELO}")
    if battlestate == True: #if battle is a win the ELO increases by 5%
        newELO = currentELO + (currentELO *0.05)
    elif battlestate == False: #if battle is a loss ELO decreases by 10%
        newELO = currentELO - (currentELO *0.1)
    print(f"New ELO is {newELO}")
    cursor.execute(setELO, [(newELO), (userID)]) #sets the new ELO
    db.commit()
    db.close()
