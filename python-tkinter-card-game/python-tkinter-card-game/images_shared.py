from tkinter import PhotoImage

class ImageDeck(object):
    """An image structure for a 52 card deck"""

    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3

    def __init__(self, folderpath):
        super().__init__()
        self.Back = PhotoImage(folderpath+'back.gif')
        self.Suits = []
        clubs = []
        self.Suits.append(clubs)
        clubs.append(PhotoImage(folderpath+'1_club.gif'))
        clubs.append(PhotoImage(folderpath+'2_club.gif'))
        clubs.append(PhotoImage(folderpath+'3_club.gif'))
        clubs.append(PhotoImage(folderpath+'4_club.gif'))
        clubs.append(PhotoImage(folderpath+'5_club.gif'))
        clubs.append(PhotoImage(folderpath+'6_club.gif'))
        clubs.append(PhotoImage(folderpath+'7_club.gif'))
        clubs.append(PhotoImage(folderpath+'8_club.gif'))
        clubs.append(PhotoImage(folderpath+'9_club.gif'))
        clubs.append(PhotoImage(folderpath+'10_club.gif'))
        clubs.append(PhotoImage(folderpath+'jack_club.gif'))
        clubs.append(PhotoImage(folderpath+'queen_club.gif'))
        clubs.append(PhotoImage(folderpath+'king_club.gif'))
        
        diamonds = []
        self.Suits.append(diamonds)
        diamonds.append(PhotoImage(folderpath+'1_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'2_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'3_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'4_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'5_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'6_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'7_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'8_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'9_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'10_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'jack_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'queen_diamond.gif'))
        diamonds.append(PhotoImage(folderpath+'king_diamond.gif'))
        
        hearts = []
        self.Suits.append(hearts)
        hearts.append(PhotoImage(folderpath+'1_heart.gif'))
        hearts.append(PhotoImage(folderpath+'2_heart.gif'))
        hearts.append(PhotoImage(folderpath+'3_heart.gif'))
        hearts.append(PhotoImage(folderpath+'4_heart.gif'))
        hearts.append(PhotoImage(folderpath+'5_heart.gif'))
        hearts.append(PhotoImage(folderpath+'6_heart.gif'))
        hearts.append(PhotoImage(folderpath+'7_heart.gif'))
        hearts.append(PhotoImage(folderpath+'8_heart.gif'))
        hearts.append(PhotoImage(folderpath+'9_heart.gif'))
        hearts.append(PhotoImage(folderpath+'10_heart.gif'))
        hearts.append(PhotoImage(folderpath+'jack_heart.gif'))
        hearts.append(PhotoImage(folderpath+'queen_heart.gif'))
        hearts.append(PhotoImage(folderpath+'king_heart.gif'))
        
        spades = []
        self.Suits.append(spades)
        spades.append(PhotoImage(folderpath+'1_spade.gif'))
        spades.append(PhotoImage(folderpath+'2_spade.gif'))
        spades.append(PhotoImage(folderpath+'3_spade.gif'))
        spades.append(PhotoImage(folderpath+'4_spade.gif'))
        spades.append(PhotoImage(folderpath+'5_spade.gif'))
        spades.append(PhotoImage(folderpath+'6_spade.gif'))
        spades.append(PhotoImage(folderpath+'7_spade.gif'))
        spades.append(PhotoImage(folderpath+'8_spade.gif'))
        spades.append(PhotoImage(folderpath+'9_spade.gif'))
        spades.append(PhotoImage(folderpath+'10_spade.gif'))
        spades.append(PhotoImage(folderpath+'jack_spade.gif'))
        spades.append(PhotoImage(folderpath+'queen_spade.gif'))
        spades.append(PhotoImage(folderpath+'king_spade.gif'))