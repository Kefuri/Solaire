import dbconnections
from dbconnections import cursor, db

def loginprocess(username, password):
    find_user = ("SELECT userID FROM users WHERE username = ? AND password = ?") #Creates Query
    try:
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchone()[0]
     #Puts result into a variable
        print("Success") #Tells console the check was successful as testing
        global globalID
        globalID = str(results)
        print(globalID)
        return True
    except:
        return False #Booleans used to determine if the game should progress to the main menu

def usernamecheck(username): #Function to check for an existing username
    findusername = ("SELECT * FROM users WHERE username = ?")
    cursor.execute(findusername,[(username)])
    if cursor.fetchall():
        return False #If found, function is false and parent function stops
    elif len(username) >= 6: #If not found, checks length of username
        if username.find(' ') == -1: #attempts to locate any spaces in username
            return True #if checks pass the function returns true
        else:
            return False
    else:
        return False

def emailcheck(email):
    atcheck = email.find('@')
    if atcheck == -1: #atcheck will return -1 if there is no @ in the user input
        return False
    elif email.find(".") < (atcheck + 2): #Looks for a '.' after the @ sign to confirm a domain
        return False
    elif email.find(" ") != -1:#Checks for spaces in the email
        return False
    else:
        return True

def passwordcheck(password, confirmpassword):
    if password == confirmpassword and (len(password) >= 8): #Makes sure passwords are the same
        return True  #and that the password length is more than 8
    else:
        return False

def registeringprocess(username, email, password, confirmpassword):
    if usernamecheck(username): #Runs the data through each function
        if emailcheck(email):
            if passwordcheck(password, confirmpassword):
                print(username, email, password) #test data
                insertData = '''INSERT INTO users(username, emailaddress, password, ELO)
                VALUES(?, ?, ?, 100)'''
                cursor.execute(insertData, [(username), (email), (password)])
                db.commit() #The data is only written to the database if all checks pass.
                db.close()
                print("Successful Register")
                return True
            else:

                return "Password Check Issue"
        else:
            return "Email Check Issue"
    else:
        return "Username Already Exists!"
