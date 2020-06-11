"""
heading_generator(title, heading_type)
heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Hi there', '3')
<h3>Hi there</h3>
"""

def heading_generator(h1, h3,):
    return (f'h1 "Greeting", + h3 "hi there')
  

""" answer for making a Generator """
# def heading_generator(title, heading_type):
#   return f'<h{heading_type}>{title}</h{heading_type}>'

# print(heading_generator('Greetings!', '1'))
# print(heading_generator('I am in a title', '3'))


# doing this with a if statement
# <h1>Greeting</h1>


# print(heading_generator('Greeting', 1))
# print(heading_generator('How are you doing today', 4))
# print(heading_generator('you are going to lose', 3))


def heading_generator(title, heading_type):

  if heading_type <= 6 and heading_type > 0:
    return f'<h{heading_type}>{title}</h{heading_type}>'
  else:
    return "Error: Heading must be between 1 and 6."


print(heading_generator("Greetings", 1))
