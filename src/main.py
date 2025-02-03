import tkinter as tk
import sqlite3
import pygame

from gameSettings import GameSettings
from loginPage import LoginPage
from menuPage import MenuPage
from masterSudoku import SudokuGame
from statsPage import StatsPage
from achievementsPage import AchievementsPage
from tipsPage import TipsPage
from settingsPage import SettingsPage

    
class MasterSudoku: 
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Master Sudoku')
        self.window.minsize(600, 600)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.currentFrame = None
        self.initDatabase()
        self.runLoginPage()
        self.settings = GameSettings()

    def initDatabase(self):
        conn = sqlite3.connect('user.db')#Open database
        cursor = conn.cursor()

        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS "users" (
            "username"	TEXT DEFAULT 'Akshaye',
            "passwords"	TEXT,
            "hints"	INTEGER,
            "difficulty"	INTEGER,
            "timer"	INTEGER,
            "mistakes"	INTEGER,
            "correctEntries"	INTEGER,
            "bestTime"	INTEGER,
            "bestSolve"	INTEGER,
            "totalHints"	INTEGER,
            "loadAmount"	INTEGER,
            "easySolves"	INTEGER,
            "theme"	INTEGER)
        ''')
        conn.commit()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS "graphing" (
            "username"	TEXT,
            "y0"	INTEGER,
            "y1"	INTEGER,
            "y2"	INTEGER,
            "y3"	INTEGER,
            "y4"	INTEGER,
            "y5"	INTEGER,
            "y6"	INTEGER,
            "y7"	INTEGER,
            "y8"	INTEGER,
            "y9"	INTEGER,
            "y10"	INTEGER
        )            
        ''')
        conn.commit()
        conn.close()

    def runGame(self):
        self.window.mainloop()

    def runSudoku(self):
        pygame.init()
        game = SudokuGame(self, self.settings)

    def runLoginPage(self):
        if self.currentFrame: self.currentFrame.removeFrame()
        self.currentFrame = LoginPage(self, self.window)

    def runStatsPage(self):
        if self.currentFrame: self.currentFrame.removeFrame()
        self.currentFrame = StatsPage(self, self.window, self.settings)

    def runAchievementsPage(self):
        if self.currentFrame: self.currentFrame.removeFrame()
        self.currentFrame = AchievementsPage(self, self.window)
    
    def runMenuPage(self):
        if self.currentFrame: self.currentFrame.removeFrame()
        self.currentFrame = MenuPage(self, self.window)

    def runTipsPage(self):
        if self.currentFrame: self.currentFrame.removeFrame()
        self.currentFrame = TipsPage(self, self.window)

    def runSettingsPage(self):
        if self.currentFrame: self.currentFrame.removeFrame()
        self.currentFrame = SettingsPage(self, self.window, self.settings)

    def quit(self):
        for self.widget in self.currentFrame.frame.winfo_children():
            self.widget.destroy()
        self.currentFrame.removeFrame()
        self.window.quit()
        self.window.destroy()


if __name__ == "__main__":
    app = MasterSudoku()
    app.runGame()