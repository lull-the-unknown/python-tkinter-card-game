from tkinter import *
from tkinter import ttk
from appBase import appBase
from gui_menuBase import MenuBase
from gui_mainMenu import MainMenu
from gameBase import *
from options_app import AppOptions

class app(appBase):
    """The app (i.e. Master Control)"""

    def __init__(self):
        super().__init__()
        self._InitState()
        self._CreateGui()
        self.LoadGame(self.options.gamemode)

    def Run(self):
        self.menuSplitFrame.grid(column=0, row=0,sticky=(N, S, E, W))
        self.CurrentScreen = self.screen_mainMenu
        self.CurrentScreen.Show()
        self.window.mainloop()

    def Quit(self):
        self.window.destroy()

    def _InitState(self):
        self.options = AppOptions()
        self.game = gameBase()
        self.CurrentScreen = None

    def _CreateGui(self):
        self._CreateMainWindow()
        self._CreateMenuSplitFrame()
        self._CreateMenuScreens()
        
    def _CreateMainWindow(self):
        self.window = Tk()
        self.window.title('Simple Card Game')
        self.window.geometry(self.options.screen)
        self.window.columnconfigure(0,weight=1)
        self.window.rowconfigure(0,weight=1)

    def _CreateMenuSplitFrame(self):
        self.menuSplitFrame = ttk.Frame(self.window)
        self.menuSplitFrame.columnconfigure(0,weight=0) #col0 is where the image goes
        self.menuSplitFrame.columnconfigure(1,weight=1) #col1 is where the menu buttons go        
        self.menuSplitFrame.imagelabel = ttk.Label(self.menuSplitFrame)
        self.menuSplitFrame.imagelabel.grid(column=0, row=0,sticky=(N, S, E, W))

    def LoadGame(self, name):
        self.game.End()
        self.game = GameLoader.LoadGame_ByName(name)
        self.menuSplitFrame.imagelabel['image'] = self.game.Images.MainMenu

    def _CreateMenuScreens(self):
        self.screen_mainMenu = MainMenu(self)
        self.screen_changeGameMenu = None
        
        #load new game menu, if available
        if self.game.menuclass_newgame != None:
            self.screen_newGameMenu = self.game.menuclass_newgame(self)
        else:
            self.screen_mainMenu.DisableButton('newgame')
        
        #load options menu, if available
        if self.game.menuclass_options != None:
            self.screen_optionsMenu = self.game.menuclass_options(self)
        else:
            self.screen_mainMenu.DisableButton('options')
        
        #load achievements menu, if available
        if self.game.menuclass_achievements != None:
            self.screen_achievementsMenu = self.game.menuclass_achievements(self)
        else:
            self.screen_mainMenu.DisableButton('achievements')
        
        #load credits menu, if available
        if self.game.menuclass_credits != None:
            self.screen_creditsMenu = self.game.menuclass_credits(self)
        else:
            self.screen_mainMenu.DisableButton('credits')

    def _switchScreens(self, newScreen:MenuBase):
        self.CurrentScreen.Hide()
        newScreen.Show()
        self.CurrentScreen = newScreen

    def ShowSplitMenu(self):
        self.menuSplitFrame.grid(column=0, row=0,sticky=(N, S, E, W))
    def HideSplitMenu(self):
        self.menuSplitFrame.grid_remove()
        
    def MainMenu(self):
        self._switchScreens(self.screen_mainMenu)
    def NewGame(self):
        self._switchScreens(self.screen_newGameMenu)
    def PlayGame(self):
        screen = self.screen_playGame
        self._switchScreens(screen)
        screen.DrawCards(self.state_Opponent.Deck, playerDeck)
    def ChangeGame(self):
        pass