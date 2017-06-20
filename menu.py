from locations import main_locations
import startup
import datetime

game_start = startup.GameStart()
game_start.loadChoice()
player = game_start.player

class Menu:
    def gen_menu(self):
        self.cur_loc = main_locations[player.location]
        menu_text = player.name + ' -- HP: ' + str(player.hp) + \
                    ' Str: ' + str(player.stats['str']) + ' Dex: ' + \
                    str(player.stats['dex']) + ' Int: ' + \
                    str(player.stats['int'])
        menu_text += '\nLocation: ' + self.cur_loc['name']
        menu_text += '\n' + str(datetime.timedelta(hours=player.time)) + '\n'
        menu_text += self.outcome['text'] + '\n'
        return menu_text

    def advance_day(self):
        player.location = 'loc_camp'
        if player.time % 24 > 8:
            player.time += 24
        player.time += 8 - (player.time % 24)

    def enter_wait(self):
        while True:
            press = self.screen.getch()
            if press == 10:
                break

    def player_choice(self, options):
        # Takes a list of dictionaries
        # Prints the options and returns the player's choice
        quit = 0
        while True:
            choice_num = 1
            choice_text = ''
            for option in options:
                choice_text += str(choice_num) + ') ' + option['title'] + '  '
                choice_num += 1
            self.screen.addstr(choice_text)
            choice = chr(self.screen.getch())
            # Test to see if we can convert to integer
            try:
                choice = int(choice)
            except ValueError:
                pass
            curY, curX = self.screen.getyx()

            # Check if it was a valid choice
            if choice in range(1,len(options) + 1):
                break
            elif choice == 'q':
                self.screen.addstr(curY + 2,0,'Do you want to quit? (y/n)')
                quit_choice = chr(self.screen.getch())
                if quit_choice == 'y':
                    quit = 1
                    choice = 1
                    break
                self.screen.move(curY + 2,0)
                self.screen.clrtoeol()
                self.screen.move(curY,0)
            else:
                self.screen.addstr(curY + 2,0,'Invalid Option!')
                self.screen.move(curY,0)
        return options[choice - 1], quit

    def main(self, stdscr):
        self.screen = stdscr
        self.outcome = {'text':'You\'re standing in camp'}
        # Main gameplay loop
        while True:
            self.screen.clear()

            menu_text = self.gen_menu()
            self.screen.addstr(menu_text)

            ### This is the pause for input ###
            self.outcome, quit = self.player_choice(self.cur_loc['options'])
            ### This is the pause for input ###

            if quit == 1:
                break

            player.location = self.outcome['new_loc']
            player.time += self.outcome['time']

            if player.time % 24 > 22 or player.time % 24 < 6:
                curY, curX = self.screen.getyx()
                self.screen.addstr(curY + 2,0,
                                   'It\'s late. You go to sleep... (ENTER)')
                self.enter_wait()
                self.advance_day()

            self.screen.refresh()
