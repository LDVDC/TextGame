from menu import menuOptions
from classes import Creature
import sys
import random
from numpy.random import choice as rand_choice

class newEncounter:
    def __init__(self, menu, player):
        self.menu = menu
        self.player = player

    def battle(self, enc):
        enemy = Creature(enc['creature'])
        self.last_turn = 'You\'re fighting a ' + enemy.name
        while True:

            # Construct the top menu
            self.menu.scrn.clear()
            self.menu.scrn.addstr('Battle\n')
            self.menu.scrn.addstr(self.player.name + ' -- HP: ' + \
                                  str(self.player.hp) + '\n')
            self.menu.scrn.addstr(enemy.name + ' -- HP: ' + \
                                  str(enemy.hp) + '\n')
            self.menu.add_text(self.last_turn)

            choice, quit = self.menu.player_choice(self.player.moves['detail'])

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
                self.last_turn = ''
                dmg = self.gen_dmg(self.player, choice, enemy)
                enemy.hp -= dmg
                self.last_turn += 'You attacked for ' + str(dmg) + ' damage!\n'

            # Victory condition
            if enemy.hp <= 0:
                self.player.xp += enemy.xp_on_kill
                self.menu.add_text('You defeated the ' + enemy.name + \
                                   '! (ENTER)')
                self.menu.enter_wait()
                break

            # Enemy turn
            enemy_attack = rand_choice(enemy.moves['detail'], 1,
                                       enemy.moves['prob'])[0]
            en_dmg = self.gen_dmg(enemy, enemy_attack, self.player)
            self.player.hp -= en_dmg
            self.last_turn += enemy.name + ' attacked for ' + str(en_dmg) + \
                              ' damage!'

    def gen_dmg(self, attacker, move, defender):
        dmg = move['dmg'] + (attacker.stats['str'] * 5)
        rand = random.random()
        if rand <= attacker.stats['crit_ch']:
            dmg = dmg * 3
            self.last_turn += 'CRIT! '
        dmg -= dmg * (defender.stats['def']/100) * 5
        return dmg

    def shop(self, enc):
        self.menu.add_text('shop')
