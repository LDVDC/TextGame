import datetime

class menuOptions:
    def __init__(self, screen):
        self.scrn = screen

    def gen_menu(self, player, chosen, loc):
        menu_text = player.name + ' -- HP: ' + str(player.hp) + \
                    ' Str: ' + str(player.stats['str']) + ' Dex: ' + \
                    str(player.stats['dex']) + ' Int: ' + \
                    str(player.stats['int'])
        menu_text += '\nLocation: ' + loc['name']
        menu_text += '\n' + str(datetime.timedelta(hours=player.time)) + '\n'
        menu_text += chosen['text'] + '\n'
        return menu_text

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
            self.scrn.addstr(choice_text)
            player_choice = chr(self.scrn.getch())
            # Test to see if we can convert to integer
            try:
                player_choice = int(player_choice)
            except ValueError:
                pass

            # Check if it was a valid choice
            if player_choice in range(1,len(options) + 1):
                break
            elif player_choice == 'q':
                self.add_text('Do you want to quit? (y/n)')
                quit_choice = chr(self.scrn.getch())
                player_choice = 1
                if quit_choice == 'y':
                    quit = 1
                    break
                elif quit_choice == 'n':
                    self.add_text('')
                    pass
                else:
                    self.add_text('Invalid Option!')
            else:
                self.add_text('Invalid Option!')
        return options[player_choice - 1], quit

    def enter_wait(self):
        while True:
            press = self.scrn.getch()
            if press == 10:
                break

    def add_text(self, text):
        curY, curX = self.scrn.getyx()
        self.scrn.move(curY + 2, 0)
        self.scrn.clrtoeol()
        self.scrn.addstr(curY + 2, 0, text)
        self.scrn.move(curY, 0)
