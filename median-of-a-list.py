"""
Tools:
- math library
- sorted function
- list slicing
- computations

need to sort the list, then split the list in 2 in order to find the median

"""
import math

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

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)






NOTION NOTES (and failed attempts at making it work)

Find MEDIAN of python LIST with an odd number of numbers. 

# import math

# """

# Tools:

# - math library

# - sorted function

# - list slicing

# - computations

# """

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

# sorted_list = sorted(sale_prices)

# num_of_sales = len(sorted_list)

# half_slice = math.floor(num_of_sales/2)

# first_sales_items = sorted_list[:half_slice]

# last_sales_items = sorted_list[-(half_slice):]

# median = sorted_list[half_slice:(half_slice + 1)]

# print(sorted_list)

# print(num_of_sales)

# print(first_sales_items)

# print(last_sales_items)

# print(median

"""

Tools:

- math library

- sorted function

- list slicing

- computations

"""

import math

sale_prices = [

100,

83,

220,

40,

100,

400,

10,

1,

3,

]

sorted_list = sorted(sale_prices)

print(sorted_list)

length_list = len(sale_prices)

print(length_list)

divided_list = math.floor(length_list / 2)

print(divided_list)

print(sorted_list[divided_list])

# first_list = sorted_list[0:4]

# print(first_list)

# second_list = sorted_list[4:9]

# print(second_list)

# sorted_list = sorted(sale_prices)

# print(sorted_list)

# new_list = sorted_list[4:6]

# print(new_list)

# sum_list = sum(new_list)

# print(sum_list)

# divide_list = sum_list / 2

# print(divide_list)



import math


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


def find_median_odd(num_list):
  sorted_list = sorted(num_list)
  list_length_mid = len(num_list)/2

  return sorted_list[math.floor(list_length_mid)]

print(find_median_odd(sale_prices))