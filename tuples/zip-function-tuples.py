'''Guide to Python's Zip Function'''


positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players) #this shold combine them together

print(list(scoreboard)) #needs to be cast as a [list]