import sqlite3 as sql
with sql.connect("Solaire.db") as db:
    global cursor #cursor made global to use throughout all functions
    cursor = db.cursor() #Establishes a cursor

def loginprocess(username, password):
    find_user = ("SELECT * FROM users WHERE username = ? AND password = ?") #Creates Query
    cursor.execute(find_user,[(username),(password)]) #Executes Query with passed arguments
    results = cursor.fetchall() #Puts result into a variable
    print("Confirmation")
    print(username)
    print(password)
    print(results) #Lines 10-13 are all for test data

    if results:
        print("Success") #Tells console the check was successful as testing
        return True
    else:
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
                insertData = '''INSERT INTO users(username, emailaddress, password)
                VALUES(?, ?, ?)'''
                cursor.execute(insertData, [(username), (email), (password)])
                db.commit() #The data is only written to the database if all checks pass.
                print("Successful Register")
                return True
            else:
                print("Password Check Issue")
                return False
        else:
            print("Email Check Issue")
            return False
    else:
        print("Username Check Issue")
        return False
