
import tkinter as tk
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import config
from frame import Frame

    

class StatsPage(Frame):
    def __init__(self, app, window, settings):
        super().__init__(window)
        self.app = app
        self.settings = settings
        self.window.minsize(800,600)
        self.height = self.window.winfo_height()
        self.width = self.window.winfo_width()
        if self.height < 600: self.height = 600
        if self.width < 800: self.width = 800
        self.window.geometry(str(self.width)+"x"+str(self.height))

        self.mistakes = 0
        self.correctEntries = 0
        self.totalHints = 0
        self.bestSolve = 0
        self.solvingStatistic = 0
        self.yvalues = []

        self.createWidgets()
        self.createGraph()
        super().exiting()
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
        cursor.execute("SELECT * FROM graphing WHERE username = ?", (str(config.getUsername()),))#Fetches difficulty from users
        graphdata = cursor.fetchall()
        for i in range(1, 12): # Takes all but first value in database which is username
            self.yvalues.append(graphdata[0][i])
        self.solvingStatistic = self.yvalues[-1]
        conn.commit()
        conn.close()#Close database

    def createGraph(self):
        xvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
        fig, ax= plt.subplots(figsize=(6,3)) # Graph axes dimensions  9.25, 2.5
        ax.spines['bottom'].set_color('black')
        #ax.spines['top'].set_color(config.DEFAULTCOLOUR)
        #ax.spines['right'].set_color(config.DEFAULTCOLOUR)
        ax.spines['left'].set_color('black')

        #ax.set_facecolor(config.DEFAULTCOLOUR)
        #fig.set_facecolor(config.DEFAULTCOLOUR)
        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')

        ax.plot(xvalues, self.yvalues, linewidth=2, color='green')
        ax.grid(True, color='black', linestyle='--', linewidth=1)  # Lighter grid lines

        x = np.array(xvalues)
        y = np.array(self.yvalues)
        horizontal, vertical = np.polyfit(x, y, 1)
        plt.plot(x, horizontal*x+vertical)
        plt.xlim(0, 10)
        plt.ylim(0, 1)
        fig.tight_layout(pad=2.0)  # Increase padding between plot and labels to prevent cutting

        ax.set_xlabel('Time (minutes)', fontsize=12, color='black')
        ax.set_ylabel('Solving rate', fontsize=12, color='black')

        plt.title('Solving Statistic')

        ax.yaxis.label.set_color('black')
        ax.xaxis.label.set_color('black')
        ax.title.set_color('black')

        self.start_x = self.window.winfo_width() // 2
        self.start_y = self.window.winfo_height() // 2

        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.get_tk_widget().place(x=0, y=100)
        canvas.draw()
    
    def createWidgets(self):
        if config.getUsername() != None:
            self.initialiseStats()
        self.Statistics_header = tk.Label(self.frame, text="Statistics", fg='black', font=("Ariel", 20))
        self.Statistics_header.place(x=250, y=20)
        self.Totalmistakes_label = tk.Label(self.frame, text="Total Mistakes: "+str(self.mistakes), fg='black', font=("Ariel", 15))
        self.Totalmistakes_label.place(x=10, y=440)
        self.TotalcorrectEntries_label = tk.Label(self.frame, text="Total correct entries: "+str(self.correctEntries), fg='black', font=("Ariel", 15))
        self.TotalcorrectEntries_label.place(x=400, y=440)
        self.Solvingstatistic_label = tk.Label(self.frame, text="Current solving statistic: "+str(self.solvingStatistic), fg='black', font=("Ariel", 15))
        self.Solvingstatistic_label.place(x=10, y=480)
        self.Bestsolve_label = tk.Label(self.frame, text="Best solving statistic: "+str(self.bestSolve), fg='black', font=("Ariel", 15))
        self.Bestsolve_label.place(x=10, y=520)
        self.hintsUsed_label = tk.Label(self.frame, text="Total hints used: "+str(self.totalHints), fg='black', font=("Ariel", 15))
        self.hintsUsed_label.place(x=400, y=480)
