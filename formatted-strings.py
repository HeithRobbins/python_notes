name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'
#old school format way of doing it
greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')
#way mo'bettah way of using format to interpolate. 
greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting)