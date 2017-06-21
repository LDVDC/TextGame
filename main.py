import curses
import game

this_game = game.Game()
wrap = curses.wrapper(this_game.main)
