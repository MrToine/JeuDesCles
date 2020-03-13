# -*-coding:utf-8-*-

import pygame

def load_img(img):
    return pygame.image.load(img).convert_alpha()