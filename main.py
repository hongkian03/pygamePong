import pygame
from variables import *
from player import Player
from ball import Ball

#initialise stuff
pygame.init()
screen = pygame.display.set_mode(screen_dimensions)
ball = Ball(ball_r,screen_centre[0],screen_centre[1])
player1 = Player(player_l,player_h,player_x,player_y)
player2 = Player(player_l,player_h,(screen_dimensions[0]-player_x-player_l),player_y)
game_font = pygame.font.SysFont(font,font_size)
start_text = game_font.render(text,True,white)
start_text_w, start_text_h = game_font.size(start_text)

def draw(screen,start):
    screen.fill(black)
    ball.draw(screen)
    player1.draw(screen)
    player2.draw(screen)

    if not start :
        screen.blit(start_text,())

running = True
start = False
while running :

    #check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    draw(screen)
    pygame.display.update()

pygame.quit()
            