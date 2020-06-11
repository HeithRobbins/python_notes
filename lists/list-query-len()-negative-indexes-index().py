tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)


tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags) # this will return 4 elements, but index is 0,1,2,3. 
print(number_of_tags)

last_item = tags[-1] #this targets the last element in the list and .
print(last_item) #print shows us it is "code"

index_of_last_item = tags.index(last_item) # using the variable we used to store "code" this saves it into a new variable and give the index value for it(because chances are in real world setting you are not going to know what it is)
print(index_of_last_item) 






NOTION NOTES

Overview of Python List Query Processes: len(), Negative Indexes, and index()

# tags = ['python', 'development', 'tutorials', 'code']

# number_of_tags = len(tags)

# last_item = tags[-1]

# index_of_last_item = tags.index(last_item)

# print(number_of_tags)

# print(last_item)

# print(index_of_last_item)

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags) #not the same as an index location. 4 tags, index of 0-3.

last_item = tags[-1] #this will ensure we are grabbing the last item

index_of_last_item = tags.index(last_item) #return index of last value

print(number_of_tags)

print(last_item)

print(index_of_last_item)