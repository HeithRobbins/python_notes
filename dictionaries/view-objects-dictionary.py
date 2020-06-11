players = {
    'ss': 'Correa',
    '2b': 'Altuve',
    '3b': 'Bregman',
    'DH': 'Gattis',
    'OF': 'Springer',
}
 
# print(players.keys()) #gives the keys of the dict
# print(players.items()) #gives the items of the dict
# print(players.values()) #gives the value of the dict
# print(players.values()[0]) #FAIL!!! Traceback (most recent call last):line 12, in <module>TypeError: 'dict_values' object is not subscriptable
# print(list(players.values())[1]) #gives index location now we can treat it like a list by saying list at the begening of the print call 

player_names = list(players.copy().values()) #displays the values of the players list AND makes a copy of the dict for further meddling. this saves the original dictionary(when needed)

# print(player_names)





teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}
 
team_groupings = teams.items()

print(len(team_groupings))


# https://docs.python.org/3.0/library/stdtypes.html#dictionary-view-objects