sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)   # As opposed to .sort(), sorted() is used by placing the list INSIDE the ()   .sort() permanetaley changes the list
reversed_sorted_list = sorted(sale_prices, reverse=True)   # To reverse, add a second argument


print(sale_prices)
print(sorted_list)
print(reversed_sorted_list)






# NOTION NOTES

# SORTED FUNCTION python

# # sale_prices = [

# # 100,

# # 83,

# # 220,

# # 40,

# # 100,

# # 400,

# # 10,

# # 1,

# # 3

# # ]

# # sorted_list = sorted(sale_prices, reverse=True)

# # print(sorted_list)

# sale_prices = [

# 100,

# 83,

# 220,

# 40,

# 100,

# 400,

# 10,

# 1,

# 3

# ]

# # sale_prices.sort()

# # sorted_list = sale_prices.sort()

# # print(sorted_list) #this will not store in a new variable.

# sorted_list = sorted(sale_prices)

# print(sorted_list)

# print(sale_prices)

# # sort and sorted. if the order of the list is going to be neccessary, DO NOT SORT. use sorted and get your copy from that and do with as you will

# write me a program that takes a string and sorts it in alphabetical order

str="hi there"
str2 = "".join(sorted(str))
print(str2)