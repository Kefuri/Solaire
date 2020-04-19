from dbconnections import cursor, db

def fetchcreatures():
    query=('SELECT creatureID, creatureName FROM creatures')
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

def verifyteam(creature1, creature2, creature3, creature4):
    list = [creature1, creature2, creature3, creature4]

    if 'Please Select...' not in list: #Makes sure the user has seleted a monster
        if len(list) == len(set(list)): #Checks if there are any duplicates in the user's choices
            return True #By comparing the list length after duplicate values are removed
            print('Check passed') #Testing Confirmation
        else:
            print('duplicates')
            return False
    else:
        print('Default text')
        return False

def existingteamcheck(username):
    query=('''SELECT userID from userteams WHERE userID = ?
    ''') #Query created and discussed in write-up
    cursor.execute(query, [(username)])
    teams = cursor.fetchall() #puts teams fetched into a variable
    if len(teams) > 1 : #Checks how many teams fetched. Allows 2 teams max
        return False
    else: #function returns true if less than 2 teams
        return True

def storeteam(ID, creature1, creature2, creature3, creature4):

    storequery=('''INSERT INTO userteams(userID, creature1, creature2, creature3, creature4)
    VALUES(?, ?, ?, ?, ?)''') #creates the INSERT INTO query
    cursor.execute(storequery, [(ID), (creature1[1]), (creature2[1]), (creature3[1]), (creature4[1])])
    db.commit() #commits the query to the database

def teamstorefunction(username, creature1, creature2, creature3, creature4):
    if existingteamcheck(username):
        if verifyteam(creature1, creature2, creature3, creature4):
            storeteam(username, creature1, creature2, creature3, creature4)
            print('team stored')
            return True
        else:
            return False
    else:
        return False

def getuserteams(username):
    query = 'SELECT creature1, creature2, creature3, creature4 FROM userteams WHERE userID = ?'
    cursor.execute(query, [(username)])
    teams = cursor.fetchall()
    return teams

def creaturedatafetch(creature1, creature2, creature3, creature4):
    creaturearray = []
    query = 'SELECT creatureName, creatureType FROM creatures WHERE creatureID=?'

    cursor.execute(query, [(creature1)]) #runs the query with each creature ID
    creaturearray.append(cursor.fetchall()) #puts the result of the query into creaturearray

    cursor.execute(query, [(creature2)]) #repeats
    creaturearray.append(cursor.fetchall())

    cursor.execute(query, [(creature3)]) #repeats
    creaturearray.append(cursor.fetchall())

    cursor.execute(query, [(creature4)]) #repeats
    creaturearray.append(cursor.fetchall())
    return creaturearray


#def creature1infofetch(username):
#    creature1 = '''SELECT creatureName, creatureType FROM creatures WHERE creatureID = (SELECT creature1 FROM userteams WHERE userID = ?)'''
#    cursor.execute(creature1, [(username)])
#    return cursor.fetchall()

#def creature2infofetch(username):
#    creature2 = '''SELECT creatureName, creatureType FROM creatures WHERE creatureID = (SELECT creature2 FROM userteams WHERE userID = ?)'''
#    cursor.execute(creature2, [(username)])
#    return cursor.fetchall()

#def creature3infofetch(username):
#    creature3 = '''SELECT creatureName, creatureType FROM creatures WHERE creatureID = (SELECT creature3 FROM userteams WHERE userID = ?)'''
#    cursor.execute(creature3, [(username)])
#    return cursor.fetchall()

#def creature4infofetch(username):
#    creature4 = '''SELECT creatureName, creatureType FROM creatures WHERE creatureID = (SELECT creature4 FROM userteams WHERE userID = ?)'''
#    cursor.execute(creature4, [(username)])
#    return cursor.fetchall()

#def existingteamcheckdisplay(username):
#    query=('''SELECT userID from userteams WHERE userID = ?
#    ''') #Query created and discussed in write-up
#    cursor.execute(query, [(username)])
#    teams = cursor.fetchall() #puts teams fetched into a variable
#    if len(teams) > 0:
#        return True
#    else:
#        return False
