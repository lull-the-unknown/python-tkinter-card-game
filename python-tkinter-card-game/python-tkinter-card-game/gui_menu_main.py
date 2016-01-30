from tkinter import *
from tkinter import ttk

from gui_menu_shared import MenuBase
from appBase import appBase

class MainMenu(MenuBase):
    """The tk frame containing the main menu"""
    
    def _CreateGui(self, app:appBase):
        self._frame = ttk.Frame(app.menuSplitFrame)
        self._frame.columnconfigure(0,weight=1)
        self._frame.rowconfigure(0,weight=1) #row0 = title
        self._frame.rowconfigure(1,weight=1) #row1 = game mode
        self._frame.rowconfigure(2,weight=2) #row2 = [New Game]
        self._frame.rowconfigure(3,weight=2) #row3 = [Deck Setup]
        self._frame.rowconfigure(4,weight=2) #row4 = [Options]
        self._frame.rowconfigure(5,weight=2) #row5 = [Acheivements]
        self._frame.rowconfigure(6,weight=2) #row6 = [Exit]
        
        ttk.Label(self._frame, text="Main Menu", padding='5 5 5 5', anchor="center").grid(row=0, column=0, sticky=(S, E, W), pady=5, padx=5)
        ttk.Label(self._frame, text="(Game Mode: Testing Grounds)", padding='5 5 5 5', anchor="center").grid(row=1, column=0, sticky=(N, E, W), pady=5, padx=5)
        self._btnNewGame = self._CreateMenuButton(row=2, text='New Game', command=app.NewGame )
        self._btnDeckSetup = self._CreateMenuButton( row=3, text='Deck Setup' )
        self._btnDeckSetup.state(['disabled'])
        self._btnOptions = self._CreateMenuButton( row=4, text='Options' )
        self._btnOptions.state(['disabled'])
        self._btnAchievements = self._CreateMenuButton( row=5, text='Achievements' )
        self._btnAchievements.state(['disabled'])
        self._btnQuit = self._CreateMenuButton( row=6, text='Exit', command=app.Quit )
        
    def BindKeys(self, app:appBase):
        app.window.bind('<Escape>', lambda e: app.Quit())
        app.window.bind('<Return>', lambda e: app.NewGame())
    def UnBindKeys(self, app:appBase):
        app.window.bind('<Escape>', None)
        app.window.bind('<Return>', None)
    
    def __init__(self, app:appBase):
        super().__init__()
        self._CreateGui(app)