import pygame
from variables import *

class Ball :
    def __init__(self, r, x, y, vert_v = 0, hor_v = 0):
        self.r = r
        self.x = x
        self.y = y
        self.vertv = vert_v
        self.horv = hor_v

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.x, self.y), self.r)