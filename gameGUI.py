import tkinter as tk
from tkinter import ttk

smallfont = ("Calibri", 8)
mediumfont = ("Calibri", 10)
largefont = ("Calibri", 12)
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

        for F in (LoginPage, MainMenu, PlayMenu, MenuSettings):

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
        tk.Frame.__init__(self, parent)
        loginlabel = tk.Label(self, text="Login To Solaire!", font=largefont)
        loginlabel.pack(pady=10, padx=10)

        usernamelabel = tk.Label(self, text="Username:", font=smallfont)
        usernamelabel.pack()
        usernamebox = tk.Entry(self, width=15)
        usernamebox.pack(pady=10, padx=10)

        passwordlabel = tk.Label(self, text="Password:", font=smallfont)
        passwordlabel.pack()
        passwordbox = tk.Entry(self, show="*", width=15)
        passwordbox.pack(pady=10, padx=10)

        loginbutton = ttk.Button(self, text="Log In!", command=lambda: controller.show_frame(MainMenu))
        loginbutton.pack()

        exitbutton = ttk.Button(self, text="Exit", command=lambda: quit(self))
        exitbutton.pack()


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

        casualbattle = tk.Button(self, text="Casual Battle", font=buttonfont, command = None)
        casualbattle.configure(width=60, height =7)
        casualbattle.grid(row=1, column=0, padx=20)

        competitivebattle = tk.Button(self, text="Competitive Battle", font=buttonfont, command = None)
        competitivebattle.configure(width=60, height = 7)
        competitivebattle.grid(row=2, column=0, pady=20, padx=20)

        teambuilder = tk.Button(self, text="Team Builder", font=buttonfont, command = None)
        teambuilder.configure(width=60, height =7)
        teambuilder.grid(row=3, column=0, padx=20)

        leaderboard = tk.Button(self, text="Leaderboard", font=buttonfont, command = None)
        leaderboard.configure(width=60, height =7)
        leaderboard.grid(row=4, column=0, pady=20, padx=20)

class MenuSettings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        settingstitle = tk.Label(self, text="Settings", font=largefont)
        settingstitle.grid(row=0, column=0)







app = SolaireGUI()
app.mainloop()
