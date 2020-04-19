import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
import loginbackend as lgb
from loginbackend import loginprocess, registeringprocess
import leaderboardbackend as ldb
from leaderboardbackend import fetchplayers
import teambuilderbackend as tbb
from teambuilderbackend import fetchcreatures, teamstorefunction, creaturedatafetch, getuserteams
import casualbattlebackend as cbb
from casualbattlebackend import getbattleteams
import fightClasses as fc
from PIL import Image, ImageTk

smallfont = ("Calibri", 8)
mediumfont = ("Calibri", 10)
largefont = ("Calibri", 16)
titlefont = ("Calibri", 18)
buttonfont = ("Calibri", 15)

class SolaireGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Solaire")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, MainMenu, PlayMenu, RegisterPage, MenuSettings, TeamBuilderPage,
         LeaderboardPage, CreaturePage, ExistingTeamsPage, CasualBattleMenu, BattleScreen):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def quitprogram(self):
        tk.Tk.destroy()

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')
        loginlabel = tk.Label(self, text="Login To Solaire!", font=titlefont, bg='#b5fff2')
        loginlabel.pack(pady=10, padx=10)

        usernamelabel = tk.Label(self, text="Username:", font=smallfont, bg='#b5fff2')
        usernamelabel.pack()
        usernamebox = tk.Entry(self, width=15)
        usernamebox.pack(pady=10, padx=10)

        passwordlabel = tk.Label(self, text="Password:", font=smallfont, bg='#b5fff2')
        passwordlabel.pack()
        passwordbox = tk.Entry(self, show="*", width=15)
        passwordbox.pack(pady=10, padx=10)

        loginbutton = ttk.Button(self, text="Log In!",
        command=lambda: self.logincommand(controller, usernamebox.get(), passwordbox.get()))
        loginbutton.pack()

        exitbutton = ttk.Button(self, text="Exit", command=lambda: quit(self))
        exitbutton.pack()

        registerlabel = tk.Label(self, text="New to Solaire?", font=largefont, bg='#b5fff2')
        registerbutton = ttk.Button(self, text="Register!", command=lambda: controller.show_frame(RegisterPage))
        registerlabel.pack()
        registerbutton.pack()
    def logincommand(self, controller, username, password): #Lets the button run two functions
        if loginprocess(username, password) == True: #Verifies whether the login was successful
            controller.show_frame(MainMenu) #Pushes the program forward if good login
            print(lgb.globalID)
        else:
            label = tk.Label(self, text="Incorrect login details!",font=largefont, bg='#b5fff2')
            label.pack()

class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        exitbutton = ttk.Button(self, text='Exit', command=lambda: controller.show_frame(LoginPage))
        exitbutton.place(x=0, y=0)

        registertitle = tk.Label(self, text="Sign Up to Solaire", font=titlefont, bg='#b5fff2')
        registertitle.pack(pady=20)

        usernamelabel = tk.Label(self, text="Username:", font=smallfont, bg='#b5fff2')
        usernamelabel.pack()
        usernamebox = tk.Entry(self, width=25)
        usernamebox.pack(pady=10, padx=10)

        emailaddresslabel = tk.Label(self, text="Email Address:", font=smallfont, bg='#b5fff2')
        emailaddresslabel.pack()
        emailaddressbox = tk.Entry(self, width=25)
        emailaddressbox.pack(pady=10, padx=10)

        passwordlabel = tk.Label(self, text="Password:", font=smallfont, bg='#b5fff2')
        passwordlabel.pack()
        passwordbox = tk.Entry(self, show="*", width=25)
        passwordbox.pack(pady=10, padx=10)

        confirmpasswordlabel = tk.Label(self, text="Confirm Password:", font=smallfont, bg='#b5fff2')
        confirmpasswordlabel.pack()
        confirmpasswordbox = tk.Entry(self, show="*", width=25)
        confirmpasswordbox.pack(pady=10, padx=10)

        registerbutton = ttk.Button(self, text="Register now!",
        command=lambda: self.registercommand(controller, usernamebox.get(), emailaddressbox.get(),
         passwordbox.get(), confirmpasswordbox.get()))
        registerbutton.pack()

        self.errorcodelabel = tk.Label(self, text="", font=mediumfont, bg='#b5fff2')
    def registercommand(self, controller, username, email, password, confirmpassword):
        if registeringprocess(username, email, password, confirmpassword) == True:
            controller.show_frame(MainMenu)
        else:
            self.errorcodelabel.config(text=registeringprocess(username, email, password, confirmpassword))
            self.errorcodelabel.pack()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')
        title = tk.Label(self, text="Solaire", font=largefont, bg='#b5fff2')
        title.pack(pady=10, padx=10)

        playbutton = ttk.Button(self, text="Play!",
        command=lambda: controller.show_frame(PlayMenu))
        playbutton.pack()

        settingsbutton = ttk.Button(self, text="Settings!",
        command=lambda: controller.show_frame(MenuSettings))
        settingsbutton.pack()

        returnbutton = ttk.Button(self, text="Quit!",
        command=lambda: quit(self))
        returnbutton.pack()

class PlayMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        returntomenu = ttk.Button(self, text="Return to menu",
        command = lambda: controller.show_frame(MainMenu))
        returntomenu.grid(row=0, sticky="W", pady=5)

        casualbattle = tk.Button(self, text="Battle!", font=mediumfont,
        command = lambda: controller.show_frame(CasualBattleMenu))
        casualbattle.configure(width=60, height =15)
        casualbattle.grid(row=1, column=0, padx=20, pady=20)

        teambuilder = tk.Button(self, text="Team Builder", font=mediumfont,
        command = lambda: controller.show_frame(TeamBuilderPage))
        teambuilder.configure(width=60, height =7)
        teambuilder.grid(row=3, column=0, padx=20)

        leaderboard = tk.Button(self, text="Leaderboard", font=mediumfont,
        command = lambda: controller.show_frame(LeaderboardPage))
        leaderboard.configure(width=60, height =7)
        leaderboard.grid(row=4, column=0, pady=20, padx=20)



class MenuSettings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        settingstitle = tk.Label(self, text="Settings", font=largefont, bg='#b5fff2')
        settingstitle.grid(row=0, column=0)

        settingsseparator = ttk.Separator(self, orient="horizontal")
        settingsseparator.grid(row=1, column=1, sticky='E')

        returnbutton = ttk.Button(self, text="Return to Main Menu", command=lambda: controller.show_frame(MainMenu))
        returnbutton.grid(row=1, column=3)

class LeaderboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        returnbutton =  ttk.Button(self, text="Return to main menu",
            command = lambda: controller.show_frame(PlayMenu))
        returnbutton.grid(row=0, column =0, sticky="W")

        leaderboardtitle = tk.Label(self, text="          The Leaderboard           ", font=titlefont, bg='#b5fff2')
        leaderboardtitle.grid(row=0, column=1)

        refreshbutton = ttk.Button(self, text="Refresh!", command= lambda: self.displayrankings())
        refreshbutton.grid(row=0, column=3, sticky="E") #Runs the functions again to refresh the database
        #in case of any new ELO gains.
        self.displayrankings() #Runs the display to generate rankings

    def displayrankings(self):
        players = fetchplayers() #assigns the return value of the function to a variable
        i = 0
        for name, elo in players:
            tk.Label(self, text=f"{i+1}. {name}                    {elo}", font= largefont, bg='#b5fff2').grid(row=(1 + i), column=1)
            i += 1 #Creates a label for each of the data entries in players

class TeamBuilderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        returntomenubutton = ttk.Button(self, text="Return to menu", command = lambda: controller.show_frame(PlayMenu))
        returntomenubutton.grid(column=0, row=0, sticky='w')

        titlelabel = tk.Label(self, text="Teambuilder", font=largefont, bg='#b5fff2')
        titlelabel.grid(column=1, row=0, sticky='n')

        newteambutton = ttk.Button(self, text="Create a new team", command= lambda: controller.show_frame(CreaturePage))
        viewteambutton = ttk.Button(self, text="View your existing teams", command = lambda: controller.show_frame(ExistingTeamsPage))

        divider= ttk.Separator(self)
        divider.grid(column=1, row=1, columnspan=10, sticky='ew', pady=10)

        newteambutton.grid(column=1, row=2, sticky='nsew')
        viewteambutton.grid(column= 1, row=3, sticky='nsew')

class CreaturePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        returnbutton =  ttk.Button(self, text="Return to menu",
            command = lambda: controller.show_frame(TeamBuilderPage))
        returnbutton.grid(row=0, column =0, sticky="W")

        choices = fetchcreatures()

        self.choice1 = StringVar()
        self.choice2 = StringVar()
        self.choice3 = StringVar()
        self.choice4 = StringVar()

        self.choice1.set('Please Select...')
        self.choice2.set('Please Select...')
        self.choice3.set('Please Select...')
        self.choice4.set('Please Select...')

        monster1label = tk.Label(self, text="Monster 1", font=mediumfont, bg = '#b5fff2')
        monster1entry = tk.OptionMenu(self, self.choice1, *choices)
        monster1label.grid(row=1, column=1)
        monster1entry.grid(row=2, column=1)

        divider = ttk.Separator(self).grid(row=3, column=1, columnspan=10, sticky='ew', pady=10)

        monster2label = tk.Label(self, text="Monster 2", font=mediumfont, bg = '#b5fff2')
        monster2entry = tk.OptionMenu(self, self.choice2, *choices)
        monster2label.grid(row=4, column=1)
        monster2entry.grid(row=5, column=1)

        divider = ttk.Separator(self).grid(row=6, column=1, columnspan=10, sticky='ew', pady=10)

        monster3label = tk.Label(self, text="Monster 3", font=mediumfont, bg = '#b5fff2')
        monster3entry = tk.OptionMenu(self, self.choice3, *choices)
        monster3label.grid(row=7, column=1)
        monster3entry.grid(row=8, column=1)

        divider = ttk.Separator(self).grid(row=9, column=1, columnspan=10, sticky='ew', pady=10)

        monster4label = tk.Label(self, text="Monster 4", font=mediumfont, bg = '#b5fff2')
        monster4entry = tk.OptionMenu(self, self.choice4, *choices)
        monster4label.grid(row=10, column=1)
        monster4entry.grid(row=11, column=1)

        createteambutton= ttk.Button(self, text="Create team",
        command = lambda : self.storeteamcommand(controller, lgb.globalID, self.choice1.get(), self.choice2.get(),
            self.choice3.get(), self.choice4.get()))
        createteambutton.grid(row=12, column=2)

    def storeteamcommand(self, controller, username, creature1, creature2, creature3, creature4):
        if teamstorefunction(username, creature1, creature2, creature3, creature4):
            successfullabel = tk.Label(self, text='Team Created Successfully!', font=largefont, bg = '#b5fff2')
            successfullabel.grid(row=13, column=1)
            successfullabel.after(2, controller.show_frame, TeamBuilderPage)
        else:
            errorlabel = tk.Label(self, text="Error Creating Team!", font=largefont, bg = '#b5fff2')
            errorlabel.grid(row=13, column=1)
            errorlabel.after(3000, controller.show_frame, TeamBuilderPage)




class ExistingTeamsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')

        titlelabel = tk.Label(self, text = "Your Teams", font=largefont, bg='#b5fff2')
        titlelabel.grid(row=0, column=1)

        divider = ttk.Separator(self).grid(row=1, column=0, columnspan=10, sticky='ew', pady=10)

        team1label = tk.Label(self, text = "Team One", font=mediumfont, bg='#b5fff2')
        team1label.grid(row=2, column=0)

        divider = ttk.Separator(self).grid(row=11, column=0, columnspan=10, sticky='ew', pady=10)

        team2label = tk.Label(self, text='Team Two', font=mediumfont, bg='#b5fff2')
        team2label.grid(row=12, column=0)

        getteambutton = tk.Button(self, text = "Get your teams", bg='#b5fff2',
        command=lambda:self.userteamfetch(lgb.globalID)).grid(row=2, column=2)

        backbutton = ttk.Button(self, text='Go Back', command= lambda: controller.show_frame(TeamBuilderPage))
        backbutton.grid(row=21, column=2)

    def userteamfetch(self, username):
        teams = getuserteams(username) #gets the teams into a variable
        if len(teams) == 2: #if the user has two teams:
            team1 = teams[0] #places the team data into two separate variables
            team2 = teams[1]
            team1data = creaturedatafetch(team1[0], team1[1], team1[2], team1[3]) #fetches the creature data for the team
            t1 = str(team1data).translate({ord(i): None for i in "[]{}()'"})
            t1data = t1.split(",")
            team2data = creaturedatafetch(team2[0], team2[1], team2[2], team2[3]) #to get the data into their own variables
            t2 = str(team2data).translate({ord(i): None for i in "[]{}()'"})
            t2data = t2.split(",")

            for x in range(len(t1data)): #runs through each creature in the team and places it in a label
                creaturetitle = tk.Label(self, text=f'Creature {x+1}', bg='#b5fff2').grid(row=(3+(2*x)), column=0)
                creaturedata = tk.Label(self, text=f'{team1data[x]}', bg='#b5fff2').grid(row=(4+(2*x)), column=0)

            for y in range(len(t2data)): #does the same thing for the second team
                creaturetitle = tk.Label(self, text=f'Creature {y+1}', bg='#b5fff2').grid(row=(13+(2*y)), column=0)
                creaturedata = tk.Label(self, text=f'{team2data[y]}', bg='#b5fff2').grid(row=(14+(2*y)), column=0)

        elif len(teams) == 1: #if the user has just 1 team
            team1 = teams[0]
            team1data = creaturedatafetch(team1[0], team1[1], team1[2], team1[3]) #fetches the creature data for the team
            t1 = str(team1data).translate({ord(i): None for i in "[]{}()'"})
            t1data = t1.split(",")
            for x in range(len(team1data)): #repeats the same process
                creaturetitle = tk.Label(self, text=f'Creature {x+1}', bg='#b5fff2').grid(row=(3+(2*x)), column=0)
                creaturedata = tk.Label(self, text=f'{team1data[x]}', bg='#b5fff2').grid(row=(4+(2*x)), column=0)
            nodatalabel = tk.Label(self, text='No Team Data found!').grid(row=13, column=0) #tells the user they have a free team

        else:
            noteamslabel = tk.Label(self, text="No teams created!", font=mediumfont, bg='#b5fff2').grid(row=3, column=0)
            #if they have no teams, this tells them so.

class CasualBattleMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')
        titlelabel = tk.Label(self, text='Casual Battle', font=largefont, bg='#b5fff2').pack()
        teamlabel = tk.Label(self, text='Choose a team to use while playing:', bg='#b5fff2').pack()

        getteambutton = ttk.Button(self, text='Get teams', command= lambda: self.getcasualteams(lgb.globalID)).pack()
        returnbutton = ttk.Button(self, text="Return to main menu", command= lambda: controller.show_frame(PlayMenu)).place(x=0, y=0)
        self.playbutton = ttk.Button(self, text='Play!', command = lambda: controller.show_frame(BattleScreen))

    def getcasualteams(self, userID):
        fetchedteams=getbattleteams(userID)
        self.choice = StringVar()
        teamchoice = tk.OptionMenu(self, self.choice, *fetchedteams).pack()
        self.choice.set('Choose a team')
        self.playbutton.pack()

class BattleScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#b5fff2')
        #menubox = tk.Canvas(self, width=1000, height=800).place(x=0, y=0)
        self.gamestate = True
        movemenulabel = tk.Label(self, text="What would you like to do?", font=largefont, bg='#b5fff2').place(x=50, y=400)
        self.move1 = tk.Button(self, text="Move 1", font=largefont, command= lambda : self.attacksequence(0))
        self.move1.place(x=50, y=470)
        self.move2 = tk.Button(self, text="Move 2", font=largefont, command= lambda : self.attacksequence(1))
        self.move2.place(x=200, y=470)

        availablemons = tk.Label(self, text="Choose the monster to switch to!", bg='#b5fff2').place(x=50, y= 520)
        self.monbutton0 = ttk.Button(self, text = fc.me.monsters[0].name, command= lambda:self.switchsequence(0))
        self.monbutton0.place(x=50, y=570)
        self.monbutton1 = ttk.Button(self, text = fc.me.monsters[1].name, command= lambda:self.switchsequence(1))
        self.monbutton1.place(x=120, y=570)
        self.monbutton2 = ttk.Button(self, text = fc.me.monsters[2].name, command= lambda:self.switchsequence(2))
        self.monbutton2.place(x=190, y=570)
        self.monbutton3 = ttk.Button(self, text = fc.me.monsters[3].name, command= lambda:self.switchsequence(3))
        self.monbutton3.place(x=260, y=570)

        self.mymonhealth = tk.Label(self, text = fc.me.get_monster().health, font = largefont, bg='#b5fff2')
        self.mymonhealth.place(x=50, y=70)
        self.mymonname = tk.Label(self, text=fc.me.get_monster().name, font=largefont, bg='#b5fff2')
        self.mymonname.place(x=50, y=40)

        self.enemymonhealth = tk.Label(self, text = fc.enemy.get_monster().health, font=largefont, bg='#b5fff2')
        self.enemymonhealth.place(x=280, y=70)
        self.enemymonname = tk.Label(self, text=fc.enemy.get_monster().name, font=largefont, bg='#b5fff2')
        self.enemymonname.place(x=280, y=40)
        #while self.gamestate == True:
        self.updatesprites()
        self.updateinfo()

        self.returntomenu = tk.Button(self, text="Return to main menu", command = lambda: controller.show_frame(PlayMenu))

    def updateinfo(self):
        self.mymonhealth.config(text=fc.me.get_monster().health)
        self.enemymonhealth.config(text=fc.enemy.get_monster().health)
        self.move1.config(text=fc.me.get_monster().moves[0].atkname)
        self.move2.config(text=fc.me.get_monster().moves[1].atkname)
        self.mymonname.config(text=fc.me.get_monster().name)
        self.enemymonname.config(text=fc.enemy.get_monster().name)

        self.mymonhealth.after(100, self.updateinfo)

        if fc.enemy.get_monster().state == False: #checks if the current monster
            enmalive = True     #still alive
            for i in range(len(fc.enemy.monsters)): #iterates through the enemy monsters
                if fc.enemy.monsters[i-1].state == True: #finds the next live monster
                    fc.enemy.switchmon(i-1) #switches to this monster
                    self.updatesprites()
                    enmalive = True
                    break #breaks the loop
                else:
                    enmalive = False #if none are found this boolean turns false

            if enmalive != True: #if the boolean is false, the user receives a victory screen
                victorylabel = tk.Label(self, text="You Win!", font = "Calibri, 60").place(x=70
                , y=100)
                self.move1.config(state='disabled')
                self.move2.config(state='disabled')
                self.monbutton0.config(state='disabled')
                self.monbutton1.config(state='disabled')
                self.monbutton2.config(state='disabled')
                self.monbutton3.config(state='disabled')
                try:
                    cbb.updateelo(lgb.globalID, True) #called when the user wins
                except:
                    pass #the function errors once it has been called once
                self.returntomenu.place(x=165, y=360)
                self.gamestate = False #the return to menu button now appears
                #all buttons are disabled so that the user cannot keep trying to click things

        if fc.me.get_monster().state == False:
            mealive = True #exactly the same as before except now the user's monsters are iterated through
            for i in range(len(fc.me.monsters)):
                if fc.me.monsters[i-1].state == True:
                    fc.me.switchmon(i-1)
                    self.updatesprites()
                    mealive = True
                    break
                else:
                    mealive = False

            if mealive != True: #a defeat label is placed
                defeatlabel = tk.Label(self, text="You Lose...", font = "Calibri, 60").place(x=70, y=100)
                self.move1.config(state='disabled')
                self.move2.config(state='disabled')
                self.monbutton0.config(state='disabled')
                self.monbutton1.config(state='disabled')
                self.monbutton2.config(state='disabled')
                self.monbutton3.config(state='disabled')
                try:
                    cbb.updateelo(lgb.globalID, False) #if the user loses this is called
                except:
                    pass #after 1 run of the code this function now errors as the databsae is locked
                self.returntomenu.place(x=165, y=360) #return to menu button now appears
                self.gamestate = False
                #All buttons are disabled to make sure the user cannot keep trying to click things
    def attacksequence(self, atknum):
        fc.enemy.take_damage(fc.me.get_monster().moves[atknum].overall_damage(fc.me.get_monster().moves[atknum].damage,
        fc.me.get_monster().monAttack, fc.enemy.get_monster().monType))
        #The above causes damage to the opponent, while the below calls the function that will cause damage to the user
        if fc.enemy.get_monster().state == True: #checks if the opponent is still alive
            self.opponentresponse()
        else:
            pass

    def switchsequence(self, newmon):
        fc.me.switchmon(newmon)
        self.updatesprites()
        #The above switches the current active creature, while the below calls the function that will cause damage to the user
        self.opponentresponse()

    def opponentresponse(self):
        enemychoice1 = fc.enemy.get_monster().moves[0].get_attack_modifier(fc.enemy.get_monster().moves[0].type, fc.me.get_monster().monType)
        enemychoice2 = fc.enemy.get_monster().moves[1].get_attack_modifier(fc.enemy.get_monster().moves[1].type, fc.me.get_monster().monType)
        #grabs the modifier of each move to determine which of the moves to use
        if enemychoice1 >= enemychoice2: #compares the moves and deals the damage
            fc.me.take_damage(fc.enemy.get_monster().moves[0].overall_damage(fc.enemy.get_monster().moves[0].damage,
            fc.enemy.get_monster().monAttack, fc.me.get_monster().monType))
        else:
            fc.me.take_damage(fc.enemy.get_monster().moves[1].overall_damage(fc.enemy.get_monster().moves[1].damage,
            fc.enemy.get_monster().monAttack, fc.me.get_monster().monType))

    def updatesprites(self):
        self.myload = Image.open(fc.me.get_monster().sprite) #loads the image
        self.myload = self.myload.resize((200, 200), Image.ANTIALIAS) #resizes the image
        self.mysprite = ImageTk.PhotoImage(self.myload) #places the resized image into a tkinter format
        self.myspritelabel = tk.Label(self, image = self.mysprite, bg='#b5fff2') #creates the label
        self.myspritelabel.place(x=10, y=110)

        self.enmload = Image.open(fc.enemy.get_monster().sprite) #repeat of above, adapted for the enemy
        self.enmload = self.enmload.resize((200, 200), Image.ANTIALIAS)
        self.enmsprite = ImageTk.PhotoImage(self.enmload)
        self.enmspritelabel = tk.Label(self, image=self.enmsprite, bg='#b5fff2')
        self.enmspritelabel.place(x=250, y=110)


app = SolaireGUI()
app.mainloop()
