from lib.data.creatures import main_creatures

class Creature:
    def __init__(self, cr_type):
        cr_dict = main_creatures[cr_type]
        self.stats = cr_dict['stats']
        self.name = cr_dict['name']
        self.hp = cr_dict['stats']['maxhp']
        self.lvl = cr_dict['lvl']
        self.moves = cr_dict['moves']
        self.xp = 0
        self.next_xp = 100
        self.xp_on_kill = cr_dict['xp_rew']
