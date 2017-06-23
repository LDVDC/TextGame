from lib.data.locations import main_locations
from lib.data.encounters import main_encounters
import events
import startup
import curses
from numpy.random import choice
from menu import menuOptions

class Game:
    def advance_day(self):
        self.player.location = 'loc_camp'
        if self.player.time % 24 > 8:
            self.player.time += 24
        self.player.time += 8 - (self.player.time % 24)

    def main(self, stdscr):
        # Start the game!
        curses.curs_set(0)
        self.scr = stdscr
        self.menu = menuOptions(self.scr)
        game_start = startup.GameStart(self.scr)
        game_start.loadChoice()
        self.player = game_start.player

        self.chosen = {'text':'You\'re standing in camp'}
        # Main gameplay loop
        while True:
            self.scr.clear()

            loc_dict = main_locations[self.player.location]
            menu_text = self.menu.gen_menu(self.player,self.chosen,loc_dict)
            self.scr.addstr(menu_text)
            self.menu.add_text(self.chosen['text'])

            # Check if we need to go to sleep
            if self.player.time % 24 > 22 or self.player.time % 24 < 6:
                self.menu.add_text('It\'s late. You go to sleep... (ENTER)')
                self.menu.enter_wait()
                self.advance_day()
                self.clear_chosen()
                continue

            ### This is the pause for input ###
            self.chosen, quit = self.menu.player_choice(loc_dict['options'])
            ### This is the pause for input ###

            if quit == 1:
                break

            self.player.location = self.chosen['new_loc']
            self.player.time += self.chosen['time']

            # Generate the outcome
            outcome = choice(self.chosen['outcomes']['details'], 1,
                             self.chosen['outcomes']['prob'])[0]

            # Check if the outcome has any special effects
            if 'hp_reg' in outcome:
                self.player.hp += self.player.stats['maxhp'] * outcome['hp_reg']
                if self.player.hp > self.player.stats['maxhp']:
                    self.player.hp = self.player.stats['maxhp']

            # Check if we got an encounter
            if outcome['title'] != 'enc_nothing':
                new_enc = events.newEncounter(self.menu, self.player)
                encounter = main_encounters[outcome['title']]
                self.clear_chosen()
                if encounter['type'] == 'battle':
                    new_enc.battle(encounter)
                elif encounter['type'] == 'shop':
                    new_enc.shop(encounter)
                else:
                    self.menu.add_text('Unsupported encounter type!')

            # Check if we leveled up
            if self.player.xp >= self.player.next_xp:
                self.level_up()

            self.scr.refresh()

    def clear_chosen(self):
        self.chosen = {'text':''}

    def level_up(self):
        self.player.lvl += 1
        self.player.xp = 0
        self.player.next_xp += 40
        self.player.hp = self.player.stats['maxhp']
        self.menu.add_text('You leveled up! (ENTER)')
        self.menu.enter_wait()
        return
