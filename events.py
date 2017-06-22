from menu import menuOptions
from classes import Creature
import sys

class newEncounter:
    def __init__(self, menu, player):
        self.menu = menu
        self.player = player

    def battle(self, enc):
        enemy = Creature(enc['creature'])
        last_turn = 'You\'re fighting a ' + enemy.name
        while True:

            # Construct the top menu
            self.menu.scrn.clear()
            self.menu.scrn.addstr('Battle\n')
            self.menu.scrn.addstr(self.player.name + ' -- HP: ' + \
                                  str(self.player.hp) + '\n')
            self.menu.scrn.addstr(enemy.name + ' -- HP: ' + \
                                  str(enemy.hp) + '\n')
            self.menu.add_text(last_turn)

            # Victory condition
            if enemy.hp <= 0:
                self.player.xp += enemy.xp_on_kill
                self.menu.add_text('You defeated the ' + enemy.name + \
                                   '! (ENTER)')
                self.menu.enter_wait()
                break

            choice, quit = self.menu.player_choice(self.player.moves)

            # Take into account the quit option
            if quit == 1:
                sys.exit(0)

            # If the player chose to run
            if choice['title'] == 'Run':
                self.menu.add_text('You run away! (ENTER)')
                self.menu.enter_wait()
                break
            # Otherwise perform the chosen attack
            else:
                dmg = choice['dmg']
                enemy.hp -= dmg
                last_turn = 'You attacked for ' + str(dmg) + ' damage!'

    def shop(self, enc):
        self.menu.add_text('shop')
