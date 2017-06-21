from locations import main_locations
from encounters import main_encounters
from creatures import main_creatures
import enc_funcs
import startup
from numpy.random import choice
import menu_funcs as menu

class Game:
    def advance_day(self):
        self.player.location = 'loc_camp'
        if self.player.time % 24 > 8:
            self.player.time += 24
        self.player.time += 8 - (self.player.time % 24)

    def encounter(self, enc_name):
        enc_dict = main_encounters[enc_name]
        self.scr.clear()
        self.scr.addstr('Battle Time!' + enc_dict['creature'])
        self.scr.getch()

    def main(self, stdscr):
        # Start the game!
        self.scr = stdscr
        game_start = startup.GameStart()
        game_start.loadChoice(self.scr)
        self.player = game_start.player

        chosen = {'text':'You\'re standing in camp'}
        # Main gameplay loop
        while True:
            self.scr.clear()

            loc_dict = main_locations[self.player.location]
            menu_text = menu.gen_menu(self.player,chosen,loc_dict)
            self.scr.addstr(menu_text)

            ### This is the pause for input ###
            chosen, quit = menu.player_choice(loc_dict['options'], self.scr)
            ### This is the pause for input ###

            if quit == 1:
                break

            self.player.location = chosen['new_loc']
            self.player.time += chosen['time']

            # Check if we got an encounter
            outcome = choice(chosen['outcomes']['titles'], 1,
                             chosen['outcomes']['prob'])
            if outcome[0] != 'enc_nothing':
                encounter = main_encounters[outcome[0]]
                if encounter['type'] == 'battle':
                    enc_funcs.battle(encounter, self.scr)
                elif encounter['type'] == 'shop':
                    enc_funcs.shop(encounter, self.scr)
                else:
                    menu.add_text('Unsupported encounter type!')

            if self.player.time % 24 > 22 or self.player.time % 24 < 6:
                menu.add_text('It\'s late. You go to sleep... (ENTER)',
                              self.scr)
                menu.enter_wait(self.scr)
                self.advance_day()

            self.scr.refresh()
