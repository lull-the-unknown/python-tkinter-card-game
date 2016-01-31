from tkinter import *
from tkinter import ttk
from appBase import appBase

class MenuBase(object):
    """Base class for menus to provide shared methods"""

    def __init__(self, gameApp:appBase):
        super().__init__()
        self.app = gameApp
        self._frame = None

    def _CreateMenuButton(self, row, text, command=None, parent=None ):
        if parent == None:
            parent = self._frame
        result = ttk.Button(parent, text=text, padding='5 5 5 5', command=command)
        result.grid(row=row, column=0, sticky=(N, S, E, W), pady=5, padx=5)
        return result
    def BindKeys(self):
        pass
    def UnBindKeys(self):
        pass
    
    def Show(self):
        self._frame.grid(column=1, row=0,sticky=(N, S, E, W))
        self.BindKeys()

    def Hide(self):
        # To remove a frame from a grid: frame.remove() to remember grid settings -or- frame.forget() to discard grid settings
        self.UnBindKeys()
        self._frame.grid_remove()