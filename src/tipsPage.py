import tkinter as tk

from frame import Frame
    

class TipsPage(Frame):
    def __init__(self, app, window):
        self.app = app
        super().__init__(window)
        self.createWidgets()
        super().exiting()

    def createWidgets(self):
        self.tipheader = tk.Label(self.frame, text="Sudoku Tips & Tricks", fg='black', font=("Helvetica", 20, "bold"))
        self.tipheader.place(x=190, y=25)
        tip = tk.Label(self.frame, text="1.Start with the Basics: Begin by filling in any obvious or easy numbers.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=90)
        tip = tk.Label(self.frame, text="2.Scan Rows, Columns, and Boxes: Look for missing numbers and note possibilities.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=120)
        tip = tk.Label(self.frame, text="3.Use Pencil Marks: Keep track of possible numbers in empty cells.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=150)
        tip = tk.Label(self.frame, text="4.Cross-Check Rows and Columns: Make sure each number appears only once in a", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=180)
        tip = tk.Label(self.frame, text="  row or column.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=210)
        tip = tk.Label(self.frame, text="5.Cross-Check Boxes: Ensure each number appears only once in a 3x3 box.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=240)
        tip = tk.Label(self.frame, text="6.Solitary Numbers: Look for cells with only one possible number left.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=270)
        tip = tk.Label(self.frame, text="7.Elimination: Narrow down possibilities by eliminating numbers based on", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=300)
        tip = tk.Label(self.frame, text="  neighboring cells.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=330)
        tip = tk.Label(self.frame, text="8.Hidden Singles: Identify numbers that can only go in one place in a row, column,", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=360)
        tip = tk.Label(self.frame, text="  or box.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=390)
        tip = tk.Label(self.frame, text="9.Naked Pairs and Triples: Look for sets of two or three cells in a row,", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=420)
        tip = tk.Label(self.frame, text="  column, or box with the same possible numbers.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=450)
        tip = tk.Label(self.frame, text="10.X-Wing and Swordfish: Advanced techniques to eliminate numbers in specific", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=480)
        tip = tk.Label(self.frame, text="  patterns.", fg='black', font=("Helvetica", 13))
        tip.place(x=50, y=510)
  