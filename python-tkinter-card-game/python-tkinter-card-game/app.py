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
        self.game = gameBase(self)
        self.CurrentScreen = None

    def _CreateGui(self):
        self._CreateMainWindow()
        self._CreateMenuSplitFrame()
        self.screen_changeGameMenu = None
        
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
        self.game.QuitGame()
        self.game = GameLoader.LoadGame_ByName(name, self)
        self.screen_mainMenu = MainMenu(self)
        self.menuSplitFrame.imagelabel['image'] = self.game.Images.MainMenu
                
    def SwitchScreens(self, newScreen:MenuBase):
        self.CurrentScreen.Hide()
        newScreen.Show()
        self.CurrentScreen = newScreen

    def ShowSplitMenu(self):
        self.menuSplitFrame.grid(column=0, row=0,sticky=(N, S, E, W))
    def HideSplitMenu(self):
        self.menuSplitFrame.grid_remove()
        
    def MainMenu(self):
        self.SwitchScreens(self.screen_mainMenu)
    def ChangeGame(self):
        pass