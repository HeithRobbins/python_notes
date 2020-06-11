'''How to Add Elements to a Tuple by Leveraging Re-Assignment'''




# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# post += ('published',) #short hand for 'post = post + ('published',)'

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)




'''SECOND EXAMPLE USING ID FUNCTION'''

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',) #short hand for 'post = post + ('published',)'
print(id(post))

