import pygame, sys, random

# if playin against computer, computer = 1. Otherwise human
global computer
computer = 1

# old_ball_loc = 0

def between(test_obj, old_loc, new_loc):
    if (test_obj >= old_loc and test_obj <= new_loc) or (test_obj <= old_loc and test_obj >= new_loc):
        return True
    else:
        return False


# # only works with integers because of range
# def collision(polyhedron):
#
#     if  polyhedron.ce



def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_start()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1


def player1_animation():
    player1.y += player1_speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height


def player2_animation(computer):
    if computer == 1:
        if player2.top < ball.y:
            player2.y += player2_speed
        if player2.bottom > ball.y:
            player2.y -= player2_speed

        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= screen_height:
            player2.bottom = screen_height

    else:
        player2.y += player2_speed

        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= screen_height:
            player2.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Pong')

# Colors
light_grey = (230, 230, 230)
bg_color = pygame.Color('black')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player1_speed = 0
if computer == 1:
    player2_speed = 7
else:
    player2_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        # player 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed -= 6
            if event.key == pygame.K_DOWN:
                player1_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed += 6
            if event.key == pygame.K_DOWN:
                player1_speed -= 6
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed -= 6
            if event.key == pygame.K_DOWN:
                player1_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed += 6
            if event.key == pygame.K_DOWN:
                player1_speed -= 6

        # player2
        if computer == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player2_speed -= 6
                if event.key == pygame.K_z:
                    player2_speed += 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player2_speed += 6
                if event.key == pygame.K_z:
                    player2_speed -= 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player2_speed -= 6
                if event.key == pygame.K_z:
                    player2_speed += 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player2_speed += 6
                if event.key == pygame.K_z:
                    player2_speed -= 6

        # if event.key == pygame.K_j:
        #     player1_swing_up = 1
        # if event.key == pygame.K_m:
        #     player1.swing_down = 1


    # Game Logic
    ball_animation()
    player1_animation()
    player2_animation(computer)


    # Visuals
    screen.fill(bg_color)
    hinder = pygame.draw.polygon(screen, light_grey, ((400, 400), (450, 450), (400, 380), (450, 430)), )

    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    lijn = pygame.draw.line(screen, light_grey, (0, 0), (screen_width,player1.y))

    print(lijn.center)


    pygame.display.flip()
    clock.tick(60)
