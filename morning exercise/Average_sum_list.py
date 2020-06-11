# from functools import reduce

# ####Jordon way of doing it for founding the mean of the list#############

# def get_average(num_list):
#     total = reduce(
#         (lambda total, element: total + element),
#         num_list)

#     return total /len(num_list)

# num_list = [1,2,3,4,5,6]

# print(get_average(num_list))


# andy answer for mean

def get_average(*args):
    return sum(args) / len(args)

print(get_average(1,2,3,4,5))