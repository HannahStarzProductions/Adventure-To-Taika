# DMgine v0.2 - Test menu and character creation

import os
import pyfiglet as figlet
import numpy as np

Tmp = ''

class Game:
    def __init__(self) -> None:
        players = []
        map = []


    def MenuMain(self):
        print(figlet.figlet_format("Adventure To Taika", width=200))
        print("(N)ew game \n(C)haracter creation \n(H)elp")
        return input("\n>")

    def MakeChar(self):
        while True:
            Player(input("choose your name adventurer:"))
            if (input("Do you want to create another character? (Y/N)")).lower() == "n":
                break
    
    def NewGame(self):
        DM.MakeChar()

    def LoadGame(self):
        pass

    def SaveGame(self):
        pass

    def Encounter(self):
        pass
        



class Player():
    def __init__(self, Name) -> None:
        self.Name = Name 
        self.Stats = {"str":np.random.randint(0,20), "dex":np.random.randint(0,20), "con":np.random.randint(0,20), "int":np.random.randint(0,20), "wis":np.random.randint(0,20), "cha":np.random.randint(0,20)}
        self.inv = {}
        print(self.Stats)

class NPC():
    def __init__(self, Name) -> None:
        self.Name = Name 
        self.Stats = {"str":0, "dex":0, "con":0, "int":0, "wis":0, "cha":0}


#Main Execution block
DM = Game()
Com = DM.MenuMain()

if Com.lower() == "n":
    DM.NewGame()
