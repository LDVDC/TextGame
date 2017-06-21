from menu import menuOptions
from classes import Creature
import sys

class newEncounter:
    def __init__(self, menu):
        self.menu = menu

    def battle(self, enc):
        choices = [{'title':'Attack'},{'title':'Run'}]
        enemy = Creature(enc['creature'])

        while True:

            self.menu.scrn.clear()
            self.menu.scrn.addstr('Battle\n')
            self.menu.scrn.addstr('Creature: ' + enemy.name + '\n')

            if enemy.hp <= 0:
                break

            choice, quit = self.menu.player_choice(choices)

            if quit == 1:
                sys.exit(0)

    def shop(self, enc):
        self.menu.add_text('shop')
