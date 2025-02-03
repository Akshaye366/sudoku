import tkinter as tk
from PIL import Image, ImageTk


from config import config
from frame import Frame

class MenuPage(Frame):
    def __init__(self, app, window):
        super().__init__(window)
        self.app = app
        super().minimumSize()
        self.createWidgets()
        self.exiting()
        super().packFrame()

    def createWidgets(self):

        self.sudoku_header = tk.Label(self.frame, text="Master Sudoku", font=("Helvetica", 20, "bold"))#Sudoku Header Label
        self.sudoku_header.place(x=227, y=100)

        self.play_sudoku = tk.Button(self.frame, text="Play sudoku", command=self.app.runSudoku,width=30, font=("Helvetica", 14))#Play sudoku label
        self.play_sudoku.place(x=157, y=150)  

        if config.getUsername() != None:
            self.stats_Button = tk.Button(self.frame, text="Statistics", command=self.app.runStatsPage, width=30, font=("Helvetica", 14))#Stats label
            self.Achievements_Button = tk.Button(self.frame, text="Achievements", command=self.app.runAchievementsPage, width=30, font=("Helvetica", 14))#Achievements label
        else:
            self.stats_Button = tk.Button(self.frame, text="Statistics", command=self.app.runStatsPage, width=30, state="disabled", font=("Helvetica", 14))#Stats label
            self.Achievements_Button = tk.Button(self.frame, text="Achievements", command=self.app.runAchievementsPage, width=30, state='disabled', font=("Helvetica", 14))#Achievements label
        
        self.stats_Button.place(x=157, y=190)
        self.Achievements_Button.place(x=157, y=230)

        self.Tips_Button = tk.Button(self.frame, text="Game tips & tricks", command=self.app.runTipsPage ,width=30, font=("Helvetica", 14))#Tips label
        self.Tips_Button.place(x=157, y=270)

        Settings_Button = tk.Button(self.frame, text="Settings", command=self.app.runSettingsPage, width=30, font=("Helvetica", 14))#Settings label
        Settings_Button.place(x=157, y=310)

        self.Quit_Button = tk.Button(self.frame, text="Quit Game", command=self.app.quit, width=30, font=("Helvetica", 14))#Quit label
        self.Quit_Button.place(x=157, y=350)

        if config.username != None:
            self.usernameLabel = tk.Label(self.frame, text=str(config.getUsername()))#Sudoku Header Label
            self.usernameLabel.place(x=187, y=403)
        else:
            self.noStats = tk.Label(self.frame, text="The statistics and achievement pages are \nnot available for guest users.")
            self.noStats.place(x=158, y=550)

        self.user = Image.open('Photoicons/user.png').resize((24, 24), True)#Icon file path
        self.userImage = ImageTk.PhotoImage(self.user)
        self.userPhoto = tk.Label(self.frame, image=self.userImage)#Icon set as label
        self.userPhoto.image = self.userImage
        self.userPhoto.place(x=158, y=400)

    def exiting(self):
        self.exitButton = Image.open('Photoicons/exit.png').resize((30, 30), True)#Icon file path
        self.exit = ImageTk.PhotoImage(self.exitButton)
        self.exitButton = tk.Label(self.frame, image=self.exit)#Icon set as label
        self.exitButton.image = self.exit
        self.exitButton.place(x=20,y=20)

        def ExitButton(event):
            config.removeUsername()
            self.app.runLoginPage()

        # Bind the click event to the label
        self.exitButton.bind("<Button-1>", ExitButton)
