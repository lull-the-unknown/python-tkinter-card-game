class gameBase(object):
    """The base class for a game object."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = ""
        self.options = None #a GameOptions object holding the options saved to file. which options are saved to file are up to the game dev. All of the options in the options screen should be saved to file. the options in the new game menu or their defaults can be saved to file if the dev wants to persist any of them. 
        self.menuclass_newgame = None #the new game menu is for selecting play-by-play options that a user would change from one playing to the next
        self.menuclass_options = None #the options menu is for selecting options that affect the game as a whole, options that would be saved to file and changed infrequently
        self.menuclass_achievements = None #achivements are stupid
        self.menuclass_credits = None #the credits screen is the place to put credits for gameart (images I nicked from the internet (legally, of coures))
        #GameImages.LoadImages() # load game specific images

class GameLoader(object):
    """Factory for creating game objects"""
    def LoadGame_ByName(name:str)->gameBase:
        """Factory for creating a game object from its name"""
        name = name.lower()
        if name == "testing grounds":
            from game_testingGrounds import TestingGrounds
            return TestingGrounds()