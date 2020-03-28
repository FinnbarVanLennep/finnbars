import pygame, sys, os

def ball_movement():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # screen boundaries
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player):
        ball_speed_y *= -1


# General setyp
pygame.init()
clock = pygame.time.Clock()

# Maind Window
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Pong')

# Game rectangles
ball_size = 30
ball = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size,ball_size)
player = pygame.Rect(screen_width/2 - 70, screen_height - 10, 140,10)

bg_color = pygame.Color('black')
light_grey = (230,230,230)

ball_speed_x = 0
ball_speed_y = -20

player_speed = 0

while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEMOTION:
            mouse_loc = pygame.mouse.get_pos()
            player.center = mouse_loc

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed -= 7
            if event.key == pygame.K_RIGHT:
                player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_speed += 7
            if event.key == pygame.K_RIGHT:
                player_speed -= 7
            if event.key = pygame.K_z:


    player.x += player_speed

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            ball.x = screen_width / 2 - ball_size / 2
            ball.y = screen_height/2 - ball_size/2

    # swing_motion


    ball_movement()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.ellipse(screen,light_grey,ball)
    # box around screen
    pygame.draw.aaline(screen, light_grey,(0,0),(0,screen_height))
    pygame.draw.aaline(screen, light_grey,(0,0),(screen_width,0))
    pygame.draw.aaline(screen, light_grey,(screen_width-1,0),(screen_width-1,screen_height))
    # middle screen line
    pygame.draw.aaline(screen, light_grey,(0,screen_height/2),(screen_width,screen_height/2))

    # updating the window
    pygame.display.flip()
    clock.tick(60)