import sqlite3
import pygame
import userboard
import random as r

from config import config

class SudokuGame():
    def __init__(self, app, settings):
        self.app = app
        self.settings = settings
        self.window_width, self.window_height = 760, 650
        self.cell_size = 40
        self.grid_size = self.cell_size * 9
        self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
        self.window.fill(config.DEFAULTCOLOUR)
        self.labelfont = pygame.font.Font(None, 20)
        self.largefont = pygame.font.Font(None, 27)
        pygame.display.set_caption("Sudoku")
        self.centering()
        self.game()

    def centering(self):

        self.start_x = (self.window_width - self.grid_size) // 2
        self.start_y = (self.window_height - self.grid_size) // 2

    def generate(self):
        self.centering()
        # Draw the grid
        for i in range(0, self.grid_size + self.cell_size, self.cell_size):
            thickness = 3 if i % (self.cell_size * 3) == 0 else 1
            # Vertical lines
            pygame.draw.line(self.window, 'black', (self.start_x + i, self.start_y), (self.start_x + i, self.start_y + self.grid_size), thickness)
            # Horizontal lines
            pygame.draw.line(self.window, 'black', (self.start_x, self.start_y + i), (self.start_x + self.grid_size, self.start_y + i), thickness)

    def outline(self, row, col):
        x1 = (col * 40) + self.start_x
        y1 = (row * 40) + self.start_y
        outlined = pygame.Rect(x1, y1, 40, 40)
        pygame.draw.rect(self.window, ('red'), outlined, width=2) #Outlined box

    def buttons(self):

        # --- EXIT BUTTON --- #
        self.exit = pygame.Rect(self.start_x-180, self.start_y-120, 40, 40)#Exit button collidepoint box
        pygame.draw.rect(self.window, config.DEFAULTCOLOUR, self.exit)
        self.exiticon = pygame.image.load('Photoicons/exit.png')#Exit button icon
        exitbutton = pygame.transform.smoothscale(self.exiticon, (30, 30))
        self.window.blit(exitbutton, (self.start_x-180, self.start_y-120))#Place position

        # --- HINT BUTTON --- #
        self.hint = pygame.Rect(self.start_x, self.start_y+365, 40, 55)
        pygame.draw.rect(self.window, config.DEFAULTCOLOUR, self.hint)
        self.buttonImage = pygame.image.load('Photoicons/hint.png')
        self.Image = pygame.transform.smoothscale(self.buttonImage, (40, 40))
        self.window.blit(self.Image, (self.start_x, self.start_y+365))
        self.text = 'Hint'
        self.icontext = self.labelfont.render(self.text, True, 'black')
        self.window.blit(self.icontext, (self.start_x+6, self.start_y+408))

        # --- PAUSE BUTTON --- #        
        self.pause = pygame.Rect(self.start_x+321, self.start_y+365, 40, 55)
        pygame.draw.rect(self.window, config.DEFAULTCOLOUR, self.pause)
        self.buttonImage = pygame.image.load('Photoicons/pause.png')
        self.Image = pygame.transform.smoothscale(self.buttonImage, (40, 40))
        self.window.blit(self.Image, (self.start_x+321, self.start_y+365))
        self.text = 'Pause'
        self.icontext = self.labelfont.render(self.text, True, 'black')
        self.window.blit(self.icontext, (self.start_x+321, self.start_y+408))

        # --- UNDO BUTTON --- #
        self.undo = pygame.Rect(self.start_x+281, self.start_y+365, 40, 55)#Undo button collidepoint box
        pygame.draw.rect(self.window, config.DEFAULTCOLOUR, self.undo)
        self.undoicon = pygame.image.load('Photoicons/undo.png')#Hint button icon
        self.undobutton = pygame.transform.smoothscale(self.undoicon, (40, 40))
        self.window.blit(self.undobutton, (self.start_x+282, self.start_y+365))#Place position
        self.text='Undo'#Undo label text
        self.icontext = self.labelfont.render(self.text, True, 'black')
        self.window.blit(self.icontext, (self.start_x+284, self.start_y+408))#Place position

    def timing(self):#Timer system
        text = f"{self.minutes:02}:{self.seconds:02}"#Timing text
        font = pygame.font.Font(None, 32)
        buttontext = font.render(str(text), True, 'black')
        self.window.blit(buttontext, (self.start_x+300, self.start_y-30))#Place position

    def timeout(self):#User runs out of time
        font = pygame.font.Font(None, 25)
        text = 'OUT OF TIME'#Output text
        buttontext = font.render(str(text), True, 'black')
        self.window.blit(buttontext, (self.start_x+130, self.start_y-120))#Place position
        text = ('Mistakes : '+ str(self.mistakes))
        buttontext = font.render(str(text), True, 'black')
        self.window.blit(buttontext, (self.start_x+130, self.start_y-90))#Place position

    def completed(self):#User completes the sudoku game
        font = pygame.font.Font(None, 25)
        text = 'Sudoku finished'                
        buttontext = font.render(str(text), True, 'black')
        self.window.blit(buttontext, (self.start_x+115, self.start_y-120))#Place position

        text = ('Mistakes : '+ str(self.mistakes))#Mistakes
        buttontext = font.render(str(text), True, 'black')
        self.window.blit(buttontext, (self.start_x+130, self.start_y-90))#Place position

        self.finishtime = self.start_time - self.timer
        self.seconds = self.finishtime % 60
        self.minutes = int(self.finishtime / 60) % 60
        time_taken = f"Time taken {self.minutes:02}:{self.seconds:02}"
        buttontext = font.render(str(time_taken), True, 'black')
        self.window.blit(buttontext, (self.start_x+115, self.start_y-60))#Place position

    def hintbutton(self):#Hint function
        emptyCells = []#Holds empty cell indexes
        for j in range(9):
            for i in range(9):
                if self.board[j][i] == 0:
                    emptyCells.append([j,i])#Adds index to array

        randomindex = r.randint(0, len(emptyCells)-1)
        gapPosition = [emptyCells[randomindex]]# Array of 2 index positions

        yposition = gapPosition[0][0] # Gets row index
        xposition = gapPosition[0][1] # Gets column index

        self.board[yposition][xposition] = self.completeboard[yposition][xposition] # Reveals this cell
        self.hintsindex.append([yposition, xposition])

    def remaininghints(self):#Show number of hints
        font = pygame.font.SysFont(None, 25)
        text=self.hintsleft#Pause label text
        icontext = font.render(str(text), True, 'black')
        self.window.blit(icontext, (self.start_x+35, self.start_y+365))#Place position

    def showDifficulty(self):
        text = 'Difficulty: ' +str(config.DIFFICULTIES[self.settings.getDifficulty()])
        icontext = self.largefont.render(text, True, 'black')
        self.window.blit(icontext, (self.start_x+2, self.start_y-25))#Place position

    def initialiseStats(self):
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
        cursor.execute("SELECT easySolves FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.easySolves = cursor.fetchall()[0][0]
        cursor.execute("SELECT loadAmount FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.loadAmount = cursor.fetchall()[0][0]
        conn.commit()
        conn.close()#Close database

    def updateData(self):
        # --- SOLVING STATISTIC FORMULA --- #
        self.timetaken = self.start_time - self.timer
        t = self.timer/self.start_time
        self.solvingStatistic = t + ((self.correctEntries*0.02)-(self.mistakes*0.01))
        self.solvingStatistic = self.solvingStatistic * (0.85**self.hintsUsed)
        self.solvingStatistic = self.solvingStatistic * (0.75**(3-self.difficulty))#Difficulty adjustment
        self.solvingStatistic = round(self.solvingStatistic, 2)

        conn = sqlite3.connect('user.db')#Opens database
        cursor = conn.cursor()
        cursor.execute("SELECT mistakes FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.newMistakes = self.mistakes + cursor.fetchall()[0][0]
        cursor.execute("UPDATE users SET mistakes = ?", (self.newMistakes,))
        cursor.execute("SELECT correctEntries FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.newCorrectEntries = self.correctEntries + cursor.fetchall()[0][0]
        cursor.execute("UPDATE users SET correctEntries = ?", (self.newCorrectEntries,)) 
        cursor.execute("SELECT totalHints FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.totalHintsUsed = self.hintsUsed + cursor.fetchall()[0][0]
        cursor.execute("UPDATE users SET totalHints = ?", (self.totalHintsUsed,)) 
        cursor.execute("SELECT * FROM graphing WHERE username = ?", (config.getUsername(),))
        full = cursor.fetchall()#Selects all graphing data for current user
        rows = ['y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10']
        temparr = []
        for i in range(2, 12):
            temparr.append(full[0][i])#Adds username and last 10 values
        temparr.append(self.solvingStatistic)#Adds new value to array
        for i in range(11):#Adds in new array of values
            cursor.execute(f"UPDATE graphing SET {rows[i]} = (?) WHERE username = (?)", (temparr[i], config.getUsername(),))
        cursor.execute("SELECT bestSolve FROM users WHERE username = ?", (config.getUsername(),))
        self.bestSolve = cursor.fetchall()[0][0]
        if self.solvingStatistic > self.bestSolve or self.bestSolve == 0:
            cursor.execute("UPDATE users SET bestSolve = ? WHERE username =?", (self.solvingStatistic, config.getUsername(),))
        cursor.execute("SELECT loadAmount FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.newLoadAmount = self.loadAmount + cursor.fetchall()[0][0]
        cursor.execute("UPDATE users SET loadAmount = ? WHERE username =?", (self.newLoadAmount, config.getUsername(),))
        cursor.execute("SELECT easySolves FROM users WHERE username = ?", (str(config.getUsername()),))#Fetches theme from users
        self.newEasySolves = self.easySolves + cursor.fetchall()[0][0]
        cursor.execute("UPDATE users SET easySolves = ? WHERE username =?", (self.newEasySolves, config.getUsername(),))
        conn.commit()
        conn.close()

    def game(self):
        if config.getUsername() != None: # Set game settings if user is logged in
            self.initialiseStats()
        # --- PRECONDITIONS --- #
        self.spamstopped = False
        self.finished = False
        self.timer = int(self.settings.getTimer() * 60)
        self.start_time = self.timer

        self.added = False
        self.mistakes = 0
        self.timemistakes = 0
        self.correctEntries = 0
        self.hintsUsed = 0

        self.valids = []
        self.invalids = []
        self.hintsindex = []
        self.initialHints = self.settings.getHints()
        self.hintsleft = self.initialHints
        
        self.onCell = False
        self.countmistakes = 0

        # -- BOARD -- #
        self.completeboard, self.board = userboard.testing()
        self.selected_cell = None
        self.indexesofNums = [[0 for _ in range(9)] for _ in range(9)]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for number in self.numbers:  # For every digit
            column = 0
            for j in range(9):
                for i in range(9):
                    if self.board[j][i] == number:  # Finds position of number
                        self.indexesofNums[number - 1][column] = [j, i]  # Adds it to indexes
                        column += 1  # Increments the column

        self.difficulty = 2 + self.settings.getDifficulty()

        for number in self.numbers:  # For every number
            spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(self.difficulty):  # Removes amount of that number
                value = spaces[r.randint(0, len(spaces) - 1)]  # Random
                spaces.remove(value)  # Removes value chosen
                y, x = self.indexesofNums[number - 1][value - 1]  # Random position
                self.board[y][x] = 0  # Clears cells

        self.initialboard = [[self.board[j][i] for i in range(9)] for j in range(9)]
        self.entries = [[False for i in range(9)] for i in range(9)] # Correct entry board counter

        self.clock = pygame.time.Clock()  # Pygame time
        self.static_time = pygame.time.get_ticks()  # Initial time variable for timer
        self.set_time = pygame.time.get_ticks()  # Initial time variable for tips changer
        self.mistake_time = pygame.time.get_ticks()  # Initial time variable for mistake spam

        self.centering()
        # --- GAME LOOP --- #
        self.running = True
        while self.running:
            self.newtime = pygame.time.get_ticks()
            self.window.fill(config.DEFAULTCOLOUR)  # Clear the screen
            self.generate()
            self.centering()
            self.buttons()
            self.remaininghints()
            self.showDifficulty()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Collapse the app
                    self.running = False
                if event.type == pygame.VIDEORESIZE:  # Handle window resizing
                    self.window_width, self.window_height = event.w, event.h
                    self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
                    self.centering()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.start_x <= x <= self.start_x + 360 and self.start_y <= y <= self.start_y + 355:
                        self.row, self.col = (y - (self.start_y)) // 40, (x - self.start_x) // 40
                        self.selected_cell = (self.row, self.col)
                        self.onCell = True
                    if self.exit.collidepoint(event.pos):
                        self.running = False
                    if not self.finished:
                        if self.hint.collidepoint(event.pos):  # Press hint
                            if self.hintsleft > 0:#If hints available
                                self.hintsleft -=1#Decrease hints left
                                self.hintsUsed +=1
                                self.hintbutton()#Use a hint
                        if self.pause.collidepoint(event.pos):
                            print("MISTAKES:", self.mistakes)
                            print("Correct entries:", self.correctEntries)
                        if self.undo.collidepoint(event.pos): pass # Press undo
                if event.type == pygame.KEYDOWN and self.selected_cell:
                    if not self.finished:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:  # Up arrow or W key pressed
                            if self.row > 0:
                                self.row -= 1  # Cell above
                                self.selected_cell = (self.row, self.col)
                            self.outline(self.row, self.col)
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # Down arrow or S key pressed
                            if self.row < 8:
                                self.row += 1  # Cell below
                                self.selected_cell = (self.row, self.col)
                            self.outline(self.row, self.col)
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # Right arrow or D key pressed
                            if self.col < 8:
                                self.col += 1  # Cell to the right
                                self.selected_cell = (self.row, self.col)
                            self.outline(self.row, self.col)
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # Left arrow or A key pressed
                            if self.col > 0:
                                self.col -= 1  # Cell to the left
                                self.selected_cell = (self.row, self.col)
                            self.outline(self.row, self.col)
                        self.row, self.col = self.selected_cell
                        if not self.finished:
                            if event.unicode.isdigit() and (self.board[self.row][self.col] == 0 or self.board[self.row][self.col] != 0 and self.initialboard[self.row][self.col] == 0):  # Input on cell
                                self.board[self.row][self.col] = int(event.unicode)  # Update cell
                                if self.board[self.row][self.col] == self.completeboard[self.row][self.col]:  # Correct entry
                                    self.valids.append([self.row, self.col])
                                    if [self.row, self.col] in self.invalids:  # Remove from invalid entries
                                        self.invalids.remove([self.row, self.col])
                                else:
                                    self.invalids.append([self.row, self.col])  # Incorrect entry
                                    if [self.row, self.col] in self.valids:  # Remove from valid entries
                                        self.valids.remove([self.row, self.col])
                                    if not self.finished:
                                        self.mistakes += 1
                                        self.timemistakes += 1
                            if event.key == pygame.K_BACKSPACE and self.board[self.row][self.col] != self.initialboard[self.row][self.col]:  # Backspace on cell
                                self.board[self.row][self.col] = 0  # Remove entry
            if self.onCell:
                self.outline(self.row, self.col)
            for j in range(9):
                for i in range(9):
                    num = self.board[j][i]
                    if num != 0:
                        font = pygame.font.Font(None, 30)
                        if [j, i] in self.valids:  # Valid entry green
                            text = font.render(str(num), True, ('#70c139'))
                        elif [j, i] in self.invalids:  # Invalid entry red
                            text = font.render(str(num), True, ('red'))
                        elif [j, i] in self.hintsindex:  # Hint entry yellow
                            text = font.render(str(num), True, ('#918941'))
                        else: # Existing number colour
                            text = font.render(str(num), True, 'black')
                        x, y = (i * 40) + 15 + self.start_x, (j * 40) + 15 + self.start_y
                        self.window.blit(text, (x, y))
            self.seconds = self.timer % 60
            self.minutes = int(self.timer / 60) % 60
            if not self.finished:
                if self.newtime - self.static_time > 1000:#Every second
                    self.timing()
                    self.timer-=1#Decrease timer
                    self.static_time = self.newtime
                else:
                    self.timing()
            if self.finished == False:
                if self.board == self.completeboard:
                    self.finished = True
            else:
                self.completed()
            if config.getUsername() != None and self.added == False and self.finished:
                for j in range(9): 
                    for i in range(9): #Iterates through every cell
                        if self.initialboard[j][i] == 0:
                            if self.board[j][i] == self.completeboard[j][i] and self.entries[j][i] == False:#Is the entry correct
                                self.entries[j][i] = True
                                self.correctEntries+=1#Increment entries
                self.correctEntries -= self.hintsUsed
                if self.difficulty == 2:
                    self.easySolves += 1
                self.loadAmount += 1
                self.updateData() # Updates statistics for user after game has finished
                print("Mistakes", self.mistakes)
                print("Corrects", self.correctEntries)
                print("HintsUsed:", self.hintsUsed)
                print("")
                self.added = True
            if self.timer == 0:
                self.timeout()   
                self.finished = True

            pygame.display.update()

        pygame.display.quit()
        pygame.quit()
  