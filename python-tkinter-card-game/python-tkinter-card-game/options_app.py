from options import *   

class AppOptions(GameOptions):
    """Container holding options for the app"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        loader = OptionsLoader()
        loader.LoadOptions_FromXML("app")
        self.gamemode = loader.GetValueOrDefault(name='gamemode',default='testing grounds')
        self.screen = loader.GetValueOrDefault('screen','800x600+30+30') # (width)x(height)+-(xoffset)+-(yoffset)