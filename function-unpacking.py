
# when starting off with unpacking (*)then (*args) stands for arguments
# def greeting(*args):
#     # when ever you us args again you don't need to (*) you only need that when you are calling a function
#   print('Hi ' + ' '.join(args))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')

# try not to using this one even though it work it not good code
# def greeting(*names):
#   print('Hi ' + ' '.join(names))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')0 

# when you are do two diffenert function you are going to call the frist one ever time with (args)
def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")

 
greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')
