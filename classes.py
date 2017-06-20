from creatures import main_creatures

class Creature:
    def __init__(self, cr_type):
        cr_dict = main_creatures[cr_type]
        self.stats = cr_dict['stats']
        self.name = cr_dict['name']
        self.hp = cr_dict['stats']['maxhp']
