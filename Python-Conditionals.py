# age = 1500

# if age < 25:
#     print(f"I'm sorry, you need to be at least 25 years old")
# elif age > 100:
#     print(f"I'm sorry, {age} is too old to rent a car")
# else:
#     print(f"You're good to go, {age} fits in the range to rent a car.")

'''How to Use the Ternary Operator in Python Conditionals'''

# role = 'admin'

# # auth = 'can access' if role == 'admin' else 'cannot access'

# # print(auth)

# if role == 'admin':
#    auth = 'can access'
# else:
#    auth = 'cannot access'

# print(auth)

''' Full list of python Conditional Operators'''

# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# <= Less than
# <= Less than or equal to

# username = 'Jonsnow'

# if username == 'Jonsnow':
#     print('Welcome')
# else:
#     print('You shall not pass')

# user_list = ['Kristine', 'Tiffany']
# second_list = ['Kristine', 'Tiffany']

# if user_list == second_list:
#     print('They match')


''' How to check if a value is included in a python string or list'''

# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'dog'

# if word.lower() in sentence.lower():
#   print('The word is in the sentence')
# else:
#   print('The word is not in the sentence')


# nums = [1, 2, 3, 4]

# if 3 in nums:
#   print('The number was found')
# else:
#   print('The number was not found')

'''How to build compount conditionals in Python'''

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')
