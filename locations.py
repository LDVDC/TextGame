main_locations = {
    'loc_camp':{
        'name':'Camp',
        'options':[{'title':'Walk','new_loc':'loc_camp','time':1,
                    'text':'You take a walk'},
                   {'title':'Go Somewhere',
                    'new_loc':'loc_chooseplace',
                    'time':0,'text':'You decide where to go'},
                   {'title':'Sleep','new_loc':'loc_camp','time':6,
                    'text':'You go to sleep'}]
    },
    'loc_chooseplace':{
        'name':'Choosing where to go',
        'options':[{'title':'Woods','new_loc':'loc_woods','time':0,
                    'text':'You go to the woods'},
                   {'title':'Nevermind','new_loc':'loc_camp','time':0,
                    'text':'On second thoughts, you go back to camp'}]
    },
    'loc_woods':{
        'name':'Woods',
        'options':[{'title':'Explore','new_loc':'loc_woods','time':1,
                    'text':'You explore the woods'},
                   {'title':'Go Back to Camp','new_loc':'loc_camp','time':1,
                    'text':'You head back to camp'}]
    }
}
