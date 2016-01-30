from tkinter import *
from tkinter import ttk
from appBase import appBase

class TemplateScreen(object):
    """Description of screen goes here"""
    
    def _CreateGui(self, app:appBase):
        self._frame = ttk.Frame(app.menuSplitFrame)
        self._frame = ttk.Frame(app.window)
        
    def BindKeys(self, app:appBase):
        app.window.bind('<Escape>', lambda e: app.Quit())
    def UnBindKeys(self, app:appBase):
        app.window.bind('<Escape>', None)
        
    def __init__(self, app:appBase):
        super().__init__()
        self._CreateGui(app)
    
    def Show(self, app:appBase):
        self._frame.grid(column=0, row=0,sticky=(N, S, E, W))
        self.BindKeys(app)

    def Hide(self, app:appBase):
        # To remove a frame from a grid: frame.remove() to remember grid settings or frame.forget() to discard grid settings
        self.UnBindKeys(app)
        self._frame.grid_remove()
        