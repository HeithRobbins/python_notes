# Given a list of integers, create a new list ranged from 0 to 20 omitting the numbers from the original
# list
# EX: [1, 3, 5] => 

# my_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

# # print(my_list)

# new_list = (1, 20)

# print(len(my_list))

def remove_nums(omit_list):
  num_list = list(range(20))

  for num in num_list:
    if num in omit_list:
      num_list.remove(num)
  return num_list

print(remove_nums([1,3,5]))