import classes
import curses
import sys
from menu import menuOptions

class GameStart:
    def __init__(self, screen):
        self.scrn = screen
        self.menu = menuOptions(self.scrn)

    def loadChoice(self):
        load_options = [{'title':'New Game'},{'title':'Load Game'}]
        choice, quit = self.menu.player_choice(load_options)

        if quit == 1:
            sys.exit(0)

        if choice['title'] == 'New Game':
            self.newGame()
        else:
            # This is where the load game call would go
            self.menu.add_text('Not yet supported! Quitting...')
            sys.exit(0)

    def newGame(self):
        self.player = classes.Creature('cr_newplayer')
        self.player.location = 'loc_camp'
        self.player.time = 8
        while True:
            self.scrn.addstr(1, 0, 'What is your name?\n')
            curses.echo()
            curses.curs_set(1)
            player_name = self.scrn.getstr().decode()
            curses.noecho()
            curses.curs_set(0)
            if not player_name:
                self.menu.add_text('Please enter something!')
            else:
                self.player.name = player_name.title()
                break
