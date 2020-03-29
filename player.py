import pygame

class Player(pygame.Rect):
    def __init__(self, start_x, start_y, UP=None, DOWN=None, LEFT=None, RIGHT=None, computer=False, width=10, heigth=140):
        super(Player, self).__init__(start_x, start_y, width, heigth)
        self.speed = 8
        self.speed_x = 0
        self.speed_y = 0
        self.computer = computer
        if not computer:
            exec(f"self.UP = pygame.K_{UP}")
            exec(f"self.DOWN = pygame.K_{DOWN}")
            exec(f"self.LEFT = pygame.K_{LEFT}")
            exec(f"self.RIGHT = pygame.K_{RIGHT}")


    def animation(self, screen_height, ball):

        if self.computer:
            if self.centery < ball.y:
                self.y += self.speed
            elif self.centery > ball.y:
                self.y -= self.speed

            if self.top <= 0:
                self.top = 0
            elif self.bottom >= screen_height:
                self.bottom = screen_height

        else:
            self.y += self.speed_y
            self.x += self.speed_x
            if self.top <= 0:
                self.top = 0
            elif self.bottom >= screen_height:
                self.bottom = screen_height

    def actions(self,event):
        if self.computer:
            return

        if event.type == pygame.KEYDOWN:
            if event.key == self.UP:
                self.speed_y -= self.speed
            if event.key == self.DOWN:
                self.speed_y += self.speed
            if event.key == self.LEFT:
                self.speed_x -= self.speed
            if event.key == self.RIGHT:
                self.speed_x += self.speed

        if event.type == pygame.KEYUP:
            if event.key == self.UP:
                self.speed_y += self.speed
            if event.key == self.DOWN:
                self.speed_y -= self.speed
            if event.key == self.LEFT:
                self.speed_x += self.speed
            if event.key == self.RIGHT:
                self.speed_x -= self.speed