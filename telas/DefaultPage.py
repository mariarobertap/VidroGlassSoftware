from tkinter import *
from tkinter import font               
from Database import Database
from tkinter import Image
from tkinter import PhotoImage


class StartPage(Frame):

    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)

 
        self.controller = controller
        self.config(bg=controller.backgoung)
        self.buttonActiveColor =   "#0E7173"
        self.buttonInactiveColor = "#737574"
        
        self.controller.showDefaultButtons(self)



    def on_enter(self, e):
        e.widget['background'] = 'blue'

    def on_leave(self, e):
        e.widget['background'] = '#737574'