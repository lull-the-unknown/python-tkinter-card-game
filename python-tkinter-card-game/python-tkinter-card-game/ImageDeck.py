from tkinter import PhotoImage
import random

class ImageDeck(object):
    """An image structure for a 52 card deck"""
    
    def __init__(self, folderpath):
        super().__init__()
        self.Back = PhotoImage(file=folderpath+'back.gif')
        self.Suits = []
        self.clubs = []
        self.Suits.append(self.clubs)
        self.clubs.append(PhotoImage(file=folderpath+'1_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'2_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'3_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'4_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'5_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'6_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'7_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'8_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'9_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'10_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'jack_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'queen_club.gif'))
        self.clubs.append(PhotoImage(file=folderpath+'king_club.gif'))
        
        self.diamonds = []
        self.Suits.append(self.diamonds)
        self.diamonds.append(PhotoImage(file=folderpath+'1_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'2_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'3_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'4_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'5_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'6_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'7_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'8_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'9_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'10_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'jack_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'queen_diamond.gif'))
        self.diamonds.append(PhotoImage(file=folderpath+'king_diamond.gif'))
        
        self.hearts = []
        self.Suits.append(self.hearts)
        self.hearts.append(PhotoImage(file=folderpath+'1_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'2_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'3_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'4_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'5_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'6_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'7_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'8_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'9_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'10_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'jack_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'queen_heart.gif'))
        self.hearts.append(PhotoImage(file=folderpath+'king_heart.gif'))
        
        self.spades = []
        self.Suits.append(self.spades)
        self.spades.append(PhotoImage(file=folderpath+'1_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'2_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'3_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'4_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'5_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'6_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'7_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'8_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'9_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'10_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'jack_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'queen_spade.gif'))
        self.spades.append(PhotoImage(file=folderpath+'king_spade.gif'))
        
    def GetRandomSuit(self):
        return random.choice(self.Suits)
    def GetRandomFaceCard(self, suit=None):
        if suit==None:
            suit=self.GetRandomSuit()
        return random.choice(suit)