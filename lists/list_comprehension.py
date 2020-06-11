# num_list = range(1,11)
# cubed_nums = []

# # for num in num_list:
# #     cubed_nums.append(num ** 3)
    
# cubed_nums = [num ** 3 for num in num_list]
    

# print(cubed_nums) 

num_list = range(1,11)

# even_number = []

# for num in num_list:
#     if num % 2 == 0:
#         even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))
print(even_numbers)


def remove_nums(omit):
  new_list = [num     for num in range(21) if num not in omit]
#             *Aciton |*Loop              |*Conditional
  return new_list


print(remove_nums([1,2,3]))