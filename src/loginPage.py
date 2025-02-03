import tkinter as tk
import sqlite3
from PIL import Image, ImageTk

from config import config
from frame import Frame

class LoginPage(Frame):
    def __init__(self, app, window):
        super().__init__(window)
        self.app = app  
        self.frame.configure(width=600, height=600)
        super().minimumSize()
        self.existing = False
        self.existing2 = False
        self.createWidgets()

    def createWidgets(self):
        # Sudoku Image
        self.mainSudoku = Image.open('Photoicons/mainSudoku.png').resize((128, 128), True)#Icon file path
        self.SudokuImage = ImageTk.PhotoImage(self.mainSudoku)
        self.photoSudoku = tk.Label(self.frame, image=self.SudokuImage)#Icon set as label
        self.photoSudoku.image = self.SudokuImage
        self.photoSudoku.place(x=235,y=30)

        self.sudoku_header = tk.Label(self.frame, text="Master Sudoku", font=("Verdana", 20, "bold"))#Sudoku Header Label
        self.sudoku_header.place(x=213,y=170)

        # REGISTER 
        self.register_label = tk.Label(self.frame, text="Register", font=("Ariel", 16))#Register text
        self.register_label.place(x=130,y=220)
        
        self.regusernamelabel = tk.Label(self.frame, text="Name:")#Register username text
        self.regusernamelabel.place(x=130, y=260)

        self.regusernameEntry = tk.Entry(self.frame, highlightcolor="black", width=20)#Register username entry box
        self.regusernameEntry.place(x=250, y=257)

        self.regpasswordLabel = tk.Label(self.frame, text="Password:")#Register password text
        self.regpasswordLabel.place(x=130, y=290)

        self.regpasswordEntry = tk.Entry(self.frame, highlightcolor="black", width=20, show="*")#Register username entry box
        self.regpasswordEntry.place(x=250, y=287)

        self.confirmpasswordLabel = tk.Label(self.frame, text="Confirm Password:")#Register confirm password text
        self.confirmpasswordLabel.place(x=130, y=320)

        self.confirmpasswordEntry = tk.Entry(self.frame, highlightcolor="black", width=20, show="*")#Register confirm password entry box
        self.confirmpasswordEntry.place(x=250, y=317)

        self.registerButton = Image.open('Photoicons/submit.png').resize((30, 30), True)#Icon file path
        self.enter = ImageTk.PhotoImage(self.registerButton)
        self.registerButton = tk.Label(self.frame, image=self.enter)#Icon set as label
        self.registerButton.image = self.enter
        self.registerButton.place(x=400,y=355)


        # Bind the click event to the label
        self.registerButton.bind("<Button-1>", self.Register)

        # LOGIN
        self.loginLabel = tk.Label(self.frame, text="Login", font=("Ariel", 16))#Login text
        self.loginLabel.place(x=130, y=425)

        self.usernameLabel = tk.Label(self.frame, text="Username:")#Login username text
        self.usernameLabel.place(x=130, y=455)

        self.usernameEntry = tk.Entry(self.frame, highlightcolor="black", width=20)#Login username entry box
        self.usernameEntry.place(x=250, y=452)

        self.passwordLabel = tk.Label(self.frame, text="Password:")#Login password text
        self.passwordLabel.place(x=130, y=485)

        self.passwordEntry = tk.Entry(self.frame, highlightcolor="black", width=20, show="*")#Login password entry box
        self.passwordEntry.place(x=250, y=482)

        self.loginButton = Image.open('Photoicons/submit.png').resize((30, 30), True)#Icon file path
        self.enter = ImageTk.PhotoImage(self.loginButton)
        self.loginButton = tk.Label(self.frame, image=self.enter)#Icon set as label
        self.loginButton.image = self.enter
        self.loginButton.place(x=400,y=520)


        # Bind the click event to the label
        self.loginButton.bind("<Button-1>", self.Login)

        self.guestplay_label = tk.Label(self.frame, text="Play as guest", font=("Ariel", 10, "bold"))  # Changes the cursor to a hand to indicate it's clickable)
        self.guestplay_label.place(x=500, y=550)

        self.guestplay_label.bind("<Button-1>", self.guestPlay)
        super().packFrame()

    def guestPlay(self, event):
        self.app.runMenuPage()

    def Login(self, event):
        conn = sqlite3.connect('user.db')#Open database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()#All account data
        conn.commit()
        conn.close()
        self.username = self.usernameEntry.get()
        self.password = self.passwordEntry.get()
        for user in range(len(data)):
            if self.username == data[user][0] and self.password == data[user][1]: # Valid login
                if self.existing2 == True:
                    self.result2.destroy()
                self.result2 = tk.Label(self.frame, text="Successfully logged in\n Loading sudoku ....", fg='black')
                self.result2.place(x=220, y=540)
                config.setUsername(self.username)
                self.window.after(1500, self.app.runMenuPage)
                break
            elif self.username == data[user][0] and self.password != data[user][1]: # Username is correct but password doesn't match
                if self.existing2 == True:
                    self.result2.destroy()
                self.result2 = tk.Label(self.frame, text="Password incorrect", fg='black')
                self.result2.place(x=220, y=540)
                self.existing2 = True
                break
            elif self.username == "" or self.password == "": # Any fields left empty
                if self.existing2 == True:
                    self.result2.destroy()
                self.result2 = tk.Label(self.frame, text="Please do not leave\n any fields empty", fg='black')
                self.result2.place(x=220, y=540)
                self.existing2 = True
                break
            else: # Username/Account doesn't exist
                if self.existing2 == True:
                    self.result2.destroy()
                self.result2 = tk.Label(self.frame, text="Failed Login, try again", fg='black')
                self.result2.place(x=220, y=540)
                self.existing2 = True

    def Register(self, event):
        global result
        valid = True
        conn = sqlite3.connect('user.db')#Open database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()#All account data
        conn.commit()
        conn.close()
        self.username = self.regusernameEntry.get()
        self.password = self.regpasswordEntry.get()
        self.confpassword = self.confirmpasswordEntry.get()
        conn = sqlite3.connect('user.db')#Open database
        cursor = conn.cursor()

        for user in range(len(data)):# Checks if username is taken
            if self.username == data[user][0]:
                valid = False
                if self.existing == True:
                    result.destroy()
                result = tk.Label(self.frame, text="Username is already in use", fg='black')
                result.place(x=220, y=370)
                self.existing = True
        if self.confpassword != self.password:
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Passwords do not match", fg='black')
            result.place(x=220, y=370)
            self.existing = True
            valid = False
        elif self.password == "" or self.username == "":
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Please do not leave any\n fields empty", fg='black')
            result.place(x=220, y=370)
            self.existing = True
            valid = False
        elif self.username == "Guest":
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Username must not be Guest", fg='black')
            result.place(x=220, y=370)
            self.existing = True
            valid = False
        elif len(self.password)<=5:
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Password is too short", fg='black')
            result.place(x=220, y=370)
            self.existing = True
            valid = False
        elif len(self.username) > 15:
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Username must not be over\n 15 characters", fg='black')
            result.place(x=220, y=370)
            self.existing = True
            valid = False
        elif self.username == self.password:
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Username and password must\n not be the same", fg='black')
            result.place(x=220, y=370)
            self.existing=True
            valid = False
        if valid == True:#Correct details entered
            if self.existing == True:
                result.destroy()
            result = tk.Label(self.frame, text="Valid account entry\nLoading sudoku ....", fg='black')
            result.place(x=220, y=370)#Result label
            self.existing = True
            conn = sqlite3.connect('user.db')#Open database
            cursor = conn.cursor()
            cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [(str(self.username), str(self.password), 3, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0)])  # Sets account user values
            cursor.executemany("INSERT INTO graphing VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [(str(self.username), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)])#Sets account graphing values
            conn.commit()
            conn.close()
            config.setUsername(self.username)
            self.window.after(1500, self.app.runMenuPage)
