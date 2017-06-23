main_creatures = {
    'cr_newplayer':{
        'name':'New Player',
        'stats':{'str':2,'dex':2,'def':2,'int':2,'maxhp':50,'crit_ch':0.02},
        'moves':{
            'detail':[{'title':'Attack','dmg':5},
                      {'title':'Run','dmg':0}],
            'prob':[0.5,0.5]
        },
        'xp_rew':0,
        'lvl':1
    },
    'cr_goblin':{
        'name':'Goblin',
        'stats':{'str':1,'dex':1,'def':1,'int':1,'maxhp':40,'crit_ch':0.01},
        'moves':{
            'detail':[{'title':'attack','dmg':5},
                      {'title':'big_attack','dmg':10}],
            'prob':[0.8,0.2]
        },
        'xp_rew':20,
        'lvl':2
    }
}
