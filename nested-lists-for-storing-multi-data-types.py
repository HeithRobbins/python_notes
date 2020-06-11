users = ['Kristine', 'Tiffany', 'Jordan', 'Lean']
ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)


# Guide to Nested Lists and Best Practices for Storing Multiple Data Types in a Python List

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']
# print(users)

ids = [1, 2, 3, 4]


mixed_list = [42, 10.3, "Altuve", ['Kristine', 'Tiffany', 'Jordan', 'Leann']] # nested list, below is a better way to do this...
# print(mixed_list)


mixed_list = [42, 10.3, "Altuve", users] # much better, mo clean
print(mixed_list)

user_list = mixed_list.pop() #this is saying to pop the mixed list out of the user variable. 

print(user_list)
print(mixed_list)



#mixed lists are dangerous. if you are not aware that it contains strings, and you call a mathematical funciton to it, it would break the program. 


nested_lists = [ [123], [234], [345] ] # try and keep the data types the same when using nested lists. 





NOTION NOTES

NESTED LISTS and best practices for storing multiple data types in a python list. 

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users] #added a variable with a list to the variable "mixed_list"

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)

print(mixed_list)

#DANGER! When adding items to a list, you could break it if its only a integer list and you add a "string" item.

nested_lists = [[123], [456], [345]] #much wow.

DONT MIX DATA TYPES IN YO LISTS. keep them uniform if possible.