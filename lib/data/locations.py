main_locations = {
    'loc_camp':{
        'name':'Camp',
        'options':[
            {'title':'Walk','new_loc':'loc_camp','time':1,
             'text':'You take a walk',
             'outcomes':{
                'details':[{'title':'enc_goblin'},{'title':'enc_nothing'}],
                'prob':[0.2,0.8]}
            },
            {'title':'Go Somewhere',
            'new_loc':'loc_chooseplace',
            'time':0,'text':'You decide where to go',
            'outcomes':{
                'details':[{'title':'enc_nothing'}],
                'prob':[1]}
            },
            {'title':'Sleep','new_loc':'loc_camp','time':6,
            'text':'You go to sleep',
            'outcomes':{
                'details':[{'title':'enc_nothing','hp_reg':0.2}],
                'prob':[1]}
            }]
    },
    'loc_chooseplace':{
        'name':'Choosing where to go',
        'options':[
            {'title':'Woods','new_loc':'loc_woods','time':0,
             'text':'You go to the woods',
             'outcomes':{
                'details':[{'title':'enc_nothing'}],
                'prob':[1]}
            },
            {'title':'Nevermind','new_loc':'loc_camp','time':0,
             'text':'On second thoughts, you go back to camp',
             'outcomes':{
                'details':[{'title':'enc_nothing'}],
                'prob':[1]}
            }]
    },
    'loc_woods':{
        'name':'Woods',
        'options':[
            {'title':'Explore','new_loc':'loc_woods','time':1,
             'text':'You explore the woods',
             'outcomes':{
                'details':[{'title':'enc_goblin'},{'title':'enc_nothing'}],
                'prob':[0.4,0.6]}
            },
            {'title':'Go Back to Camp','new_loc':'loc_camp','time':1,
             'text':'You head back to camp',
             'outcomes':{
                'details':[{'title':'enc_nothing'}],
                'prob':[1]}
            }]
    }
}
