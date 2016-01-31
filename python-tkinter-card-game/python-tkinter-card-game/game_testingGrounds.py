import gameBase
from appBase import appBase
from options_testingGrounds import TestingGroundsOptions
from gui_testingGrounds_menu_newgame import TestingGroundsNewGameMenu
from gui_testingGrounds_game import TestingGroundsGameScreen
from images_testingGrounds import TestingGroundsImages

class TestingGrounds(gameBase.gameBase):
    """Testing Grounds isn't a real game, it's just for testing out techniques."""

    def __init__(self, app:appBase):
        super().__init__(app)
        self.name = "Testing Grounds"
        self.options = TestingGroundsOptions()
        self.Images = TestingGroundsImages()
        self.menu_newgame = TestingGroundsNewGameMenu(app, self)
        self.menu_options = None
        self.menu_achievements = None
        self.menu_credits = None
        
    def StopPlaying(self):
        self.app.SwitchScreens(self.menu_newgame)
    def StartPlaying(self):
        self.gamescreen = TestingGroundsGameScreen(self.app)
        self.app.SwitchScreens(self.gamescreen)
        self.gamescreen.DrawCards()