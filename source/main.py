# DMgine v0.2 - Test menu and character creation

import os
import pyfiglet as figlet

Tmp = ''

class Game:
    def __init__(self) -> None:
        players = {}

    def MenuMain():
        print(figlet.figlet_format("Adventure To Taika", width=200))
        print("(N)ew game \n(C)haracter creation \n(H)elp")
        return input("\n>")

    def MakeChar():
        Player(input("choose your name adventurer:"))

class Player():
    def __init__(self, Name) -> None:
        self.Name = Name 
        self.Stats = {"str":0, "dex":0, "con":0, "int":0, "wis":0, "cha":0}

class NPC():
    def __init__(self, Name) -> None:
        self.Name = Name 
        self.Stats = {"str":0, "dex":0, "con":0, "int":0, "wis":0, "cha":0}


Tmp = Game.MenuMain()

if Tmp.lower() == "c":
    Game.MakeChar()
