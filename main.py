from game import Game
from player import Player
from ball import Ball

if __name__ == '__main__':
    game = Game(1600, 900)
    game.add_ball(Ball(game.screen_width / 2 - 15, game.screen_height / 2 - 15, 30, 30))
    game.add_ball(Ball(game.screen_width / 2 - 15, game.screen_height / 2 - 15, 20, 20))
    game.balls[0].speed = 6
    game.balls[1].speed = 9

    game.add_player(Player(game.screen_width - 20, game.screen_height / 2 - 70, 'UP', 'DOWN', 'LEFT', 'RIGHT'))
    game.add_player(Player(10, game.screen_height / 2 - 70, 'w', 's', 'a', 'd'))

    game.run()