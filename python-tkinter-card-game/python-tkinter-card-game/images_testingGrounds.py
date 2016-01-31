from tkinter import PhotoImage
import random
from ImageDeck import ImageDeck

class TestingGroundsImages(object):
    """description of class"""
    
    def __init__(self):
        self.Blank = PhotoImage(width=70,height=100)
        self.MainMenu = PhotoImage(file='Images\\main menu_testing grounds.gif')
        self.backs = []
        self.backs.append(PhotoImage(file='Images\\back_adorably hideous.gif'))
        self.decks = []
        self.oxygen = ImageDeck('Images\\oxygen\\')
        self.decks.append(self.oxygen)
        self.backs.append(self.oxygen.Back)
        self.oxygenWhite = ImageDeck('Images\\oxygen white\\')
        self.oxygenWhite.Joker = PhotoImage(file='Images\\oxygen white\\joker.gif')
        self.decks.append(self.oxygenWhite)
        self.backs.append(self.oxygenWhite.Back)
        
    def GetRandomBack(self)->PhotoImage:
        return random.choice(self.backs)
    def GetRandomDeck(self)->ImageDeck:
        return random.choice(self.decks)