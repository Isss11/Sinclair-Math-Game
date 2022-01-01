"""
This class is basically just organizing all the graphical aspects of this program one class. It makes it easier for me to organize main.py
"""

from tkinter import *
from tkinter import ttk

class graphicsObject:
    def __init__(self, root):
        self.root = root
        self.root.title("Sinclair Math -- Learn Math!")
        self.frame = ttk.Frame(self.root)
        self.frame['padding'] = (5, 10) #setting up the window and frame
        self.frame.grid(row = 0, column = 0, sticky=(N, W, E, S))
        
        self.introTitle = ttk.Label(self.frame, text='Sinclair Math!')
        self.introTitle.grid(row = 2)

        self.waitVar = IntVar()

        self.introButton = ttk.Button(self.frame, text= "Continue", command= self.clearIntro) #Creates a button that clears everything if it is clicked
        self.introButton.grid(row = 4, column = 8)

    def clearIntro(self):
        self.introButton.destroy()
        self.introTitle.destroy()

    def getGameType(self):
        self.gameTypeTitle = ttk.Label(self.frame, text = "Choose a Math Game Type")

        self.additionGame = ttk.Button(self.frame, text = "Addition")
        self.subtractionGame = ttk.Button(self.frame, text = "Subtraction")
        self.multiplicationGame = ttk.Button(self.frame, text = "Multiplication")
        self.divisionGame = ttk.Button(self.frame, text = "Division") #creating initial title and all 4 buttons

        self.gameTypeTitle.grid(row = 1)
        self.additionGame.grid(row = 2)
        self.subtractionGame.grid(row = 3)
        self.multiplicationGame.grid(row = 4)
        self.divisionGame.grid(row = 5) #drawing them all

        

        
root = Tk()
graphicsWindow = graphicsObject(root) 
graphicsWindow.getGameType()
root.mainloop() #remember to always include the mainloop!