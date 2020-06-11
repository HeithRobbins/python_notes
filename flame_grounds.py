
name = 'flame'
# print(name.index(''))

def destroy(string):
    first_two = name[:2]
    second_two = name[3:]
    new_name = first_two + second_two
    
    print(new_name)
    
    # if new_name != name:
    if len(new_name) < len(name):
        f_two = new_name[:2] + new_name[:2]
        
        print(f_two)
            
        if len(f_two) == len(new_name):
            last_name = f_two[:1]
            print(last_name)
            
            
destroy(name)
print(destroy(name))



# # import math

# # loss = -20.25
# # product_cost = 89.99

# # print(abs(loss)) #does not need math library
# # print(math.floor(product_cost)) #does need math library. 
# # print(math.ceil(product_cost)) #similar to floor, only returns an int but rounds it up.
# # print(abs(math.floor(loss))) # 
# # print(round(product_cost))
# # print(math.sqrt(product_cost))
# # print(math.pow(5, 2))
# # print(5 ** 2)

# import math

# loss = -20.25
# product_cost = 89.99

# print(abs(loss))