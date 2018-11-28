# -*- coding: utf-8 -*-

import datetime
import json

def checkCapacity(contents):
    """ Contents are expected as a dictionary of the form {item_id:(volume,value), ...} """
    """ This function returns True if the knapsack is within capacity; False if the knapsack is overloaded """
    load = 0
    if isinstance(contents,dict):
        for this_key in contents.keys():
            load = load + contents[this_key][0]
        if load <= knapsack_cap:
            return True
        else:
            return False
    else:
        print("function checkCapacity() requires a dictionary")

def knapsack_value(items):
    value = 0.0
    if isinstance(items,dict):
        for this_key in items.keys():
            value = value + items[this_key][1]
        return(value)
    else:
        print("function knapsack_value() requires a dictionary")

def getData():
    f = open('knapsack.json','r')
    x = json.load(f)
    f.close()
    for i in range(len(x)):
        myData = x[i]['data']
        x[i]['data'] = {}
        for j in range(len(myData)):
            x[i]['data'][j] = tuple(myData[j]) 
    return x

def loadKnapsack(items,in_knapsack,knapsack_cap):
    """ You write this function which is your heuristic knapsack algorithm
    
        You may indicate one or more items to put into the backpack within a list data structure
        by returning a list of values corresponding to the dictionary keys for the inserted items
    
        If you are finished loading the knapsack, then return any string value  """
        
    """ Compute existing load in knapsack """
    my_team_number = 9    # always return this variable as the first item
    items_to_pack = []    # use this list for the indices of the items you load into the knapsack
    
    load = 0.0            # use this variable to keep track of how much volume is already loaded into the backpack
    for this_key in in_knapsack:
        load += in_knapsack[this_key][0]
        
    """
    Code your algorithm here
    """
                
    return my_team_number, 'finished'                     # use this statement when you have filled the backpack
        

""" Main code """
""" Get data and define problem ids """
probData = getData()
problems = range(len(probData))

for problem_id in problems:
    in_knapsack = {}
    knapsack_cap = probData[problem_id]['cap']
    items = probData[problem_id]['data']
    finished = False
    response = None
    
    while finished == False:
        timeStart = datetime.datetime.now()
        team_num, response = loadKnapsack(items,in_knapsack,knapsack_cap)
        timeFinish = datetime.datetime.now()
        if not isinstance(response,str):
            for this_key in response:
                if this_key in items.keys():
                    in_knapsack[this_key] = items[this_key]
                    del items[this_key]
                else:
                    print()
                    print("loadKnapsack() returned a response that was neither a key found in the items dictionary, nor")
                    print("was it a string value which indicating the knapsack loading process was complete.")
                    print("It will be assumed that the knapsack is fully loaded.")
                    finished = True
        else:
                print()
                print("Problem ", str(problem_id), "Knapsack Loaded....")
                finished = True
                
    knapsack_ok = checkCapacity(in_knapsack)
    print('Is solution feasible for Problem '+str(problem_id)+'? ',knapsack_ok)
    print('Knapsack value: ',knapsack_value(in_knapsack))
    print('Execution time: ',timeFinish-timeStart)