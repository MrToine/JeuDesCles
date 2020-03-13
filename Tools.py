# -*-coding:utf-8-*-

import pygame
from pygame.locals import *

from constants import *
from Board import *

class Tools():
    """
    classe qui contiens plusieurs fonctions utiles. Elle contiens également
    la boucle principal du programme et la fonction de contrôles
    """
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption(GAME_TITLE)
        if self.done == False:
            self.event_loop()

    def controles_quit(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.done = True

    def event_loop(self):
        while not self.done:
            self.controles_quit()
            ### On défini ici le premier état a charger lors du lancement de la fenëtre
            first_load_State = Board(self.screen)
        pygame.quit()
        quit()