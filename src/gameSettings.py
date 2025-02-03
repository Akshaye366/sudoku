class GameSettings:
    def __init__(self):
        self.theme = 0
        self.hints = 3
        self.difficulty = 2
        self.timer = 4

    def setTheme(self, value):
        self.theme = value
        
    def setHints(self, value):
        self.hints = value

    def setDifficulty(self, value):
        self.difficulty = value

    def setTimer(self, value):
        self.timer = value

    def getTheme(self):
        return self.theme
        
    def getHints(self):
        return self.hints

    def getDifficulty(self):
        return self.difficulty
    
    def getTimer(self):
        return self.timer
    
    def getAllSettings(self):
        self.allSettings = f"""
        Theme: {self.theme}
        Hints: {self.hints}
        Difficulty: {self.difficulty}
        Timer: {self.timer}
        """#string to display all the game settings
                #FINISH
        return self.allSettings
