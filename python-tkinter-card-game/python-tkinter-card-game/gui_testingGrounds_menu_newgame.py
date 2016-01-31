from tkinter import *
from tkinter import ttk
from appBase import appBase
from gameBase import gameBase
from gui_menuBase import MenuBase

class TestingGroundsNewGameMenu(MenuBase):
    """The tk frame containing the new game menu"""

    def __init__(self, app:appBase, game:gameBase):
        super().__init__(app)
        self.game = game
        self._CreateGui()
    
    def _CreateGui(self):
        self._frame = ttk.Frame(self.app.menuSplitFrame)
        self._frame.columnconfigure(0,weight=1)
        self._frame.rowconfigure(0,weight=1) #row0 = title
        self._frame.rowconfigure(1,weight=1) #row1 = [Start]
        self._frame.rowconfigure(2,weight=1) #row2 = [Select Opponent]
        self._frame.rowconfigure(3,weight=1) #row3 = [Deck Setup]
        self._frame.rowconfigure(4,weight=2) #row4 = empty
        self._frame.rowconfigure(5,weight=1) #row5 = [Back]
        
        ttk.Label(self._frame, text="New Game", padding='5 5 5 5', anchor="center").grid(row=0, column=0, sticky=(N, S, E, W), pady=5, padx=5)
        self._btnStart = self._CreateMenuButton( row=1, text='Start', command=self.game.StartPlaying )
        self._btnSelectOpponent = self._CreateMenuButton( row=2, text='Select Opponent' )
        self._btnSelectOpponent.state(['disabled'])
        self._btnSelectDeck = self._CreateMenuButton( row=3, text='Deck Setup' )
        self._btnSelectDeck.state(['disabled'])
        self._btnBack = self._CreateMenuButton( row=5, text='Back', command=self.app.MainMenu )
        
    def BindKeys(self):
        self.app.window.bind('<Escape>', lambda e: self.app.MainMenu())
        self.app.window.bind('<Return>', lambda e: self.game.StartPlaying())
    def UnBindKeys(self):
        self.app.window.unbind('<Escape>')
        self.app.window.unbind('<Return>')

    def Show(self):
        self.app.ShowSplitMenu()
        show = super().Show
        self.app.window.after(200,lambda:show()) 
        #self._btnSelectOpponent['text'] = "Select Opponent ("+self.app.game.options.opponent.Name+")"
        #self._btnSelectDeck['text'] = "Select Deck ("+self.app.game.options.PlayerDeck.Name+")"
    def Hide(self):
        self.app.HideSplitMenu()
        super().Hide()