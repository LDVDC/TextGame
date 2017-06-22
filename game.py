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

    def encounter(self, enc_name):
        enc_dict = main_encounters[enc_name]
        self.scr.clear()
        self.scr.addstr('Battle Time!' + enc_dict['creature'])
        self.scr.getch()

    def main(self, stdscr):
        # Start the game!
        curses.curs_set(0)
        self.scr = stdscr
        menu = menuOptions(self.scr)
        game_start = startup.GameStart(self.scr)
        game_start.loadChoice()
        self.player = game_start.player

        chosen = {'text':'You\'re standing in camp'}
        # Main gameplay loop
        while True:
            self.scr.clear()

            loc_dict = main_locations[self.player.location]
            menu_text = menu.gen_menu(self.player,chosen,loc_dict)
            self.scr.addstr(menu_text)

            ### This is the pause for input ###
            chosen, quit = menu.player_choice(loc_dict['options'])
            ### This is the pause for input ###

            if quit == 1:
                break

            self.player.location = chosen['new_loc']
            self.player.time += chosen['time']

            # Generate the outcome
            outcome = choice(chosen['outcomes']['titles'], 1,
                             chosen['outcomes']['prob'])
            # Check if we got an encounter
            if outcome[0] != 'enc_nothing':
                new_enc = events.newEncounter(menu, self.player)
                encounter = main_encounters[outcome[0]]
                if encounter['type'] == 'battle':
                    new_enc.battle(encounter)
                elif encounter['type'] == 'shop':
                    new_enc.shop(encounter)
                else:
                    menu.add_text('Unsupported encounter type!')

            if self.player.time % 24 > 22 or self.player.time % 24 < 6:
                menu.add_text('It\'s late. You go to sleep... (ENTER)')
                menu.enter_wait()
                self.advance_day()

            self.scr.refresh()
