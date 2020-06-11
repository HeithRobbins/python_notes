# https: // www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)



NOTION NOTES


Using the JOIN Function in Python to Build a URL Query String

# https://www.google.com/search?q=python+development+tutorial

# uri = 'https://www.google.com/search?q='

# tags = ['python', 'development', 'tutorial']

# formatted_tags = '+'.join(tags)

# query_uri = f'{uri}{formatted_tags}'

# print(query_uri)

uri = 'https://www.google.com/search?q=python+development+tutorial'

tags = ['python', 'development', 'tutorial']

formatted_tags = '+'.join(tags)

query_uri = f'{uri}{formatted_tags}'

print(query_uri)