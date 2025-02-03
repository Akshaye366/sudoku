     
import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk


from config import config
from frame import Frame


class SettingsPage(Frame):
    def __init__(self, app, window, settings):
        self.app = app
        self.settings = settings
        super().__init__(window)
        self.createWidgets()
        super().exiting()
        super().packFrame()

    def createWidgets(self):
        self.header = tk.Label(self.frame, text="Settings", fg='black', font=("Ariel", 20, "bold"))
        self.header.place(x=255, y=25)

        # --- THEME --- #
        self.themeselectlabel = tk.Label(self.frame, text="Select theme", fg='black', font=("Ariel", 15, "bold"))
        self.themeselectlabel.place(x=50, y=70)
        """
        self.image1 = Image.open('Photoicons/themes.png').resize((30, 30), True)
        test = ImageTk.PhotoImage(self.image1)
        self.label1 = tk.Label(self.frame, image=test, bg=config.DEFAULTCOLOUR, border=False)
        self.label1.image = test
        self.label1.place(x=160, y=70)"""
        self.themeoptions = ['Default','Alpine','Greyscale','Hedge','Bloodshot','Contrast']
        self.combobox = ttk.Combobox(self.frame, values=self.themeoptions, state='readonly')#, textvariable=sel)
        self.combobox.set(self.themeoptions[self.settings.getTheme()])
        self.combobox.place(x=350, y=75)
        self.themeDescription = tk.Label(self.frame, text="Change up the feel of Master Sudoku with themes! Included are a range of", fg='black', font=("Ariel", 13))
        self.themeDescription.place(x=50, y=110)
        self.themeDescription2 = tk.Label(self.frame, text="themes so you can choose what suits your preference the best.", fg='black', font=("Helvetica", 13))
        self.themeDescription2.place(x=50, y=130)
        
        # --- HINTS --- #
        hintselectlabel = tk.Label(self.frame, text="Select hint amount", fg='black', font=("Ariel", 15, "bold"))
        hintselectlabel.place(x=50, y=160)#Select hint label    
        """
        image1 = Image.open('Photoicons/Hints.png').resize((30, 30), True)
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self.frame, image=test, bg=config.DEFAULTCOLOUR, border=False)
        label1.image = test
        label1.place(x=200, y=180)"""
        self.var0 = tk.IntVar() 
        checkbox0 = tk.Radiobutton(self.frame, fg='black', variable=self.var0, value=0, text="0 hints")#Radiobuttons
        checkbox1 = tk.Radiobutton(self.frame, fg='black', variable=self.var0, value=2, text="2 hints")
        checkbox2 = tk.Radiobutton(self.frame, fg='black', variable=self.var0, value=3, text="3 hints")
        checkbox3 = tk.Radiobutton(self.frame, fg='black', variable=self.var0, value=5, text="5 hints")
        checkbox4 = tk.Radiobutton(self.frame, fg='black', variable=self.var0, value=10, text="10 hints")
        checkboxes = [checkbox0, checkbox1, checkbox2, checkbox3, checkbox4]#List of buttons to be placed
        for i in range(len(checkboxes)):#Placing radiobuttons evenly
            checkboxes[i].place(x=80+98*i, y=210)     
        self.var0.set(self.settings.getHints())  # Correct way to select the default radio button
        self.hintDescription = tk.Label(self.frame, text="If you feel that a puzzle has stumped you, taking a hint will bring you closer", font=("Helvetica", 13))
        self.hintDescription.place(x=50, y=250)
        self.hintDescription2 = tk.Label(self.frame, text="to the final answer. Howoever, The use of hints is not advised and will lower", font=("Helvetica", 13))
        self.hintDescription2.place(x=50, y=270)
        self.hintDescription3 = tk.Label(self.frame, text="your solving statistic", font=("Helvetica", 13))
        self.hintDescription3.place(x=50, y=290)

        # --- DIFFICULTY --- #
        self.diffLabel = tk.Label(self.frame, text="Select Difficulty", fg='black', font=("Ariel", 15, "bold"))
        self.diffLabel.place(x=50, y=330)
        self.combobox2 = ttk.Combobox(self.frame, values=config.DIFFICULTIES, state='readonly')
        self.combobox2.set(config.DIFFICULTIES[self.settings.getDifficulty()])
        self.combobox2.place(x=350, y=335)
        self.diffDescription = tk.Label(self.frame, text="If you feel confident with the game of sudoku, increase the difficulty to test your", fg='black', font=("Helvetica", 13))
        self.diffDescription.place(x=50, y=365)
        self.diffDescription2 = tk.Label(self.frame, text="skill. Completing puzzles of higher difficulty creates a better solving statistic.", fg='black', font=("Helvetica", 13))
        self.diffDescription2.place(x=50, y=385)

        # --- TIMER --- #
        self.setTimelabel = tk.Label(self.frame, text="Adjuts timer (minutes)", fg='black', font=("Ariel", 15, "bold"))
        self.setTimelabel.place(x=50, y=425)#Adjust timer label
        self.slider = tk.Scale(self.frame, from_=3, to=6, resolution=0.5, length=190, relief="sunken", orient="horizontal", fg='black')#Slider input
        self.slider.place(x=352, y=430)
        self.slider.set(self.settings.getTimer())
        self.frame.update_idletasks()  # Forces UI update
        self.timerDescription = tk.Label(self.frame, text="If you feel as though the puzzle's are too hard, give yourself some extra time.", fg='black', font=("Helvetica", 13))
        self.timerDescription.place(x=50, y=480)
        self.timerDescription2 = tk.Label(self.frame, text="How fast you complete a puzzle makes a great difference on your solving statistic.", fg='black', font=("Helvetica", 13))
        self.timerDescription2.place(x=50, y=500)

        if config.getUsername() != None:
            conn = sqlite3.connect('user.db')#Opens database
            cursor = conn.cursor()
            cursor.execute("SELECT theme FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
            self.settings.setTheme(cursor.fetchall()[0][0])
            cursor.execute("SELECT hints FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
            self.settings.setHints(cursor.fetchall()[0][0])
            cursor.execute("SELECT difficulty FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches difficulty from users
            self.settings.setDifficulty(cursor.fetchall()[0][0])
            cursor.execute("SELECT timer FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
            self.settings.setTimer(cursor.fetchall()[0][0])
            conn.commit()
            conn.close()#Close database
            self.combobox.set(self.themeoptions[self.settings.getTheme()])
            self.var0.set(self.settings.getHints()) 
            self.combobox2.set(config.DIFFICULTIES[self.settings.getDifficulty()])
            self.slider.set(self.settings.getTimer())

        def save(): #Save settings button command
            """ 
            theme = self.themeoptions.index(self.combobox.get())#Gets selects theme chosen   
               
            cursor.execute("UPDATE users SET Themechoice = ? WHERE username = ?", (theme, str(username),))#Updates value in the database for theme
            if var0.get() or var0.get() == 0:#If combobox is updated or not
                if username != "Guest":
                    hintschoice = var0.get()#Hints chosen value
                    cursor.execute("UPDATE users SET allowedHints = ? WHERE username = ?", (hintschoice, str(username),))#Update hints fields
                else:
                    guestHints = var0.get()#Guest hints
            if username != "Guest":
                userDifficulty = difficulties.index(combobox2.get())
                cursor.execute("UPDATE users SET Difficulty = ? WHERE username = ?", (userDifficulty, str(username),))#Update Difficulty fields
            else:
                guestDifficulty = difficulties.index(combobox2.get())
            if username != "Guest":
                userTimer = slider.get()
                cursor.execute("UPDATE users SET Timer = ? WHERE username = ?", (userTimer, str(username),))
            else:
                guestTimer = slider.get()
            
            conn.commit()
            conn.close()#Close database"""
            print("\nALL:")
            conn = sqlite3.connect('user.db')#Opens database
            cursor = conn.cursor()    
            theme = self.themeoptions.index(self.combobox.get())
            hints = self.var0.get()
            difficulty = config.DIFFICULTIES.index(self.combobox2.get())
            timer = self.slider.get()
            self.settings.setTheme(theme)
            self.settings.setHints(hints)
            self.settings.setDifficulty(difficulty)
            self.settings.setTimer(timer)
            print(self.settings.getAllSettings())
            if config.getUsername() != None:
                cursor.execute("UPDATE users SET theme = ? WHERE username = ?", (theme, str(config.getUsername()),))#Updates theme field
                cursor.execute("UPDATE users SET hints = ? WHERE username = ?", (hints, str(config.getUsername()),))#Update hints field
                cursor.execute("UPDATE users SET difficulty = ? WHERE username = ?", (difficulty, str(config.getUsername()),))#Update difficulty field
                cursor.execute("UPDATE users SET timer = ? WHERE username = ?", (timer, str(config.getUsername()),))#Update timer field 
            conn.commit()
            conn.close()#Close database

        self.savebutton = tk.Label(self.frame, text="Save", fg='black', font=("Ariel", 15, "bold"))
        self.savebutton.place(x=450, y=537) # Adjust timer label
        image2 = Image.open('Photoicons/save.png').resize((30, 30), True)
        test = ImageTk.PhotoImage(image2)
        label2 = tk.Button(self.frame, image=test, command=save, border=False)
        label2.image = test
        label2.place(x=500, y=534)
