from locations import main_locations
from encounters import main_encounters
from creatures import main_creatures
import startup
from numpy.random import choice
import menu_funcs as menu

game_start = startup.GameStart()
game_start.loadChoice()
player = game_start.player

class Game:
    def advance_day(self):
        player.location = 'loc_camp'
        if player.time % 24 > 8:
            player.time += 24
        player.time += 8 - (player.time % 24)

    def encounter(self, enc_name):
        enc_dict = main_encounters[enc_name]
        self.scr.clear()
        self.scr.addstr('Battle Time!' + enc_dict['creature'])
        self.scr.getch()

    def main(self, stdscr):
        self.scr = stdscr
        chosen = {'text':'You\'re standing in camp'}
        # Main gameplay loop
        while True:
            self.scr.clear()

            loc_dict = main_locations[player.location]
            menu_text = menu.gen_menu(player,chosen,loc_dict)
            self.scr.addstr(menu_text)

            ### This is the pause for input ###
            chosen, quit = menu.player_choice(loc_dict['options'], self.scr)
            ### This is the pause for input ###

            if quit == 1:
                break

            player.location = chosen['new_loc']
            player.time += chosen['time']

            # Check if we got an encounter
            outcome = choice(chosen['outcomes']['titles'], 1,
                             chosen['outcomes']['prob'])
            outcome = outcome[0]
            if outcome != 'enc_nothing':
                self.encounter(outcome)

            if player.time % 24 > 22 or player.time % 24 < 6:
                curY, curX = self.scr.getyx()
                self.scr.addstr(curY + 2,0,
                                'It\'s late. You go to sleep... (ENTER)')
                self.enter_wait(self.scr)
                self.advance_day()

            self.scr.refresh()
