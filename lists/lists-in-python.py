"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)

print([users[2]])

users[4] = 'Brayden'

print(users)


LISTS

running a database query will return a list of items.

to INSERT items into a list user.insert("index value, list value")

"""

User Database Query

Kristine

Tiffany

Jordan

"""

users = ['Kristine', 'Tiffany', 'Jordan']

# users.insert(index, value)

users.insert(1, "Anthony")

users.append('Ian') #add item to the end of the list

print(users[2]) #print([users[2]]) returns item in its own list

users[4] = 'Brayden' #this will find the 4th user and replace the 4th item

print(users)
