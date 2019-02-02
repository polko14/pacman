import pygame
from pygame.locals import *
from MapCreator import *
from Menu import *
from LevelSelect import *
from Ranking import *
from Game import *
from Rules import *
PLAYING = True
MENU = 0
PLAY_LEVEL_SELECT = 1
GAME = 2
TOPSCORE_LEVEL_SELECT = 3
TOPSCORE = 4
MAP_CREATOR = 6
EXIT = 7
RULES = 8
CURRENT = MENU
FILE = ""
while PLAYING:
    if CURRENT == MENU:
        CURRENT = menu()
    if CURRENT == PLAY_LEVEL_SELECT:
        CURRENT, FILE = level_select(1)
    if CURRENT == GAME:
        CURRENT = game(FILE)
    if CURRENT == TOPSCORE_LEVEL_SELECT:
        CURRENT, FILE = level_select(2)
    if CURRENT == TOPSCORE:
        CURRENT = ranking(FILE)
    if CURRENT == RULES:
        CURRENT = rules()
    if CURRENT == MAP_CREATOR:
        mapcreator()
        CURRENT = MENU
    if CURRENT == EXIT:
        PLAYING = False
