

'''Basic Seyntax for Creating Python Functions'''


# def full_name(first, last):
#   print(f'{first} {last}')


# full_name('Kristine', 'Hudgens')


# def auth(email, password):
#   if email == 'kristine@hudgens.com' and password == 'secret':
#     print('You are authorized')
#   else:
#     print('You are not authorized')


# auth('kristine@hudgens.com', 'asdf')


# def hundred():
#   for num in range(1, 101):
#     print(num)


# hundred()


# def counter(max_value):
#   for num in range(1, max_value):
#     print(num)


# counter(501)


''' What Dose it Mean to Return a Value from a Python Functions '''

# def full_name(first, last):
#     return f'{first} {last}'
    
# kristine = full_name('Kristine', 'Hudgens')

# def greeting(name):
#     print(f'hi {name}!')
    
# greeting(kristine)

''' How to Nest Functions in Parent Functions in Python '''

'''whenever you're working with nested function is when should you choose to nest versus keep 
them separate. And one of my rules of thumb for it is whenever I have a function that does not 
need to exist outside of a parent function then that is a good time to perform nesting.'''

def greeting(first, last):
    def full_name():
        return f'{first} {last}'

    print(f'hi {full_name()}!')


greeting('Kristine', 'Hudgens')
