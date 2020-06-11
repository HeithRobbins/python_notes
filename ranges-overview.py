tags = ['python', 'development', 'tutorials', 'code', 'whatever', 'whatever again']

tag_range = tags[1:3]  # This is to grab both development and tutorials 

multiple_tag_ranges = tags[3:]  # Grabs from index 3 up to the end

print(tag_range)

print(multiple_tag_ranges)







NOTION NOTES


RANGES in python LISTS

# tags = ['python', 'development', 'tutorials', 'code']

# tag_range = tags[2:]

# tag_range = tags[0:2]

# tag_range = tags[:2]

# tag_range = tags[0:-1]

# print(tag_range)

tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[:2] #again, not the same as returning the index location.

tag_range = tags[:-1] #returns all but last item in list.

tag_range = tags[:] #returns it all.

print(tag_range)