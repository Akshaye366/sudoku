import tkinter as tk
from PIL import Image, ImageTk

class Frame:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(window)
        self.frame.grid(row=0, column=0)
        self.frame.configure(width=600, height=600)

    def minimumSize(self):
        self.window.minsize(600,600)
        
    def packFrame(self):
        self.frame.grid()

    def removeFrame(self):
        self.frame.grid_forget()


    def exiting(self):
        self.exitButton = Image.open('Photoicons/exit.png').resize((30, 30), True)#Icon file path
        self.exit = ImageTk.PhotoImage(self.exitButton)
        self.exitButton = tk.Label(self.frame, image=self.exit)#Icon set as label
        self.exitButton.image = self.exit
        self.exitButton.place(x=20,y=20)

        def ExitButton(event):
            self.app.runMenuPage()

        # Bind the click event to the label
        self.exitButton.bind("<Button-1>", ExitButton)
