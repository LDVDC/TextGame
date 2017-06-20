def player_choice(options):
    # Takes a list of dictionaries
    # Prints the options and returns the player's choice
    while True:
        choice_num = 1
        for option in options:
            print (str(choice_num) + ') ' + option['title'], end='  ')
            choice_num += 1
        choice = input()
        # Test to see if we can convert to integer
        try:
            choice = int(choice)
        except ValueError:
            pass
        # Check if it was a valid choice
        if choice in range(1,len(options) + 1):
            break
        else:
            print ('Invalid option!')
    return options[choice - 1]
