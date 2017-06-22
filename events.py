from menu import menuOptions
from classes import Creature
import sys

class newEncounter:
    def __init__(self, menu, player):
        self.menu = menu
        self.player = player

    def battle(self, enc):
        enemy = Creature(enc['creature'])

        while True:

            self.menu.scrn.clear()
            self.menu.scrn.addstr('Battle\n')
            self.menu.scrn.addstr('Creature: ' + enemy.name + '\n')

            if enemy.hp <= 0:
                break

            choice, quit = self.menu.player_choice(self.player.moves)

            if quit == 1:
                sys.exit(0)

            if choice['title'] == 'Run':
                self.menu.add_text('You run away! (ENTER)')
                self.menu.enter_wait()
                break

    def shop(self, enc):
        self.menu.add_text('shop')
