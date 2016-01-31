from options import *   

class TestingGroundsOptions(GameOptions):
    """Container holding options for the 'Testing Grounds' game"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Testing Grounds'
        self.Load()

    def Load(self):
        loader = OptionsLoader()
        loader.LoadOptions_FromXML(self.name)
        # there are currently no options for this game mode
        #self.optionName = loader.GetValueOrDefault(name='optionName',default='default value if no option found by that name')
        #self.otherOptionName = loader.GetValueOrDefault(name='otherOptionName',default='default value if no option found by that name')

    def ToDict(self)->dict:
        results = super().ToDict()
        # there are currently no options for this game mode
        #results['optionName'] = self.optionName
        #results['otherOptionName'] = self.otherOptionName
        return results