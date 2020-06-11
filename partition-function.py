"""
heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ') #variable deconstruction. '_,' this indicates a throwaway value you dont need to use. it removed the :. 

print(header)
print(subheader)
"""


heading = "Python: An Introduction"

first, second, third = heading.partition(': ') #giving an example that "header" and "first" represent the same thing. 

print(first)
print(third)