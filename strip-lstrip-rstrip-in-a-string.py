url = 'https://google.com'

print(url.strip('https://')) #this will remove https://

url = url.lstrip('https://') # this will lstrip l is for the left so going to strip the left side
url = url.rstrip('.com') # this will be right rstrip is for the right side

print(url.capitalize()) # this using capitalize like we done be for it caps the frist letter





# REPL NOTES

"""
url = 'https://google.com'

print(url.strip("https://"))
"""

"""
url = 'https://google.com'

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)
"""

url = 'https://google.com'

print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com')
 
print(url.capitalize())