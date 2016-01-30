from tkinter import PhotoImage
import random

class Images(object):
    """description of class"""
    
    def LoadImages():
        Images.Blank = PhotoImage(width=70,height=100)
        Images.MainMenu = PhotoImage(file='Images\\main menu.gif')
        Images.Backs = []
        Images.Backs.append(PhotoImage(file='Images\\back_adorably hideous.gif'))
        
    def GetRandomBack()->PhotoImage:
        return random.choice(Images.Backs)