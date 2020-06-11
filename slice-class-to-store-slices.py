tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]


print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])






NOTION NOTES (THIS MAY NOT BELONG HERE)


Implementing Ranges and Slices in Python Lists

# tags = [

# 'python',

# 'development',

# 'tutorials',

# 'code',

# 'programming',

# 'computer science'

# ]

# tag_range = tags[1:-1:2]

# tag_range = tags[::-1]

# print(tag_range)

# tags.sort(reverse=True)

# print(tags)

tags = [

'python',

'development',

'tutorials',

'code',

'programming',

'computer science'

]

# tag_range = tags[1:-1] # going to start with second element and go to last element but not include the last element. slices before last el. ""

# tag_range = tags[ : -1: 2] #steps through items skipping each second item.

tag_range = tags[ : : -1] #returns last to first because of the 'step' value using 'slice'

print(tag_range)
