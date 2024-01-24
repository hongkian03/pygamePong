import pygame
from variables import *

class Player :
    def __init__(self,l,h,x,y,v=player_v):
        self.l = l
        self.h = h
        self.x = x
        self.y = y
        self.v = v
        self.shape = pygame.Rect((self.x,self.y),(self.l,self.h))
    def draw(self,screen):
        pygame.draw.rect(screen,white,self.shape)