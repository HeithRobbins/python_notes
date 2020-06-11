teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  'red sox':['Price', 'Betts'],
}

# featured_team = teams['mets'] #this failed to run, and breaks the program
featured_team = teams.get('yankees', 'No featured') #get takes two args, first is the key "mets" second is the value or message. (like an if else statement, if mets is false, return key/value statement)

print(featured_team)

