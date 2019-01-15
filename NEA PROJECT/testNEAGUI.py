from tkinter import *
import tkinter as tk

class titleScreen:

    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)

        self.gameTitle = tk.Label(self.frame, text = "Solaire", font = ('Verdana', 16), fg = 'Yellow')
        self.startButton = tk.Button(self.frame, text = "Click to start!", font = ('Verdana', 8), fg = 'Blue', bg = 'White', command = self.startGame)
        self.settingsButton = tk.Button(self.frame, text = "Settings", font = ('Verdana', 8), fg = 'Blue')
        self.quitButton = tk.Button(self.frame, text = 'Quit', font = ('Verdana', 8), fg = 'Red')

        self.frame.pack()
        self.gameTitle.pack()
        self.startButton.pack()
        self.settingsButton.pack()
        self.quitButton.pack()

    def startGame(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = mainMenuScreen(self.newWindow)




class mainMenuScreen:

    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)

        self.mainMenuTitle = tk.Label(self.frame, text = "Main Menu", font = ('Verdana', 16), fg = "Yellow")
        self.startCasual = tk.Button(self.frame, text = "Casual Play", font = ('Verdana', 12), fg = "Purple", highlightcolor = 'Blue')
        self.startCompetitive = tk.Button(self.frame, text = "Competitive Play", font = ("Verdana", 12), fg = 'Purple', highlightcolor = 'Blue')
        self.startTeamBuild = tk.Button(self.frame, text = 'Team Builder', font = ("Verdana", 12), fg = 'Purple')

        self.frame.pack()
        self.mainMenuTitle.pack()
        self.startCasual.pack()
        self.startCompetitive.pack()
        self.startTeamBuild.pack()

class teamBuilderMenuScreen:

    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)

        self.



def main():
    root = tk.Tk()
    app = titleScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
