import gameBase
from options_testingGrounds import TestingGroundsOptions
from gui_testingGrounds_menu_newgame import NewGameMenu
#from gui_testingGrounds_game import PlayScreen

class TestingGrounds(gameBase.gameBase):
    """Testing Grounds isn't a real game, it's just for testing out techniques."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Testing Grounds"
        self.options = TestingGroundsOptions()
        self.menuclass_newgame = NewGameMenu
        self.menuclass_options = None
        self.menuclass_achievements = None
        self.menuclass_credits = None
        #TestingGroundsImages.LoadImages()
