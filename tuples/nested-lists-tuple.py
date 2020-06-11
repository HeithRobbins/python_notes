'''Working with Lists Nested in Tuples'''

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# tags = ['python', 'coding', 'tutorial']

# post += (tags, )
# print(post[-1][-1])



post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags, )#includes tags list into post tuple

print(post[-1][1]) #gives access to 'coding'

