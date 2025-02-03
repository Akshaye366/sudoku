import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk


from config import config
from frame import Frame
    

class AchievementsPage(Frame):
    def __init__(self, app, window):
        self.app = app
        super().__init__(window)
        super().exiting()
        self.createWidgets()
        super().packFrame()

    def initialiseStats(self):
        conn = sqlite3.connect('user.db')#Opens database
        cursor = conn.cursor()
        cursor.execute("SELECT mistakes FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.mistakes = cursor.fetchall()[0][0]
        cursor.execute("SELECT correctEntries FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.correctEntries = cursor.fetchall()[0][0]
        cursor.execute("SELECT bestSolve FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.bestSolve = cursor.fetchall()[0][0]
        cursor.execute("SELECT totalHints FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches difficulty from users
        self.totalHints = cursor.fetchall()[0][0]
        cursor.execute("SELECT easySolves FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches difficulty from users
        self.easySolves = cursor.fetchall()[0][0]
        cursor.execute("SELECT loadAmount FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches difficulty from users
        self.loadAmount = cursor.fetchall()[0][0]
        conn.commit()
        conn.close()#Close database

    def createWidgets(self):
        self.initialiseStats()
        self.achievementsHeader = tk.Label(self.frame, text="Achievements", font=("Ariel", 20, "bold"))#Achievements Header
        self.achievementsHeader.place(x=230, y=20)#Header position
        milestone1 = tk.Label(self.frame, text="Mistake merchant", font=("Helvetica", 13, "bold"))#Achievement label
        milestone1.place(relx=0.05, rely=0.21)#Achievement position
        description1 = tk.Label(self.frame, text="Make a total of 100 mistakes", font=("Helvetica", 13))#Description label
        description1.place(relx=0.05, rely=0.24)#Description position
        milestone1Stat = tk.Label(self.frame, text=str(self.mistakes)+"/100", font=("Helvetica", 13))#Milestone counter label
        milestone1Stat.place(relx=0.76, rely=0.24)#Counter position

        progressBar = ttk.Progressbar(self.frame, length=480)#Progress bar
        if self.mistakes < 100:#If milestone not completed
            progressBar.step(self.mistakes)#Increment progress bar
            image1 = Image.open('Photoicons/incomplete.png').resize((30, 30), True)
        else:
            image1 = Image.open('Photoicons/complete.png').resize((30, 30), True)
            progressBar.step(99.999)#Completed progress bar
        progressBar.place(relx=0.05, rely=0.28)#Progress bar position

        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self.frame, image=test, border=False)
        label1.image = test
        label1.place(relx=0.88, rely=0.27)

        milestone2 = tk.Label(self.frame, text="I love sudoku", font=("Helvetica", 13, "bold"))#Achievement label
        milestone2.place(relx=0.05, rely=0.33)#Achievement position
        description2 = tk.Label(self.frame, text="Make a total of 1000 correct entries", font=("Helvetica", 13))#Description label
        description2.place(relx=0.05, rely=0.36)#Description position
        milestone2Stat = tk.Label(self.frame, text=str(self.correctEntries)+"/1000", font=("Helvetica", 13))#Milestone counter label
        milestone2Stat.place(relx=0.74, rely=0.36)#Counter position

        progressBar2 = ttk.Progressbar(self.frame, maximum=1000, length=480)#Progress bar
        if self.correctEntries < 1000:#If milestone not completed
            progressBar2.step(self.correctEntries)#Increment progress bar
            image1 = Image.open('Photoicons/incomplete.png').resize((30, 30), True)
        else:
            image1 = Image.open('Photoicons/complete.png').resize((30, 30), True)
            progressBar2.step(999.999)#Completed progress bar
        progressBar2.place(relx=0.05, rely=0.40)#Progress bar position

        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self.frame, image=test, border=False)
        label1.image = test
        label1.place(relx=0.88, rely=0.39)

        milestone3 = tk.Label(self.frame, text="Clueless", font=("Helvetica", 10, "bold"))#Achievement label
        milestone3.place(relx=0.05, rely=0.45)#Achievement position
        description3 = tk.Label(self.frame, text="Use a total of 20 hints", font=("Helvetica", 13))#Description label
        description3.place(relx=0.05, rely=0.48)#Description position
        milestone3Stat = tk.Label(self.frame, text=str(self.totalHints)+"/20", font=("Helvetica", 13))#Milestone counter label
        milestone3Stat.place(relx=0.78, rely=0.48)#Counter position

        progressBar3 = ttk.Progressbar(self.frame, maximum=20, length=480)#Progress bar
        if self.totalHints < 20:#If milestone not completed
            progressBar3.step(self.totalHints)#Increment progress bar
            image1 = Image.open('Photoicons/incomplete.png').resize((30, 30), True)
        else:
            image1 = Image.open('Photoicons/complete.png').resize((30, 30), True)
            progressBar3.step(999.999)#Completed progress bar
        progressBar3.place(relx=0.05, rely=0.52)#Progress bar position    
        
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self.frame, image=test, border=False)
        label1.image = test
        label1.place(relx=0.88, rely=0.51)
        
        milestone4 = tk.Label(self.frame, text="Genius", font=("Helvetica", 13, "bold"))#Achievement label
        milestone4.place(relx=0.05, rely=0.57)#Achievement position
        description3 = tk.Label(self.frame, text="Achieve a solving statistic of 0.9", font=("Helvetica", 13))#Description label
        description3.place(relx=0.05, rely=0.60)#Description position
        milestone4Stat = tk.Label(self.frame, text=str(self.bestSolve)+"/0.9", font=("Helvetica", 13))#Milestone counter label
        milestone4Stat.place(relx=0.76, rely=0.60)#Counter position

        progressBar4 = ttk.Progressbar(self.frame, maximum=0.9, length=480)#Progress bar
        if self.bestSolve < 0.9:#If milestone not completed
            progressBar4.step(self.bestSolve)#Increment progress bar
            image1 = Image.open('Photoicons/incomplete.png').resize((30, 30), True)
        else:
            image1 = Image.open('Photoicons/complete.png').resize((30, 30), True)
            progressBar4.step(0.8999)#Completed progress bar
        progressBar4.place(relx=0.05, rely=0.64)#Progress bar position

        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self.frame, image=test, border=False)
        label1.image = test
        label1.place(relx=0.88, rely=0.63)

        milestone5 = tk.Label(self.frame, text="Devoted", font=("Helvetica", 13, "bold"))#Achievement label
        milestone5.place(relx=0.05, rely=0.69)#Achievement position
        description5 = tk.Label(self.frame, text="Play and complete 100 puzzles", font=("Helvetica", 13))#Description label
        description5.place(relx=0.05, rely=0.72)#Description position
        milestone5Stat = tk.Label(self.frame, text=str(self.loadAmount)+"/100", font=("Helvetica", 13))#Milestone counter label
        milestone5Stat.place(relx=0.76, rely=0.72)#Counter position

        progressBar5 = ttk.Progressbar(self.frame, length=480)#Progress bar
        if self.loadAmount < 100:#If milestone not completed
            progressBar5.step(self.loadAmount)#Increment progress bar
            image1 = Image.open('Photoicons/incomplete.png').resize((30, 30), True)
        else:
            image1 = Image.open('Photoicons/complete.png').resize((30, 30), True)
            progressBar5.step(99.999)#Completed progress bar
        progressBar5.place(relx=0.05, rely=0.76)#Progress bar position  

        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(self.frame, image=test, border=False)
        label1.image = test
        label1.place(relx=0.88, rely=0.75)

        milestone6 = tk.Label(self.frame, text="Rookie", font=("Helvetica", 13, "bold"))#Achievement label
        milestone6.place(relx=0.05, rely=0.81)#Achievement position
        description6 = tk.Label(self.frame, text="Complete 10 puzzles on easy difficulty", font=("Helvetica", 13))#Description label
        description6.place(relx=0.05, rely=0.84)#Description position
        milestone6Stat = tk.Label(self.frame, text=str(self.easySolves)+"/10", font=("Helvetica", 13))#Milestone counter label
        milestone6Stat.place(relx=0.79, rely=0.84)#Counter position

        progressBar6 = ttk.Progressbar(self.frame, maximum=10, length=480)#Progress bar
        if self.easySolves < 10:#If milestone not completed
            progressBar6.step(self.easySolves)#Increment progress bar
            completion = Image.open('Photoicons/incomplete.png').resize((30, 30), True)#Incomplete icon
        else:
            completion = Image.open('Photoicons/complete.png').resize((30, 30), True)#Complete icon
            progressBar6.step(9.999)#Completed progress bar
        progressBar6.place(relx=0.05, rely=0.88)#Progress bar position  

        completionImage = ImageTk.PhotoImage(completion)#Completion
        imageLabel = tk.Label(self.frame, image=completionImage, border=False)#Icon image label
        imageLabel.image = completionImage
        imageLabel.place(relx=0.88, rely=0.87)#Icon placement

        if (self.mistakes >= 100) and (self.correctEntries >= 1000) and (self.totalHints >= 20) and (self.bestSolve >= 0.9) and (self.loadAmount >= 100) and (self.easySolves >= 10):#All achievements complete
            medal = Image.open('Photoicons/medal.png').resize((60, 60), True)#medal icon
            medalImage = ImageTk.PhotoImage(medal)#Medal
            imageLabel = tk.Label(self.frame, image=medalImage, border=False)#Icon image label
            imageLabel.image = medalImage
            imageLabel.place(relx=0.8, rely=0.1)#Icon placement
