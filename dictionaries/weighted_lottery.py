import random

#i need a container: he makes a list = container_list
#i need to loop through my container
    # uses for loop
        #for (name*this assignes to the key, weight*this assignes to the value)
        #nests another for loop 


my_weights = {
    'winning': 1,
    'break-even': 2,
    'losing':  3,
}

def weighted_lottery(weights):
    # print(weights) to check to see if it calls my dict
    container = []
    counter = 0
    for key, value in weights.items(): #this breaks out our items
        counter = 0
        while counter < value:
            container.append(key)
            counter +=1
    print(random.choice(container))   #need to import random for this to work. random is built in function in python
weighted_lottery(my_weights)
    
































'''MY UNSUCCESSFUL ATTEMPTS'''




# #should take weights as the argument

# # i need to return winning one time, and losing 1000 times randomly
# # i need a function that will iterate over my dictionary 

# import random

# weights = {
#         'winning': 1,
#         'losing': 1000,
# }


# weighted_lottery(weights):
    


# # print("The winner is : " + str(weights))

# # res = key, val = random.choice(list(weights.items())) 

# # print("The winner is : " + str(res))










# # def weighted_lottery(string):
# #     winner = random.shuffle(weights)
    
    
# # weighted_lottery(weights(winner))
# # print(weighted_lottery(weights))
# # print()

# # other_weights = {
# #         'winning': 1,
# #         'break_even': 2,
# #         'losing': 3


# # weighted_lottery(other_weights)



    

    