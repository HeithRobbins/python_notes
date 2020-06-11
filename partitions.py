heading = "Python: An Introduction and Python: Advanced"

header, _, subheader = heading.partition(': ')   # Within .partition('this is what will be removed')

print(header)
print(subheader) 

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)