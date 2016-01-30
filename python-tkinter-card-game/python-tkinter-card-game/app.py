from tkinter import *
from tkinter import ttk
from appBase import appBase
from gui_menu_shared import MenuBase
import gui_menu_main
import gui_menu_newgame
#import gui_game_testingGrounds
#import Opponents
from images import Images
#from RandomDeckBuilder import GenerateRandomDeck

class app(appBase):
    """The app (i.e. Master Control)"""

    def __init__(self):
        super().__init__()
        self._CreateMainWindow()
        self._InitState()
        self._CreateMenuSplitFrame()
        self._CreateMenuScreens()
        self.CurrentScreen = None

    def Run(self):
        self.menuSplitFrame.grid(column=0, row=0,sticky=(N, S, E, W))
        self.CurrentScreen = self.screen_mainMenu
        self.CurrentScreen.Show(self)
        self.window.mainloop()

    def Quit(self):
        self.window.destroy()

    def _CreateMainWindow(self):
        self.window = Tk()
        self.window.title('Simple Card Game')
        #self.window.geometry ="800x600+0+0"
        self.window.minsize(width=800,height=600)
        self.window.columnconfigure(0,weight=1)
        self.window.rowconfigure(0,weight=1)

    def _CreateMenuSplitFrame(self):
        self.menuSplitFrame = ttk.Frame(self.window)
        self.menuSplitFrame.columnconfigure(0,weight=0) #col0 is where the image goes
        self.menuSplitFrame.columnconfigure(1,weight=1) #col1 is where the menu buttons go        
        label = ttk.Label(self.menuSplitFrame)
        label.grid(column=0, row=0,sticky=(N, S, E, W))
        label['image'] = Images.MainMenu

    def _CreateMenuScreens(self):
        self.screen_mainMenu = gui_menu_main.MainMenu(self)
        self.screen_newGameMenu = gui_menu_newgame.NewGameMenu(self)
        #self.screen_playGame = gui_screen_play.PlayScreen(self)

    def _InitState(self):
        Images.LoadImages()
        #self.state_PlayerDeck = GenerateRandomDeck()

    def _switchScreens(self, newScreen:MenuBase):
        #self.CurrentScreen.Hide(self)
        self.CurrentScreen = newScreen
        self.window.after(200,lambda:self.CurrentScreen.Show(self))

    def ShowSplitMenu(self):
        self.CurrentScreen.Hide(self)
        self.menuSplitFrame.grid(column=0, row=0,sticky=(N, S, E, W))
    def HideSplitMenu(self):
        self.CurrentScreen.Hide(self)
        self.menuSplitFrame.grid_remove()
        
    def MainMenu(self):
        self.ShowSplitMenu()
        self._switchScreens(self.screen_mainMenu)
    def NewGame(self):
        self.ShowSplitMenu()
        self._switchScreens(self.screen_newGameMenu)
    def PlayGame(self):
        screen = self.screen_playGame
        self.HideSplitMenu()
        self._switchScreens(screen)
        self.state_Opponent.GameStart(self)
        playerDeck = self.state_PlayerDeck.Clone()
        screen.DrawCards(self.state_Opponent.Deck, playerDeck)