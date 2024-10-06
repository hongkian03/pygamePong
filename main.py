import pygame
from variables import *
from player import Player
from ball import Ball
from random import randint

#initialise stuff
pygame.init()
screen = pygame.display.set_mode(screen_dimensions)
clock = pygame.time.Clock()
ball = Ball(ball_r,screen_centre[0],screen_centre[1])
player1 = Player(player_l,player_h,player_x,player_y)
player2 = Player(player_l,player_h,(screen_dimensions[0]-player_x-player_l),player_y)
ball_polarity = [-1, 1]
game_font = pygame.font.SysFont(font,font_size)
start_text = game_font.render(text,True,white)
start_text_w, start_text_h = start_text.get_width(), start_text.get_height()

# draw function updates screen
def draw(screen,start):
    screen.fill(black)
    ball.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    score_text = game_font.render(f'{player1.score} - {player2.score}', True, white)
    score_text_w, score_text_h = score_text.get_width(), score_text.get_height()
    screen.blit(score_text, (screen_centre[0] - (score_text_w // 2), score_gap))

    if not start :
        screen.blit(start_text, (screen_centre[0] - (start_text_w // 2), screen_centre[1] - (start_text_h // 2) - start_gap))

running = True
start = False
while running :
    clock.tick(60)

    # check keypresses
    keys = pygame.key.get_pressed()

    # check start
    if keys[pygame.K_SPACE]:
        start = True
        ball.horv = ball_v * ball_polarity[randint(0, 1)] 
        ball.vertv = ball_v * ball_polarity[randint(0, 1)] 

    # check player movement
    if keys[pygame.K_w] and player1.y > 0 :
        player1.y -= player1.v

    if keys[pygame.K_s] and (player1.y + player1.h) < screen_dimensions[1] :
        player1.y += player1.v

    if keys[pygame.K_UP] and player2.y > 0 :
        player2.y -= player2.v

    if keys[pygame.K_DOWN] and (player2.y + player2.h) < screen_dimensions[1] :
        player2.y += player2.v

    # update ball position (constant)
    ball.x += ball.horv
    ball.y += ball.vertv

    # check ball hit upper or lower boundary
    if ball.y + ball.r >= screen_dimensions[1] or ball.y - ball.r <= 0 :
        ball.vertv *= -1

        if ball.vertv < 0 :
            ball.vertv -= speed_increment
        else :
            ball.vertv += speed_increment

    # check ball hit player1
    if (player1.y <= (ball.y + ball.r)) and ((ball.y - ball.r) <= (player1.y + player1.h)) and ((ball.x - ball.r) <= player1.x + player1.l) :
        ball.horv *= -1
        ball.horv += speed_increment

    # check ball hit player2
    if (player2.y <= (ball.y + ball.r)) and ((ball.y - ball.r) <= (player2.y + player2.h))  and ((ball.x + ball.r) >= player2.x) :
        ball.horv *= -1
        ball.horv -= speed_increment

    # check player1 win
    if ball.x > screen_dimensions[0] + win_gap :
        pygame.time.delay(delay)
        player1.score += 1
        start = False
        ball.horv = 0 
        ball.vertv = 0
        ball.x, ball.y = screen_centre

    # check player2 win
    if ball.x < -win_gap :
        pygame.time.delay(delay)
        player2.score += 1
        start = False
        ball.horv = 0 
        ball.vertv = 0
        ball.x, ball.y = screen_centre

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    draw(screen, start)
    pygame.display.update()

pygame.quit()
            