import curses
import menu

game = menu.Menu()
wrap = curses.wrapper(game.main)
