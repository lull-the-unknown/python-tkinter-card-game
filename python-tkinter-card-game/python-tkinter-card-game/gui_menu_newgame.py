from tkinter import *
from tkinter import ttk
from appBase import appBase
from gui_menu_shared import MenuBase

class NewGameMenu(MenuBase):
    """The tk frame containing the new game menu"""
    
    def _CreateGui(self, app:appBase):
        self._frame = ttk.Frame(app.menuSplitFrame)
        self._frame.columnconfigure(0,weight=1)
        self._frame.rowconfigure(0,weight=1) #row0 = title
        self._frame.rowconfigure(1,weight=1) #row1 = [New Game]
        self._frame.rowconfigure(2,weight=1) #row2 = [Deck Setup]
        self._frame.rowconfigure(3,weight=1) #row3 = [Options]
        self._frame.rowconfigure(4,weight=2) #row4 = empty
        self._frame.rowconfigure(5,weight=1) #row5 = [Exit]
        
        ttk.Label(self._frame, text="New Game", padding='5 5 5 5', anchor="center").grid(row=0, column=0, sticky=(N, S, E, W), pady=5, padx=5)
        self._btnStart = self._CreateMenuButton( row=1, text='Start', command=app.PlayGame )
        self._btnSelectOpponent = self._CreateMenuButton( row=2, text='Select Opponent' )
        self._btnSelectOpponent.state(['disabled'])
        self._btnSelectDeck = self._CreateMenuButton( row=3, text='Select Deck' )
        self._btnSelectDeck.state(['disabled'])
        self._btnBack = self._CreateMenuButton( row=5, text='Back', command=app.MainMenu )
        
    def BindKeys(self, app:appBase):
        app.window.bind('<Escape>', lambda e: app.MainMenu())
        app.window.bind('<Return>', lambda e: app.PlayGame())
    def UnBindKeys(self, app:appBase):
        app.window.bind('<Escape>', None)
        app.window.bind('<Return>', None)

    def __init__(self, app:appBase):
        super().__init__()
        self._CreateGui(app)

    def Show(self, app):
        super().Show(app)
        self._btnSelectOpponent['text'] = "Select Opponent ("+app.state_Opponent.Name+")"
        self._btnSelectDeck['text'] = "Select Deck ("+app.state_PlayerDeck.Name+")"