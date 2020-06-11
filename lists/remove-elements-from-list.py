users = ['Kristine', 'Tiffany', 'Jordan', 'Lean']


print(users)

users.remove('Jordan')

print(users)

popped_users = users.pop()   #the popped user on the end will be stored in popped_user variable

print(popped_users)
print(users)

del users[0]

print(users)




users = ['Kristine','Tiffany','Jordan','Leann']

print(users)

users.remove('Jordan') #removes from the list

print(users)

popped_user = users.pop() #does not delete the item, but returns the item for further use. this will store the user in the variable "popped_user"

print(popped_user)
print(users)

del users[0] #delets the value
print(users)




NOTION NOTES

REMOVE items from LISTS

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan') #takes the value of what you want removed.

print(users)

popped_user = users.pop() #pop doesnt delete, it returns the item for futher use.

print(popped_user)

print(users)

del users[0] #this will delete an item [index value]. Need to know value and index location

print(users)
