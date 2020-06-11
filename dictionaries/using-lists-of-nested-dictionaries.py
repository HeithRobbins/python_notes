'''Guide to Working with Lists of Nested Dictionaries'''
            '''this is original code'''
# teams = [
#   {
#     'astros': {
#       '2B': 'Altuve',
#       'SS': 'Correa',
#       '3B': 'Bregman',
#     }
#   },
#   {
#     'angels': {
#       'OF': 'Trout',
#       'DH': 'Pujols',
#     }
#   }
# ]

# # print(teams[0])

# angels = teams[1].get('angels', 'Team not found')

# print(list(angels.values())[1])





"""this is mine"""

teams = [
    {
    'astros': {
        '2B': 'Altuve',
        'SS': 'Correa',
        '3B': 'Bregman',
        }
    },
    {
    'angels':{
        'OF': 'Trout',
        'DH': 'Pujols',
            }
    }
]

# print(teams[0]) #index of astros in teams 


angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1]) #finding the value at index 1