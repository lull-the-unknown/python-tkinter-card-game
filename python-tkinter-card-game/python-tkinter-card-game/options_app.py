from options import *   

class AppOptions(GameOptions):
    """Container holding options for the app"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'app'
        self.Load()

    def Load(self):
        loader = OptionsLoader()
        loader.LoadOptions_FromXML(self.name)
        self.gamemode = loader.GetValueOrDefault(name='gamemode',default='Testing Grounds')
        self.screen = loader.GetValueOrDefault('screen','800x600+30+30') # (width)x(height)+-(xoffset)+-(yoffset)

    def ToDict(self)->dict:
        results = super().ToDict()
        results['gamemode'] = self.gamemode
        results['screen'] = self.screen
        return results