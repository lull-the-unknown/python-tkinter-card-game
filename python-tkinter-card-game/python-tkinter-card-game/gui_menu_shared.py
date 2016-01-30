from tkinter import *
from tkinter import ttk
from appBase import appBase

class MenuBase(object):
    """Base class for menus to provide shared methods"""

    def __init__(self):
        super().__init__()
        self._frame = None

    def _CreateMenuButton(self, row, text, command=None ):
        result = ttk.Button(self._frame, text=text, padding='5 5 5 5', command=command)
        result.grid(row=row, column=0, sticky=(N, S, E, W), pady=5, padx=5)
        return result
    def BindKeys(self,app:appBase):
        pass
    def UnBindKeys(self,app:appBase):
        pass
    
    def Show(self, app:appBase):
        self._frame.grid(column=1, row=0,sticky=(N, S, E, W))
        self.BindKeys(app)

    def Hide(self, app:appBase):
        # To remove a frame from a grid: frame.remove() to remember grid settings -or- frame.forget() to discard grid settings
        self.UnBindKeys(app)
        self._frame.grid_remove()