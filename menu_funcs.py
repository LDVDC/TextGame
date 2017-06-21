import datetime

def gen_menu(player,chosen,loc):
    menu_text = player.name + ' -- HP: ' + str(player.hp) + \
                ' Str: ' + str(player.stats['str']) + ' Dex: ' + \
                str(player.stats['dex']) + ' Int: ' + \
                str(player.stats['int'])
    menu_text += '\nLocation: ' + loc['name']
    menu_text += '\n' + str(datetime.timedelta(hours=player.time)) + '\n'
    menu_text += chosen['text'] + '\n'
    return menu_text

def player_choice(options, scrn):
    # Takes a list of dictionaries
    # Prints the options and returns the player's choice
    quit = 0
    while True:
        choice_num = 1
        choice_text = ''
        for option in options:
            choice_text += str(choice_num) + ') ' + option['title'] + '  '
            choice_num += 1
        scrn.addstr(choice_text)
        player_choice = chr(scrn.getch())
        # Test to see if we can convert to integer
        try:
            player_choice = int(player_choice)
        except ValueError:
            pass
        curY, curX = scrn.getyx()

        # Check if it was a valid choice
        if player_choice in range(1,len(options) + 1):
            break
        elif player_choice == 'q':
            scrn.addstr(curY + 2,0,'Do you want to quit? (y/n)')
            quit_choice = chr(scrn.getch())
            if quit_choice == 'y':
                quit = 1
                player_choice = 1
                break
            scrn.move(curY + 2,0)
            scrn.clrtoeol()
            scrn.move(curY,0)
        else:
            scrn.addstr(curY + 2,0,'Invalid Option!')
            scrn.move(curY,0)
    return options[player_choice - 1], quit

def enter_wait(scrn):
    while True:
        press = scrn.getch()
        if press == 10:
            break

def add_text(text, scrn):
    curY, curX = scrn.getyx()
    scrn.addstr(curY + 2, 0, text)
