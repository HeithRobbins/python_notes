# def greeting(**kwargs):
#     print(kwargs)
    
# greeting()
# # if i print this now it going to bring me a {}dictionary


def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first='Kristine', last='Hudgens')
