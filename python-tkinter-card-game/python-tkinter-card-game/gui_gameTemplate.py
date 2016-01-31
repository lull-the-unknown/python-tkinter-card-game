from tkinter import *
from tkinter import ttk
from appBase import appBase

class TemplateScreen(object):
    """Description of screen goes here"""
        
    def __init__(self, gameApp:appBase):
        super().__init__()
        self.app = gameApp
        self._CreateGui(gameApp)
    
    def _CreateGui(self):
        #self._frame = ttk.Frame(self.app.menuSplitFrame) #if using split screen for a menu
        self._frame = ttk.Frame(self.app.window)
        
    def BindKeys(self):
        self.app.window.bind('<Escape>', lambda e: self.app.Quit())
    def UnBindKeys(self):
        self.app.window.bind('<Escape>', None)
    
    def Show(self):
        self._frame.grid(column=0, row=0,sticky=(N, S, E, W)) #if NOT using split screen for a menu
        #self.app.ShowSplitMenu() #if using split screen for a menu
        #self.app.window.after(200,lambda:self._frame.grid(column=1, row=0,sticky=(N, S, E, W)))  #if using split screen for a menu
        self.BindKeys(self.app)

    def Hide(self):
        # To remove a frame from a grid: frame.remove() to remember grid settings or frame.forget() to discard grid settings
        self.UnBindKeys(self.app)
        self._frame.grid_remove()
        #self.app.HideSplitMenu() #if using split screen for a menu
        