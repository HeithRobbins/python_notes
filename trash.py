# def simple():
#     print("my first function")
    
# simple()

# a = 100

# def plus_ten(a):
#     result = a + 10
#     outcome = result
#     print('outcome:' )
#     return result

# print(plus_ten(a))

# def wage(w_hours):
#     return w_hours * 25

# def with_bonus(w_hours):
#     return wage(w_hours) + 50

# wage(8), with_bonus(8)

# print(wage(8), with_bonus(8))


# def add_10(m):
#     if m >= 100:
#         m = m + 10
#         return m
        
#     # if m <= 100:
#     #     print('Save More!') #my way of doing it
#     else: 
#         return "Save More!!!"
        
# add_10(90) # calls the function. print shows what the result of this is. 

# print(add_10(90))


# word = 'flame'

# def slicer(string):
#     left_two = word[:2]
#     right_two = word[-2:]
#     new_word = left_two + right_two

#     if len(word) < 2:
#         print('Empty String')
#     else:
#         return new_word
    
# slicer(word)
# print(slicer(word))



# word = "Hello"

# # def reverse_it(string):
# #     return(word[: : -1])
    
# # print(reverse_it(word))



# # reversedString=[]

# # index = len(word)
# # while index > 0:
# #     reversedString += word[ index -1 ]
# #     index = index - 1

# # print(reversedString)



# reversedstring = ''.join(reversed(word))

# print(reversedstring)



# def subtract_bc(a, b, c):
#     result = a - b * c
#     print ("Parameter a equals", a)
#     print ("Parameter b equals", b)  ##this is a internet example. 
#     print ("Parameter c equals", c)
#     return result
    

# print(subtract_bc(5, 10, 10))


# [
    
#     [0, 1, 2, 3, 4],
#     [1, 2, 3, 4, 5],
#     [2, 3, 4, 5, 6],
#     [3, 4, 5, 6, 7],
#     [4, 5, 6, 7, 8],

# ]



# def manual_matrix(n):
#     matrix = [ [ None for y in range(n)] for x in range(n) ]
#     return matrix
    

# print(manual_matrix(5))


# def manual_matrix(n):
#     matrix = [ [ None for x in range(n)] for y in range(n) ] # None is our value/element, x is the inner lists, range gives us how many(n=5), y is how many lists
#     counter = 0
#     for idx, el in enumerate(matrix):
#         for nested_idx, nested_el in enumerate(el):
#             matrix [idx][nested_idx] = counter + nested_idx
#         counter += 1

#     return matrix

# print(manual_matrix(5))


# name = "tyson"

# def increment():
#     x = 0
#     while x < 10:
#         x += 1    
#     return name

# print(increment()) 


# name = "tyson"
# def increment(argument):
#     x = 0
#     while x < 10:
#         x += 1    
#         return name
# print(increment(name))


name = "tyson"
another_name = "daniel"
def increment(argument):
    x = 0
    while x < 10:
        x += 1    
        print(argument)
increment(name)
increment(another_name)