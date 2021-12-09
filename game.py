import pygame
import random


# pygame initialization
pygame.init()

# window setup
width = 800
length = 600
win = pygame.display.set_mode((width, length))
pygame.display.set_caption('Multiplayer - ping pongw game')

# player A
playera = pygame.image.load('paddle.png')
player_a = pygame.transform.rotate(pygame.transform.scale(playera, (75, 35)), 90)
player_a_x = 1
player_a_y = 300

# player B
playerb = pygame.image.load('paddle.png')
player_b = pygame.transform.rotate(pygame.transform.scale(playera, (75, 35)), 90)
player_b_x = 765
player_b_y = 300

# background
background = pygame.image.load('soccer-bg.jpg')
bg = pygame.transform.scale(background, (800, 600))
# ball
ball = pygame.image.load('ball.png')
ball_x = 400
ball_y = 300
ball_speed = 0.2
ball_px = ball_x   # ball previous x

# score
a_score = 0
b_score = 0
font = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.Font('freesansbold.ttf', 32)

def ball_direction(ball_speed):
    global ball_x, ball_y
    global b_score, a_score
    global flag
    global ball_px

    if flag == 1:
        ball_y += ball_speed
        ball_x -= ball_speed
    if flag == 0:
        ball_x -= ball_speed
        ball_y -= ball_speed
    if flag == 2:
        ball_y += ball_speed
        ball_x += ball_speed
    if flag == 3:
        ball_y -= ball_speed
        ball_x += ball_speed

    if ball_y < 16:
        if ball_px - ball_x > 0:
            flag = 1
        elif ball_px-ball_x < 0:
            flag = 2
    if ball_x < 1:
        ball_x = 400
        ball_y = 300
        b_score += 1
        flag = random.randint(0, 3)

    if ball_y > 586:
        if ball_px - ball_x > 0:
            flag = 0
        elif ball_px - ball_x < 0:
             flag = 3
    if ball_x > 785:
        ball_x = 400
        ball_y = 300
        a_score += 1
        flag = random.randint(0, 3)

    ball_px = ball_x

def display_score():
    score_of_a = font.render("Score : " + str(a_score), True, (255, 0, 0))
    win.blit(score_of_a, (150, 50))
    score_of_b = font.render("Score : " + str(b_score), True, (0, 0, 255))
    win.blit(score_of_b, (550, 50))


def playerA(player_a_x, player_a_y):
    win.blit(player_a, (player_a_x, player_a_y))


def playerB(player_b_x, player_b_y):
    win.blit(player_b, (player_b_x, player_b_y))

def game_ending():
    global ball_x, ball_y, ball_speed
    if a_score == 5:
        ball_x = 400
        ball_y = 300
        ball_speed = 0
        a_win = font.render("Player A won", True, (255, 0, 0))
        win.blit(a_win, (200, 300))
        game_over = font2.render("GAME OVER", True, (255, 255, 255))
        win.blit(game_over, (300, 400))
    if b_score == 5:
        ball_x = 400
        ball_y = 300
        ball_speed = 0
        b_win = font.render("Player B won", True, (0, 0, 255))
        win.blit(b_win, (600, 300))
        game_over = font2.render("GAME OVER", True, (255, 255, 255))
        win.blit(game_over, (300, 400))

r = random.randint(0, 3)
flag = r # to determine the ball's direction

# Game loop
running = True
while running:
    win.fill((255, 255, 255))
    win.blit(bg, (1, 1))
    playerA(player_a_x, player_a_y)
    playerB(player_b_x, player_b_y)
    win.blit(ball, (ball_x, ball_y))
    display_score()
    player_a_top = player_a_y
    player_a_bottom = player_a_y + 75
    player_b_top = player_b_y
    player_b_bottom = player_b_y + 75
    game_ending()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w]:
        player_a_y -= 0.5
        # boundary limit
        if player_a_y < 1:
            player_a_y = 3
        playerA(player_a_x, player_a_y)

    if key_pressed[pygame.K_s]:
        player_a_y += 0.5
        # boundary limit
        if player_a_y > 525:
            player_a_y = 525
        playerA(player_a_x, player_a_y)

    if key_pressed[pygame.K_UP]:
        player_b_y -= 0.5
        # boundary limit
        if player_b_y < 1:
            player_b_y = 3
        playerB(player_b_x, player_b_y)

    if key_pressed[pygame.K_DOWN]:
        player_b_y += 0.5
        # boundary limit
        if player_b_y > 525:
            player_b_y = 525
        playerB(player_b_x, player_b_y)

    # paddle and ball collision
    if ball_x < 30 and (ball_y > player_a_top and ball_y < player_a_bottom):
        if key_pressed[pygame.K_w]:
            flag = 3
        else:
            flag = 2

    if ball_x > 765 and (ball_y > player_b_top and ball_y < player_b_bottom):
        if key_pressed[pygame.K_UP]:
            flag = 0
        else:
            flag = 1
    ball_direction(ball_speed)



