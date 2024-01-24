import pygame
from variables import *

class Ball :
    def __init__(self,r,x,y,v=ball_v):
        self.r = r
        self.x = x
        self.y = y
        self.v = v

    def draw(self,screen):
        pygame.draw.circle(screen,white,(self.x,self.y),self.r)