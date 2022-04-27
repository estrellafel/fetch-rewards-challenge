#
# This FastAPI has a few capabilites. An add route that allows for one to send a transaction
# to the app in the form of { "payer": <string>, "points": <integer>, "timestamp": <date>}.
# Then those points can be spent by calling the spend route which takes an input in the form 
# of { "payer": <string>, "points": <integer> } and returns how many points where spent from
# each payer. Lastly, there is a balance route which will show the remaining point balances 
# for each payer.
#
# Author: Felix Estrella
# Date: April 27, 2022
#

from fastapi import FastAPI
from payer import Payer
from spend import Spend

app = FastAPI() # Create a FastAPI instance
payer_list = [] # List used to store all the payers

# Home page to welcome the user
@app.get('/')
async def root():
    return 'Welcome to the fetch rewards challange'


# The add route which will will add a payer to the payer_list and returns the payer_dict
@app.post('/add')
async def add(payer: Payer):
    global payer_list

    payer_dict = payer.dict() # Convert player to a dictionary
    payer_list.append(payer_dict)

    # Make timestamp readable for when it is returned
    payer_dict['timestamp'] = payer_dict['timestamp'].strftime('%Y-%m-%dT%H:%M:%SZ')
    return payer_dict

# A route which will spend points from the payers in order of the payers timestamp
@app.post('/spend')
async def spend_points(spend: Spend):
    global payer_list

    spender = [] # Will keep track of who's points got spent
    payer_list.sort(key=lambda d: d['timestamp']) # Sort playerlist by the timestamp

    # Used to run through all the payers until the points are spent or no more payers have points
    i = 0 # Used to index through payer_list
    while spend.points > 0 and i < len(payer_list):
        # Stores the current player dictionary and instantiate values
        cur_payer = {'payer': '', 'points': 0}

        # Check to see if the current payer has already spent points
        for j in range(len(spender)):
            # If payer already spent point set cur_player points and remove old instance
            if payer_list[i]['payer'] == spender[j]['payer']:
                cur_payer['points'] = spender[j]['points']
                spender.pop(j)
                break

        cur_payer['payer'] = payer_list[i]['payer'] # Set the payers name

        # If the payer does not have any points pass through them
        if payer_list[i]['points'] == 0:
            pass
        
        # If the payer can only pay part of what was spent
        elif spend.points - payer_list[i]['points'] > 0:
            # Decrement the current payers points by payer points
            cur_payer['points'] -= payer_list[i]['points']
            # Decrement the amount of spending points still needing to be spent by the payer points
            spend.points -= payer_list[i]['points']
            payer_list[i]['points'] = 0 # Set payer points to zero

        # Else all the remaining spend points are taken on by one payer
        else:
            # Decrement the points by the points being spent
            cur_payer['points'] += -spend.points
            # Decrement the amount of spending points still needing to be spent by the payer points
            spend.points -= payer_list[i]['points']
            # Add the current player points to the player in the player list
            payer_list[i]['points'] += cur_payer['points']

        spender.append(cur_payer) # Append the cur_player as a spender

        i = i + 1
    
    return spender

# A route to get the point balance for all payers 
@app.get('/balance')
async def get_balanace():
    global payer_list

    ret_dict = {} # Used to store the results and get returned
    
    # For all payers, added them to the ret_dict while setting the points properly
    for d in payer_list:
        if d['payer'] in ret_dict:
            ret_dict[d['payer']] += d['points']
        else:
            ret_dict[d['payer']] = d['points']
            
    return ret_dict