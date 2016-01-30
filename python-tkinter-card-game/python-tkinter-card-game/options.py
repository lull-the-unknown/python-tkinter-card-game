import xml.etree.ElementTree as ET

class GameOptions(object):
    """Container holding options for a game"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # subclass template:
        #loader = OptionsLoader()
        #loader.LoadOptions_FromXML("gameName")
        #self.optionName = loader.GetValueOrDefault(name='optionName',default='default value if no option found by that name')
        #self.otherOptionName = loader.GetValueOrDefault(name='otherOptionName',default='default value if no option found by that name')
        

class OptionsLoader(object):
    """Handles loading/saving options"""

    filepath = "saves\options.xml"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gameName = ""
        self.options = None

    def GetValueOrDefault( self, name:str, default:str):
        if name in self.options:
            return self.options[name]
        else:
            print('Error: no "'+name+'" in the options file for "'+self.gameName+'". Setting default value of "'+default+'".')
            return default

    def LoadOptions_FromXML(self, name:str):
        self.gameName = name
        self.options = dict()
        xmlTree = ET.parse(filepath)
        xmlRoot = xmlTree.getroot()
        gameNodes = xmlRoot.findall("game")
        for game in gameNodes:
            if game.get("name") != name:
                continue
            optionNodes = game.findall('option')
            for option in optionNodes:
                self.options[option.get(name).lower()] = option.get(value)

    def SaveOptions_ToXml(name:str, optionsToSave:dict):
        xmlTree = ET.parse(filepath)
        xmlRoot = xmlTree.getroot()
        xmlGameNodes = xmlRoot.findall("game")
        xmlGame = None
        for gameElement in xmlGameNodes:
            if gameElement.get("name") == name:
                xmlGame = gameElement
                break

        if xmlGame == None:
            xmlGame = ET.SubElement(xmlGameNodes, 'game')
        else:
            xmlGame.clear()
        xmlGame.set('name', name)
        for optName in optionsToSave:
            xmlOption = ET.SubElement(xmlGame, 'option')
            xmlOption.set('name', optName.lower())
            xmlOption.set('value', optionsToSave[optName])

        tree.write(filepath)
