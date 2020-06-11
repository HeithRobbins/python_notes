# The quick brown fox jumped 
  # the T is at an index of 0, h is 1, e is 2 and "space" is 3. 

starter_sentence = "the quick brown fox jumped"
print(starter_sentence[0])

# starter_sentence = "the quick brown fox jumped"
# first_word = starter_sentence[0:3]
# new_sentence = first_word
# print(new_sentence)

# strings are immutable once created. 

starter_sentence = "The quick brown fox jumped"

new_sentence = "Thy" + starter_sentence[3:]

print(new_sentence)


# print(starter_sentence.replace('The', 'Thy'))