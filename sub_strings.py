"""
sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('quick') #'quick' here is the substring
query_two = sentence.index('quick') 

print(query)
print(query_two)
"""

#find will return -1 if string is not found
#index will return an error if not found.divmod

"""
sentence = 'The quick brown fox jumped over the lazy dog.'

query = 'lazy' in sentence #returns true or false if found

print(query)
"""

sentence = 'The quick brown fox jumped over the lazy dog.'

query = 'oops' in sentence

if "oops" in sentence:

print(query) #check out substring video. Missed something here. 