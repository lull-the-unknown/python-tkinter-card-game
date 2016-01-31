from tkinter import *
from tkinter import ttk
from gui_menuBase import MenuBase
from appBase import appBase

class MainMenu(MenuBase):
    """The tk frame containing the main menu"""
    
    def __init__(self, gameApp:appBase):
        super().__init__(gameApp)
        self._CreateGui()
    
    def _CreateGui(self):
        self._frame = ttk.Frame(self.app.menuSplitFrame)
        self._frame.columnconfigure(0,weight=1)
        self._frame.rowconfigure(0,weight=1) #row0 = title
        self._frame.rowconfigure(1,weight=1) #row1 = game mode
        self._frame.rowconfigure(2,weight=1) #row2 = [New Game]
        self._frame.rowconfigure(3,weight=1) #row4 = [Options]
        self._frame.rowconfigure(4,weight=1) #row5 = [Acheivements]
        self._frame.rowconfigure(5,weight=1) #row6 = [Exit]
        
        ttk.Label(self._frame, text="Main Menu", padding='5 5 5 5', anchor="center").grid(row=0, column=0, sticky=(N, S, E, W), pady=5, padx=5)
        #ttk.Label(self._frame, text="(Game Mode: Testing Grounds)", padding='5 5 5 5', anchor="center").grid(row=1, column=0, sticky=(N, E, W), pady=5, padx=5)
        self._btnNewGame = self._CreateMenuButton(row=1, text='New Game ('+self.app.options.gamemode+')', command=self.app.NewGame )
        self._btnChangeGame = self._CreateMenuButton(row=2, text='Change Game ('+self.app.options.gamemode+')', command=self.app.ChangeGame )
        self._btnChangeGame.state(['disabled'])
        self._btnOptions = self._CreateMenuButton( row=3, text='Options' )
        frame = ttk.Frame(self._frame)
        frame.grid(column=0, row=4, sticky=(N,S,E,W))
        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(1,weight=1)
        frame.rowconfigure(0,weight=1)
        self._btnAchievements = self._CreateMenuButton( row=0, text='Achievements', parent=frame )
        self._btnAchievements.grid_configure(column=0)
        self._btnCredits = self._CreateMenuButton( row=0, text='Credits', parent=frame )
        self._btnCredits.grid_configure(column=1)
        self._btnQuit = self._CreateMenuButton( row=5, text='Exit', command=self.app.Quit )
        
    def BindKeys(self):
        self.app.window.bind('<Escape>', lambda e: self.app.Quit())
        self.app.window.bind('<Return>', lambda e: self.app.NewGame())
    def UnBindKeys(self):
        self.app.window.bind('<Escape>', None)
        self.app.window.bind('<Return>', None)
    def Show(self):
        self.app.ShowSplitMenu()
        show = super().Show
        self.app.window.after(200,lambda:show())        
    def Hide(self):
        self.app.HideSplitMenu()
        super().Hide()

    def DisableButton(self, name:str):
        name = name.lower()
        if name == 'newgame':
            self._btnNewGame.state(['disabled'])
        elif name == 'options':
            self._btnOptions.state(['disabled'])
        elif name == 'achievements':
            self._btnAchievements.state(['disabled'])
        elif name == 'credits':
            self._btnCredits.state(['disabled'])