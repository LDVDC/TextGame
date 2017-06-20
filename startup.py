from choice import player_choice
import classes
import sys

class GameStart:
    def loadChoice(self):
        load_options = [{'title':'New Game'},{'title':'Load Game'}]
        choice = player_choice(load_options)
        if choice['title'] == 'New Game':
            self.newGame()
        else:
            # This is where the load game call would go
            print ('Not yet supported! Quitting...')
            sys.exit(0)

    def newGame(self):
        print ('New Game!')
        self.player = classes.Creature('cr_newplayer')
        self.player.location = 'loc_camp'
        self.player.time = 8
        while True:
            print ('What is your name?')
            player_name = input()
            if not player_name:
                print ('Please enter something!')
            else:
                self.player.name = player_name.title()
                break
