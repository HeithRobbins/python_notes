'''Three Ways to Remove Elements from a Python Tuple'''


post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')

#removing elements from end
# post = post[:-1]

#removing elements from beginning
# post = post[1:]

#removing specfic element (MESSY/NOT RECOMMENDED)
post = list(post) #this is changing post from a tuple to a list
post.remove('published')
post = tuple(post) #this casts this back into a tuple from a list. 

print(post)

