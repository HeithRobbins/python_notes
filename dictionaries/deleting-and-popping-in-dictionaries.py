teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['astros'] #deletes the astros 
# del teams(teams.get('mets', 'no team')) #for when you never need the value

teams.pop('yankees', 'no team')
# removed_teams = teams.pop('angels', 'no team') #to remove and use a element


print(teams)
# print(removed_teams)
print(teams)
