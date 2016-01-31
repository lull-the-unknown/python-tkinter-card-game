from tkinter import PhotoImage
import random

class AppImages(object):
    """description of class"""
    
    def LoadImages():
        AppImages.Blank = PhotoImage(width=70,height=100)
        AppImages.MainMenu = PhotoImage(file='Images\\main menu.gif')
        AppImages.Backs = []
        AppImages.Backs.append(PhotoImage(file='Images\\back_adorably hideous.gif'))
        
    def GetRandomBack()->PhotoImage:
        return random.choice(AppImages.Backs)