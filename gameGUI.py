import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
from loginbackend import loginprocess, registeringprocess
from leaderboardbackend import fetchplayers
from teambuilderbackend import fetchcreatures

smallfont = ("Calibri", 8)
mediumfont = ("Calibri", 10)
largefont = ("Calibri", 16)
titlefont = ("Calibri", 18)
buttonfont = ("Calibri", 15)

class SolaireGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #tk.Tk.iconbitmap(Self, default="")
        tk.Tk.wm_title(self, "Solaire")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, MainMenu, PlayMenu, RegisterPage, MenuSettings, TeamBuilderPage, LeaderboardPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(TeamBuilderPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def quitprogram(self):
        tk.Tk.destroy()

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        loginlabel = tk.Label(self, text="Login To Solaire!", font=titlefont)
        loginlabel.pack(pady=10, padx=10)

        usernamelabel = tk.Label(self, text="Username:", font=smallfont)
        usernamelabel.pack()
        usernamebox = tk.Entry(self, width=15)
        usernamebox.pack(pady=10, padx=10)


        passwordlabel = tk.Label(self, text="Password:", font=smallfont)
        passwordlabel.pack()
        passwordbox = tk.Entry(self, show="*", width=15)
        passwordbox.pack(pady=10, padx=10)


        loginbutton = ttk.Button(self, text="Log In!", command=lambda: self.logincommand(controller, usernamebox.get(), passwordbox.get()))
        loginbutton.pack()

        exitbutton = ttk.Button(self, text="Exit", command=lambda: quit(self))
        exitbutton.pack()

        registerlabel = tk.Label(self, text="New to Solaire?", font=largefont)
        registerbutton = ttk.Button(self, text="Register!", command=lambda: controller.show_frame(RegisterPage))
        registerlabel.pack()
        registerbutton.pack()
    def logincommand(self, controller, username, password): #Lets the button run two functions
        if loginprocess(username, password) == True: #Verifies whether the login was successful
            controller.show_frame(MainMenu) #Pushes the program forward if bad login

class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        registertitle = tk.Label(self, text="Sign Up to Solaire", font=titlefont)
        registertitle.grid(row=0, column=0)

        usernamelabel = tk.Label(self, text="Username:", font=smallfont)
        usernamelabel.grid(row=1, column=0,)
        usernamebox = tk.Entry(self, width=25)
        usernamebox.grid(rowspan=2, column=0, pady=10, padx=10)

        emailaddresslabel = tk.Label(self, text="Email Address:", font=smallfont)
        emailaddresslabel.grid(row=4, column=0)
        emailaddressbox = tk.Entry(self, width=25)
        emailaddressbox.grid(row=5, column=0)

        passwordlabel = tk.Label(self, text="Password:", font=smallfont)
        passwordlabel.grid(row=7, column=0)
        passwordbox = tk.Entry(self, show="*", width=25)
        passwordbox.grid(row=8, column=0, pady=10, padx=10)

        confirmpasswordlabel = tk.Label(self, text="Confirm Password:", font=smallfont)
        confirmpasswordlabel.grid(row=9, column=0)
        confirmpasswordbox = tk.Entry(self, show="*", width=25)
        confirmpasswordbox.grid(row=10, column=0, pady=10, padx=10)

        registerbutton = ttk.Button(self, text="Register now!", command=lambda: self.registercommand(controller, usernamebox.get(), emailaddressbox.get(), passwordbox.get(), confirmpasswordbox.get()))
        registerbutton.grid(row=11)

    def registercommand(self, controller, username, email, password, confirmpassword):
        if registeringprocess(username, email, password, confirmpassword) == True:
            controller.show_frame(MainMenu)


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="Solaire", font=largefont)
        title.pack(pady=10, padx=10)

        playbutton = ttk.Button(self, text="Play!", command=lambda: controller.show_frame(PlayMenu))
        playbutton.pack()

        settingsbutton = ttk.Button(self, text="Settings!", command=lambda: controller.show_frame(MenuSettings))
        settingsbutton.pack()

        returnbutton = ttk.Button(self, text="Quit!", command=lambda: quit(self))
        returnbutton.pack()

class PlayMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        returntomenu = ttk.Button(self, text="Return to menu", command = lambda: controller.show_frame(MainMenu))
        returntomenu.grid(row=0, sticky="W", pady=5)

        casualbattle = tk.Button(self, text="Casual Battle", font=mediumfont, command = None)
        casualbattle.configure(width=60, height =7)
        casualbattle.grid(row=1, column=0, padx=20)

        competitivebattle = tk.Button(self, text="Competitive Battle", font=mediumfont, command = None)
        competitivebattle.configure(width=60, height = 7)
        competitivebattle.grid(row=2, column=0, pady=20, padx=20)

        teambuilder = tk.Button(self, text="Team Builder", font=mediumfont, command = lambda: controller.show_frame(TeamBuilderPage))
        teambuilder.configure(width=60, height =7)
        teambuilder.grid(row=3, column=0, padx=20)

        leaderboard = tk.Button(self, text="Leaderboard", font=mediumfont, command = lambda: controller.show_frame(LeaderboardPage))
        leaderboard.configure(width=60, height =7)
        leaderboard.grid(row=4, column=0, pady=20, padx=20)

class MenuSettings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        settingstitle = tk.Label(self, text="Settings", font=largefont)
        settingstitle.grid(row=0, column=0)

        settingsseparator = ttk.Separator(self, orient="horizontal")
        settingsseparator.grid(row=1, column=1, sticky='E')

        returnbutton = ttk.Button(self, text="Return to Main Menu", command=lambda: controller.show_frame(MainMenu))
        returnbutton.grid(row=1, column=3)

class LeaderboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        returnbutton =  ttk.Button(self, text="Return to main menu",
            command = lambda: controller.show_frame(PlayMenu))
        returnbutton.grid(row=0, column =0, sticky="W")

        leaderboardtitle = ttk.Label(self, text="          The Leaderboard           ", font=titlefont)
        leaderboardtitle.grid(row=0, column=1)

        refreshbutton = ttk.Button(self, text="Refresh!", command= lambda: self.displayrankings())
        refreshbutton.grid(row=0, column=3, sticky="E") #Runs the functions again to refresh the database
        #in case of any new ELO gains.
        self.displayrankings() #Runs the display to generate rankings

    def displayrankings(self):
        players = fetchplayers() #assigns the return value of the function to a variable
        i = 0
        for name, elo in players:
            ttk.Label(self, text=f"{i+1}. {name}                    {elo}", font= largefont).grid(row=(1 + i), column=1)
            i += 1 #Creates a label for each of the data entries in players


class TeamBuilderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        returnbutton =  ttk.Button(self, text="Return to main menu",
            command = lambda: controller.show_frame(PlayMenu))
        returnbutton.grid(row=0, column =0, sticky="W")

        choices = fetchcreatures()

        self.choice1 = StringVar()
        self.choice1.set('Please Select...')
        self.choice1.trace('w', self.getchange1())

        self.choice2 = StringVar()
        self.choice2.set('Please Select...')
        self.choice2.trace('w', self.getchange2())

        self.choice3 = StringVar()
        self.choice3.set('Please Select...')
        self.choice3.trace('w', self.getchange3())

        self.choice4 = StringVar()
        self.choice4.set('Please Select...')
        self.choice4.trace('w', self.getchange4())

        monster1entry = tk.OptionMenu(self, self.choice1, *choices)
        monster1entry.grid(row=1, column=1)

        monster2entry = tk.OptionMenu(self, self.choice1, *choices)
        monster2entry.grid(row=2, column=1)

    def getchange1(self):
        self.choice1.get()
    def getchange2(self):
        self.choice2.get()
    def getchange3(self):
        self.choice3.get()
    def getchange4(self):
        self.choice4.get()





app = SolaireGUI()
app.mainloop()
