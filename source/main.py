# DMgine v0.3 - Traversal, Combat, and Encounters

import os
import pyfiglet as figlet
import numpy as np
import pickle

Tmp = ''

class Game:
    def __init__(self) -> None:
        self.players = []
        self.NPCs = []
        self.map = []


    def MenuMain(self):
        print(figlet.figlet_format("Adventure To Taika", width=200))
        print("(N)ew game \n(C)haracter creation \n(H)elp")
        return input("\n>")

    def MakeChar(self):
        while True:
            self.players.append(Player(input("choose your name adventurer:")))
            if (input("Do you want to create another character? (Y/N)")).lower() == "n":
                break
    
    def MakeNPC(self, Name):
        self.NPCs.append(NPC(Name))
    
    def NewGame(self):
        self.MakeChar()

    def LoadGame(self):
        pass

    def SaveGame(self):
        pass

    def RunGame(self): #Main game loop
        print("(C)ombat (E)ncounter (S)ave (Q)uit \n")
        Com = input(">") 
        if Com.lower() == "c":
            self.Combat()
        elif Com.lower() == "e":    
            self.Encounter()
        elif Com.lower() == "s":
            self.SaveGame()
        elif Com.lower() == "q":
            pass
    def Encounter(self):
        pass

    def Combat(self): #determine order with dexterity check, then call turn() for each player and npc TODO: refactor to use dexterity check
        while True:
            for player in self.players:
                player.turn()
            for npc in self.NPCs:
                npc.turn()
            if (input("Continue combat? (Y/N)")).lower() == "n":
                break
        
        



class Player():
    def __init__(self, Name) -> None:
        self.Name = Name 
        self.info = {"HP": 10, "AC": 10}
        self.Stats = {"str":np.random.randint(0,20), "dex":np.random.randint(0,20), "con":np.random.randint(0,20), "int":np.random.randint(0,20), "wis":np.random.randint(0,20), "cha":np.random.randint(0,20)}
        self.inv = {}
        print(self.Stats)

    def turn(self):
        print("Player turn")

    def move(self):
        pass

class NPC():
    def __init__(self, Name, Friends, Foes) -> None:
        self.Name = Name 
        self.Stats = {"str":0, "dex":0, "con":0, "int":0, "wis":0, "cha":0}
        self.inv = {}
        self.Friends = [Friends]
        self.Foes = [Foes]

    def turn(self):
        pass

    def move(self):
        pass
    
    def attack(self):
        pass


#Main Execution block
DM = Game()
Com = DM.MenuMain()

if Com.lower() == "n":
    DM.NewGame()
    DM.RunGame()