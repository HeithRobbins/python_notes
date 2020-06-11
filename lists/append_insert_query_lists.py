users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(1, 'Anthony')  #index location where you want it inserted, what you want inserted

print(users)

users.append('Ian') #adds the element to the end of the list

print(users)




print(users[2]) #we queried the item in the list, and returns it out of the list

print([users[2]]) #same query but in a list

users[4] = 'Brayden' #This reassigned the element at index 4 to Brayden. It did not change Ian to Brayden. 

print(users)


