
# def word_reverser(word):
#   word_container = []

#   for i in word:
#     word_container = i.split() + word_container

#   word_container = map(str, word_container)
#   reverse_word = "".join(word_container)

#   return reverse_word


# print(word_reverser("Ryan"))

# #######different way######
# def reverse_word(word):
#   return word[::-1]

# print(reverse_word("Ryan"))


def reverse_word(word):
  result = ""
  word_list = list(word)

  for litter in range(len(word_list)):
    result += word_list.pop()

  return result

print(reverse_word("Ryan"))