import random, pygame, sys


class Game:
    def __init__(self, width, height):

        # General setup
        pygame.init()
        self.clock = pygame.time.Clock()

        # Main Window
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Pong')

        # Colors
        self.light_grey = (236, 236, 236)
        self.bg_color = pygame.Color('black')

        # Game Rectangles
        # self.ball = pygame.Rect(self.screen_width / 2 - 15, self.screen_height / 2 - 15, 30, 30)
        #
        # self.ball_speed_x = 8 * random.choice((1, -1))
        # self.ball_speed_y = 8 * random.choice((1, -1))
        self.score1, self.score2 = 0, 0
        self.players = []
        self.balls = []

    def add_player(self, player):
        self.players.append(player)

    def add_ball(self, ball):
        self.balls.append(ball)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                # player 1 up, down, left, right
                for player in self.players:
                    player.actions(event)

            # Game Logic
            for ball in self.balls:
                ball.animation(self)
            for player in self.players:
                player.animation(self.screen_height, ball)

            # Visuals
            self.screen.fill(self.bg_color)

            # box around screen
            pygame.draw.aaline(self.screen, self.light_grey, (0, 0), (0, self.screen_height))
            pygame.draw.aaline(self.screen, self.light_grey, (0, 0), (self.screen_width, 0))
            pygame.draw.aaline(self.screen, self.light_grey, (self.screen_width - 1, 0), (self.screen_width - 1,self.screen_height + 5))
            pygame.draw.aaline(self.screen, self.light_grey, (0,self.screen_height - 1), (self.screen_width,self.screen_height - 1))
            pygame.draw.aaline(self.screen, self.light_grey, (self.screen_width / 2, 0), (self.screen_width / 2,self.screen_height))

            # movables
            for player in self.players:
                pygame.draw.rect(self.screen, self.light_grey, player)
            for ball in self.balls:
                pygame.draw.ellipse(self.screen, self.light_grey, ball)

            font = pygame.font.SysFont('calibri', 64)

            score = font.render(f"{self.score1}    {self.score2}", True, (255, 255, 255))
            self.screen.blit(score, (self.screen_width / 2 - 60, 15))

            pygame.display.flip()
            self.clock.tick(200)