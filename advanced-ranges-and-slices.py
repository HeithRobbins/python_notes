tags = [
  'python', 
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[:-1:2]   # This is used to grab EVERY OTHER index
reversed_tag_range = tags[::-1]  # This [::-1] is used to reverse a list

print(tags)
print(tag_range)
print(reversed_tag_range)


 



# NOTION NOTES


# Implementing Ranges and Slices in Python Lists

# # tags = [

# # 'python',

# # 'development',

# # 'tutorials',

# # 'code',

# # 'programming',

# # 'computer science'

# # ]

# # tag_range = tags[1:-1:2]

# # tag_range = tags[::-1]

# # print(tag_range)

# # tags.sort(reverse=True)

# # print(tags)

# tags = [

# 'python',

# 'development',

# 'tutorials',

# 'code',

# 'programming',

# 'computer science'

# ]

# # tag_range = tags[1:-1] # going to start with second element and go to last element but not include the last element. slices before last el. ""

# # tag_range = tags[ : -1: 2] #steps through items skipping each second item.

# tag_range = tags[ : : -1] #returns last to first because of the 'step' value using 'slice'

# print(tag_range)