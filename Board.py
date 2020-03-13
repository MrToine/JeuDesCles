# -*-coding:utf-8-*-

from utils import *
from constants import *
import pygame
from pygame.locals import *


class Board:
    """
    Classe qui contiens toutes les infos et
    les possibilités efféctué sur le plateau
    """

    def __init__(self, screen):
        """

        """
        self.screen = screen
        self.wall = load_img(WALL)
        self.chest = load_img(CHEST)
        self.keys = {}
        for key, value in KEYS.items():
            self.keys[key] = load_img(value)
            print(key)



    def gird(nb_blocs):
        tab_gird = []
        for i in range(nb_blocs):
            tab_gird.append([''] * nb_blocs)