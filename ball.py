import pygame, random

class Ball(pygame.Rect):
    def __init__(self, start_x, start_y, width, height):
        super(Ball, self).__init__(start_x, start_y, width, height)
        self.speed = 8
        self.speed_y = random.choice((1, -1)) * self.speed
        self.speed_x = random.choice((1, -1)) * self.speed

    def start(self, start_x, start_y):
        self.center = start_x, start_y
        self.speed_y = random.choice((1, -1)) * self.speed
        self.speed_x = random.choice((1, -1)) * self.speed

    def animation(self, game):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.top <= 0 or self.bottom >= game.screen_height:
            self.speed_y *= -1
        if self.left <= 0:
            game.score1 += 1
            self.start(game.screen_width / 2, game.screen_height / 2)

        if self.right >= game.screen_width:
            game.score2 += 1
            self.start(game.screen_width / 2, game.screen_height / 2)

        for player in game.players:
            if self.colliderect(player):
                self.speed_x *= -1
                if self.centerx < player.centerx:
                    self.right = player.left
                else:
                    self.left = player.right
