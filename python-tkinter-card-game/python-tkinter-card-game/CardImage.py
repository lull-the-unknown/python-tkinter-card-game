from tkinter import *
from tkinter import ttk
from images_app import AppImages


class CardImage(object):
    """The element representing a card on the screen"""

    def __init__(self, parentFrame:Frame, gridCol:int, gridRow:int):
        super().__init__()
        self.gridCol = gridCol
        self.gridRow = gridRow
        self.index = 0
        self._highlight = ttk.Label(parentFrame)
        self._card = ttk.Label(self._highlight, borderwidth=3, relief="groove")
        self._card.CardImage = self
        self._card.grid()
        self.cardFace = AppImages.Blank
        self.cardBack = AppImages.Blank
        self._card['image'] = AppImages.Blank
        self.isShowing = False
        self.currentHighlight = ''
        
    def _GetPady(self):
        peek = 20
        pad = 3
        if self.currentHighlight == '':
            return (self.index*peek+pad,(4-self.index)*peek+pad)
        else:
            return (self.index*peek,(4-self.index)*peek)
    def _GetPadx(self):
        pad = 3
        if self.currentHighlight == '':
            return pad
        else:
            return 0
    def Show(self):
        self._highlight.grid(column=self.gridCol, row=self.gridRow, padx=self._GetPadx(), pady=self._GetPady())
        self.isShowing = True
    def Hide(self):
        self._highlight.grd_remove()
        self.isShowing = False
    def MoveUp(self):
        self.index -= 1
        if self.index < 0:
            self.index = 0
        if self.isShowing:
            self._highlight.grid_configure(pady=self._GetPady())
    def MoveDown(self):
        self.index += 1
        if self.index > 4:
            self.index = 4
        if self.isShowing:
            self._highlight.grid_configure(pady=self._GetPady())
    def Highlight(self, color:str):
        pad = 3
        isBlank = self.currentHighlight == ''
        wantsBlank = color == ''
        self._highlight['background'] = color
        self.currentHighlight = color

        if isBlank and not wantsBlank:
            self._card.grid_configure(padx=3,pady=3)
            self._highlight.grid_configure(padx=self._GetPadx(), pady=self._GetPady())
        elif not isBlank and wantsBlank:
            self._card.grid_configure(padx=0,pady=0)
            self._highlight.grid_configure(padx=self._GetPadx(), pady=self._GetPady())
    def ShowCardFace(self):
        self._card['image'] = self.cardFace
    def ShowCardBack(self):
        self._card['image'] = self.cardBack
    def BindEvent(self, event:str, command):
        self._card.bind(event, command)