import classes
import curses
import sys
from menu_funcs import player_choice, add_text

class GameStart:
    def loadChoice(self, scrn):
        load_options = [{'title':'New Game'},{'title':'Load Game'}]
        choice, quit = player_choice(load_options, scrn)
        if choice['title'] == 'New Game':
            self.newGame(scrn)
        else:
            # This is where the load game call would go
            add_text('Not yet supported! Quitting...', scrn)
            sys.exit(0)

    def newGame(self, scrn):
        self.player = classes.Creature('cr_newplayer')
        self.player.location = 'loc_camp'
        self.player.time = 8
        while True:
            add_text('What is your name?', scrn)
            curses.echo()
            player_name = scrn.getstr().decode()
            curses.noecho()
            if not player_name:
                add_text('Please enter something!', scrn)
            else:
                self.player.name = player_name.title()
                break
