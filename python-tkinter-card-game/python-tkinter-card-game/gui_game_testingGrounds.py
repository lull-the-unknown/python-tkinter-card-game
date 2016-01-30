from tkinter import *
from tkinter import ttk
from appBase import appBase
#from Decks import *
#import Cards
from images import Images
from CardImage import CardImage

class PlayScreen(object):
    """The screen where the actual game is played"""
    
    def _CreateCards(self)->[]:
        border = 3
        relief = "groove"
        width = 70 + 3*border
        height = 100 + 3*border
        peek = 20
        pad = 3
        # Row0: Opponent's deck
        self.cards_Opponent = []
        for pileIndex in range(5):
            label = ttk.Label(self._frame, borderwidth=border, relief=relief)
            label.grid(column=pileIndex, row=0, padx=pad, pady=pad)
            label['image'] = Images.Blank
            self.cards_Opponent.append(label)
        # Row1: Player's Attacking Slots
        self.cards_PlayerAttack = []
        for pileIndex in range(5):
            label = ttk.Label(self._frame, borderwidth=border, relief=relief)
            label.grid(column=pileIndex, row=1, padx=pad, pady=pad)
            label['image'] = Images.Blank
            self.cards_PlayerAttack.append(label)
            
        # Row1: Opponent's Discard Pile
        self.cards_OpponentDiscard = ttk.Label(self._frame, borderwidth=border, relief=relief)
        self.cards_OpponentDiscard.grid(column=5, row=1, padx=(10+pad,pad), pady=pad)
        self.cards_OpponentDiscard['image'] = Images.Blank

        # Row3: Opponent's Attacking Slots
        self.cards_OpponentAttack = []
        for pileIndex in range(5):
            label = ttk.Label(self._frame, borderwidth=border, relief=relief)
            label.grid(column=pileIndex, row=3, padx=pad, pady=pad)
            label['image'] = Images.Blank
            self.cards_OpponentAttack.append(label)
            
        # Row3: Player's Discard Pile
        self.cards_PlayerDiscard = ttk.Label(self._frame, borderwidth=border, relief=relief)
        self.cards_PlayerDiscard.grid(column=5, row=3, padx=(10+pad,pad), pady=pad)
        self.cards_PlayerDiscard['image'] = Images.Blank

        # Row4: Player's Deck
        self.cards_Player = []
        for pileIndex in range(5):
            pile = []
            self.cards_Player.append(pile)
            for cardIndex in range(5):
                card = CardImage(self._frame, gridCol=pileIndex, gridRow=4)
                card.index = 4 - cardIndex
                card.BindEvent('<1>', self.OnCardClick1)
                card.BindEvent('<Enter>', self.OnCardEnter1)
                card.BindEvent('<Leave>', self.OnCardLeave1)
                card.Show()
                pile.append(card)
            #    highlight = ttk.Label(self._frame)
            #    highlight.grid(column=pileIndex, row=4, padx=pad, pady=((4-cardIndex)*peek+pad,cardIndex*peek+pad))
            #    label = ttk.Label(highlight, borderwidth=border, relief=relief)
            #    label.grid()
            #    label.highlight = highlight
            #    label.pileIndex = pileIndex
            #    label.cardIndex = cardIndex
            #    label['image'] = Images.Blank
            #    label.bind('<1>', self.OnCardClick)
            #    label.bind('<Enter>', self.OnCardEnter)
            #    label.bind('<Leave>', self.OnCardLeave)
            #    pile.append(label)

        # Row4: Highlighted Card
        self.cards_HighlightedCard = ttk.LabelFrame(self._frame, width=width, height=height, borderwidth=border, relief='groove', text="Viewing", labelanchor='nw')
        #self.cards_HighlightedCard.grid(column=6, row=4, padx=pad, pady=pad)
        self.cards_HighlightedCard.grid(column=5, row=4, padx=pad, pady=(4*peek+pad,pad))
        self.cards_HighlightedCard.label = ttk.Label(self.cards_HighlightedCard)
        self.cards_HighlightedCard.label['image'] = Images.Blank
        self.cards_HighlightedCard.label.grid()

        # SneakAPeek Card
        self.cards_SneakAPeek = ttk.Label(self._frame, borderwidth=border, relief=relief)
        self.cards_SneakAPeek['image'] = Images.Blank
        self.cards_SneakAPeek.bind('<1>', self.SneakAPeek_Click)
        self.cards_SneakAPeek.bind('<Leave>', lambda e: self.cards_SneakAPeek.grid_forget())
        
    def _CreateGui(self, app:appBase):
        self._frame = ttk.Frame(app.window)
        self._frame.columnconfigure(0,weight=0) # pile 1
        self._frame.columnconfigure(1,weight=0) # pile 2
        self._frame.columnconfigure(2,weight=0) # pile 3
        self._frame.columnconfigure(3,weight=0) # pile 4
        self._frame.columnconfigure(4,weight=0) # pile 5
        self._frame.columnconfigure(5,weight=0) # discards
        self._frame.columnconfigure(6,weight=1) # ui
        self._frame.rowconfigure(0,weight=0) # opponent's cards
        self._frame.rowconfigure(1,weight=0) # your attack
        self._frame.rowconfigure(2,weight=1) # no man's land
        self._frame.rowconfigure(3,weight=0) # opponent's attack
        self._frame.rowconfigure(4,weight=0) # your cards
        self._CreateCards()

    def DrawCards(self, opponent:Deck, player:Deck):
        self.deckOpponent = opponent
        self.deckPlayer = player
        for pileIndex in range(5):
            self.cards_Opponent[pileIndex].BackImage = opponent.BackImage
            self.cards_Opponent[pileIndex]['image'] = opponent.BackImage
            pile = self.cards_Player[pileIndex]
            for cardIndex in range(5):
                pile[cardIndex].cardBack = player.BackImage
                pile[cardIndex].cardFace = player.Piles[pileIndex].PeekAt(cardIndex).FaceImage
                pile[cardIndex].ShowCardBack()
                #pile[cardIndex].BackImage = player.BackImage
                #pile[cardIndex].FaceImage = player.Piles[pileIndex].PeekAt(cardIndex).FaceImage
                #pile[cardIndex]['image'] = player.BackImage
        self.cards_OpponentDiscard['image'] = opponent.BackImage
        self.cards_PlayerDiscard['image'] = player.BackImage
                
    def BindKeys(self, app:appBase):
        app.window.bind('<Escape>', lambda e: app.NewGame())
    def UnBindKeys(self, app:appBase):
        app.window.bind('<Escape>', None)

    def __init__(self, app:appBase):
        super().__init__()
        self._CreateGui(app)
    
    def Show(self, app:appBase):
        self._frame.grid(column=0, row=0,sticky=(N, S), padx=5,pady=5)
        self.BindKeys(app)

    def Hide(self, app:appBase):
        # To remove a frame from a grid: frame.remove() to remember grid settings or frame.forget() to discard grid settings
        self.UnBindKeys(app)
        self._frame.grid_remove()
        
    def OnCardEnter(self, e):
        label = e.widget
        #pileIndex = label.pileIndex
        #cardIndex = label.cardIndex
        image = label.FaceImage
        label['image'] = image
        self.cards_HighlightedCard.label['image'] = image
        label.highlight['background'] = 'green'
        gridInfo = label.highlight.grid_info()
        padx = gridInfo['padx']
        pady = gridInfo['pady']
        label.grid_configure(padx=3, pady=3)
        label.highlight.grid_configure(padx=padx-3,pady=(pady[0]-3,pady[1]-3))
        
    def OnCardEnter1(self, e):
        #card = CardImage() #intellisense
        card = e.widget.CardImage
        card.ShowCardFace()
        self.cards_HighlightedCard.label['image'] = card.cardFace
        card.Highlight('green')
        
    def OnCardLeave1(self, e):
        #card = CardImage() #intellisense
        card = e.widget.CardImage
        card.ShowCardBack()
        card.Highlight('')
        self.cards_HighlightedCard.label['image'] = Images.Blank
        
    def OnCardLeave(self, e):
        label = e.widget
        #pileIndex = label.pileIndex
        #cardIndex = label.cardIndex
        label['image'] = self.deckPlayer.BackImage
        label.highlight['background'] = ''
        gridInfo = label.highlight.grid_info()
        padx = gridInfo['padx']
        pady = gridInfo['pady']
        label.grid_configure(padx=0, pady=0)
        label.highlight.grid_configure(padx=padx+3,pady=(pady[0]+3,pady[1]+3))
        
    def OnCardClick(self, e):
        label = e.widget
        if label.cardIndex < (self.deckPlayer.Piles[label.pileIndex].Count()-1):
            self.SneakAPeek(label)
            return
        
    def OnCardClick1(self, e):
        #card = CardImage() #intellisense
        card = e.widget.CardImage
        if card.index > 0:
            self.SneakAPeek(card._card)
            return

    def SneakAPeek(self, label):
        gridInfo = label.master.grid_info()
        self.cards_SneakAPeek.grid(column=gridInfo['column'], row=gridInfo['row'], padx=gridInfo['padx'], pady=gridInfo['pady'])
        self.cards_SneakAPeek['image'] = label.FaceImage
        self.cards_SneakAPeek.viewing = label

    def SneakAPeek_Click(self, e):
        self.cards_SneakAPeek.viewing['image'] = self.cards_SneakAPeek.viewing.FaceImage
        self.cards_SneakAPeek.grid_forget()