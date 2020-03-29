import pygame, sys, random

# if playin against computer, computer = 1. Otherwise human
computer = 1

def between(test_obj, old_loc, new_loc):
    if (test_obj >= old_loc and test_obj <= new_loc) or (test_obj <= old_loc and test_obj >= new_loc):
        return True
    else:
        return False

def ball_animation():
    global ball_speed_x, ball_speed_y,score2,score1

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        score1 += 1
        ball_start()

    if ball.right >= screen_width:
        score2 += 1
        ball_start()

    if ball.colliderect(player1):
        ball_speed_x *= -1
        ball.right = player1.left
    if ball.colliderect(player2):
        ball_speed_x *= -1



def player1_animation():
    player1.y += player1_speed_y
    player1.x += player1_speed_x
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height


def player2_animation(computer):
    if computer == 1:
        if player2.centery < ball.y:
            player2.y += player2_speed
        if player2.centery > ball.y:
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
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Pong')

# Colors and fonts
light_grey = (236, 236, 236)
bg_color = pygame.Color('black')
font = pygame.font.SysFont('calibri', 64)

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player1 = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Game Variables
ball_speed_x = 8 * random.choice((1, -1))
ball_speed_y = 8 * random.choice((1, -1))
player1_speed_y, player1_speed_x = 0,0
speed = 8
score1, score2 = 0,0

if computer == 1:
    player2_speed = 10
else:
    player2_speed = 0

onzin = pygame.K_UP

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        # player 1 up, down, left, right
        if event.type == pygame.KEYDOWN:
            if event.key == onzin:
                player1_speed_y -= speed
            if event.key == pygame.K_DOWN:
                player1_speed_y += speed
            if event.key == pygame.K_LEFT:
                player1_speed_x -= speed
            if event.key == pygame.K_RIGHT:
                player1_speed_x += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed_y += speed
            if event.key == pygame.K_DOWN:
                player1_speed_y -= speed
            if event.key == pygame.K_LEFT:
                player1_speed_x += speed
            if event.key == pygame.K_RIGHT:
                player1_speed_x -= speed

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

    # Game Logic
    ball_animation()
    player1_animation()
    player2_animation(computer)

    # Visuals
    screen.fill(bg_color)

    # box around screen
    pygame.draw.aaline(screen, light_grey,(0,0),(0,screen_height))
    pygame.draw.aaline(screen, light_grey,(0,0),(screen_width,0))
    pygame.draw.aaline(screen, light_grey,(screen_width-1,0),(screen_width-1,screen_height+5))
    pygame.draw.aaline(screen, light_grey,(0,screen_height-1),(screen_width,screen_height-1))
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # movables
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)

    score = font.render(f"{score1}    {score2}", True, (255, 255, 255))
    screen.blit(score, (screen_width/2 - 60, 15))

    pygame.display.flip()
    clock.tick(200)
