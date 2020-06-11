# # tags = (
# #     'python',
# #     'conding',
# #     'tutorials',
# #     'coding',
    
# # )

# # print(tags)

# # # Nope
# # # print(tags[0])

# # query_one = 'python' in tags
# # query_two = 'ruby' in tags


# # print(query_two)
# ''' need to understand how it write out flase'''

# """Various Methods for Merging Python Sets"""

# tags_one = {
#     'python',
#     'coding',
#     'tutorials',
#     'coding'
# }

# tags_two = {
#     'ruby',
#     'coding',
#     'tutorials',
#     'development'
# }

# # merged tags
# merged_tags = tags_one | tags_two
# print(merged_tags)

# # tags in tags_one but not in tags_two
# exclusive_to_tag_one = tags_one - tags_two
# print(exclusive_to_tag_one)

# # tags in tags_two but not in tags_one
# exclusive_to_tag_two = tags_two - tags_one
# print(exclusive_to_tag_two)

# # tags found in both tags_one and tags_two
# universal_tags = tags_one & tags_two
# print(universal_tags)

# thisset = {"apple", "banana", "cherry"}

# this_otherr = set()
# for x in thisset:
#     is x != "apple":
#         this_other.add(x)

# print(this_other)
# print(thisset)
    
''' rewatch video not really understanding this '''

'''Introduction to Python Loops'''

#  4 loop with only go for what you have



# while True:
#     print("hi")
    
    
    
# is_true = True

# while is true == true:
#     print('hi')
#     is_true = true


# '''How to Implement Python Loops for Lists, Tuples, and Dictionaries'''


#    players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
   
# #    what you diffened after for is a vaulable so you can change the  name 


#    for player in players:
#        print(player) 


# players = {
#     '2b': 'Altuve',
#     '3b': 'Bregman',
#     'ss': 'Correa',
#     'dh': 'Gattis',
# }
# for position, player in players.items():
#      print('position', position)
#      print('player Name', player)
    
    
    
'''key is frist, value next'''


'''                   How to Loop Through the Characters of a Python String               '''
            
# alphabet = 'abcdef'

# for letter in alphabet:
#     print(letter)


'''                 Guide to Looping Over Ranges in Python                              '''


# for num in range(1, 11, 2):
#     print(num)
    
    # when using ranges it like the same as a slice 
    
'''                     Guide to Continue and Break in Python Loops                     '''

# usernames = [ 
#     'jon',
#     'tyrion',
#     'theon',
#     'cersei',
#     'sansa',
# ]

# # for username in usernames:
# #     if username == 'cersei':
# #         print(f'sorry, {username}, you are not allowed')
# #         continue
# #     else:
# #         print(f'{username} is allowed')
        
# for username in usernames:
#     if username == 'cersei':
#         print(f'{username} was found at index {usernames.index(username)}')
#         break
#     print(username)

'''                 Overview of While Loops in Python               '''

# def guessing_game():
#     while True:
#         print('what is your guess?')
#         guess = input()
        
#         if guess == '42'
#             print('You correctly quessed it!')
#             return False
#     else:
#         print(f'No, {guess} is not the answer, please try again\n')
        
# guessing_game()

# nums = list(range(1, 100))

# while len(nums) > 0:
#     print(nums.pop())

''' remember he going to give us a test with using this '''
    
'''Guide to Continue and Break in Python Loops'''
    
    
    
# lagacy_customers = ['Alice', 'Bob']
# new_customers = ['Tiffany', 'Kristine']

# raw_db = [lagacy_customers, new_customers]

# print(raw_db)

# for lagacy_customers in lagacy_customers:
#     new_customers.append(lagacy_customers)
    
# print(new_customers)


'''introduction to list comprehension in Python'''



# num_list = range(1, 11)
# cubed_nums = []

# # for num in num_list:
# #   cubed_nums.append(num ** 3)

# cubed_nums = [num ** 3 for num in num_list]

# print(cubed_nums)

# even_numbers = []

# # doing this down below you are trying to found if this is even 
# for num in num_list:
#   if num % 2 == 0:
#     even_numbers.append(num)
#     # this take all your even number and putting them in a arrey from your num_list
# # when us append(num) you are tell it to add the number to the list but at the end beacue you are
# # using append so that make it go to the end 

# even_numbers = [num for num in num_list if num % 2 == 0]
# # using the above it will work but to me i dont like it but it dose save code space
# print(even_numbers)



